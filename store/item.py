"""Canonical item model and URL normalization."""

from __future__ import annotations

import hashlib
import re
from dataclasses import asdict, dataclass, field, fields, replace
from datetime import datetime, timezone
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

# Params that carry no meaning and would otherwise split one story into several.
TRACKING_PREFIXES = ("utm_",)
TRACKING_EXACT = {"ref", "fbclid", "gclid", "igshid", "mc_cid", "mc_eid"}

_ARXIV_PATH = re.compile(r"^/(?:abs|pdf)/(.+?)(?:v\d+)?(?:\.pdf)?$")


def utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def iso_utc(value: str | None) -> str | None:
    """Coerce a source timestamp onto the same `...Z` shape as `first_seen`.

    Sources disagree: Algolia sends `2026-09-20T17:21:03.000Z`, GitHub sends
    `...Z`, arXiv sends `...Z`. An unparseable stamp is returned untouched —
    a slightly odd string still beats silently dropping the only date we have.
    """
    if not value:
        return None
    text = str(value).strip()
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return text
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def normalize_url(url: str) -> str:
    """Collapse cosmetically different URLs onto one canonical form."""
    parts = urlsplit(url.strip())
    host = parts.netloc.lower()
    if host.startswith("www."):
        host = host[4:]

    path = parts.path
    if host == "arxiv.org":
        match = _ARXIV_PATH.match(path)
        if match:
            path = f"/abs/{match.group(1)}"
    if len(path) > 1 and path.endswith("/"):
        path = path[:-1]

    query = sorted(
        (k, v)
        for k, v in parse_qsl(parts.query, keep_blank_values=True)
        if k.lower() not in TRACKING_EXACT
        and not k.lower().startswith(TRACKING_PREFIXES)
    )
    return urlunsplit(("https", host, path, urlencode(query), ""))


def item_id(normalized_url: str) -> str:
    return hashlib.sha1(normalized_url.encode("utf-8")).hexdigest()[:12]


@dataclass
class Item:
    id: str
    url: str
    normalized_url: str
    title: str
    source: str
    first_seen: str
    text: str = ""
    meta: dict = field(default_factory=dict)
    sent_in: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Item":
        """Build from a stored row, ignoring keys this version does not know.

        A future writer adding a field must not make today's reader raise
        TypeError in the middle of loading the pool.
        """
        known = {f.name for f in fields(cls)}
        return cls(**{k: v for k, v in data.items() if k in known})


def make_item(
    url: str,
    title: str,
    source: str,
    text: str = "",
    meta: dict | None = None,
    now: str | None = None,
) -> Item:
    """Build an Item, or raise ValueError if it could not be identified.

    The id is derived from the normalized URL, so a URL with no host
    normalizes to "https://" and every malformed item across every source
    collapses onto that single id — dedupe would then silently eat real
    stories. Rejecting here makes that failure loud and local: it surfaces
    inside the source's own per-item try/except instead of poisoning the pool.
    """
    if not isinstance(title, str) or not title.strip():
        raise ValueError(f"item has no usable title: {title!r} (url {url!r})")
    if not isinstance(url, str):
        raise ValueError(f"item url is not a string: {url!r}")
    normalized = normalize_url(url)
    if not urlsplit(normalized).netloc:
        raise ValueError(f"item url has no host: {url!r} -> {normalized!r}")
    return Item(
        id=item_id(normalized),
        url=url.strip(),
        normalized_url=normalized,
        title=title.strip(),
        source=source,
        first_seen=now or utcnow(),
        text=text,
        meta=meta or {},
    )


def combine(base: Item, other: Item, refresh_title: bool = False) -> Item:
    """Fold a duplicate of `base` into it, returning the merged row.

    The longer `text` wins: an HN link post carries none, while the blog row
    for the same URL carries the excerpt, and dropping it loses the only prose
    the Judge would have had. `meta` is unioned with the newer values on top,
    so HN's points/kind and a blog's published date both survive and volatile
    counters refresh. The earliest `first_seen` stands — it is the record of
    when the story entered the pool.
    """
    return replace(
        base,
        title=other.title if (refresh_title and other.title) else base.title,
        text=other.text if len(other.text or "") > len(base.text or "") else base.text,
        meta={**(base.meta or {}), **(other.meta or {})},
        first_seen=min(base.first_seen, other.first_seen),
    )


def dedupe(items: list[Item]) -> list[Item]:
    """Collapse each id onto one row, merging collisions, preserving order."""
    index: dict[str, int] = {}
    out: list[Item] = []
    for item in items:
        position = index.get(item.id)
        if position is None:
            index[item.id] = len(out)
            out.append(item)
        else:
            out[position] = combine(out[position], item)
    return out

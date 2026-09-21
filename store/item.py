"""Canonical item model and URL normalization."""

from __future__ import annotations

import hashlib
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

# Params that carry no meaning and would otherwise split one story into several.
TRACKING_PREFIXES = ("utm_",)
TRACKING_EXACT = {"ref", "fbclid", "gclid", "igshid", "mc_cid", "mc_eid"}

_ARXIV_PATH = re.compile(r"^/(?:abs|pdf)/(.+?)(?:v\d+)?(?:\.pdf)?$")


def utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


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
        return cls(**data)


def make_item(
    url: str,
    title: str,
    source: str,
    text: str = "",
    meta: dict | None = None,
    now: str | None = None,
) -> Item:
    normalized = normalize_url(url)
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


def dedupe(items: list[Item]) -> list[Item]:
    """Keep the first occurrence of each id, preserving order."""
    seen: set[str] = set()
    out: list[Item] = []
    for item in items:
        if item.id in seen:
            continue
        seen.add(item.id)
        out.append(item)
    return out

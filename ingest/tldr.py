"""Fetch and parse a TLDR AI issue.

Not a pool source: nothing here ever becomes a digest item. It exists so the
day's rival newsletter can be put next to ours for a blind comparison.
"""

from __future__ import annotations

import re

from ingest.http import get_text
from ingest.text import plain

ISSUE_URL = "https://tldr.tech/ai/{date}"

_ARTICLE = re.compile(r"<article\b[^>]*>(.*?)</article>", re.IGNORECASE | re.DOTALL)
_H3 = re.compile(r"<h3\b[^>]*>(.*?)</h3>", re.IGNORECASE | re.DOTALL)
# The fallback shape: a headline followed by prose, up to the next headline or
# section header. Used when the page drops <article> wrappers, which it has.
_H3_PAIR = re.compile(
    r"<h3\b[^>]*>(.*?)</h3>(.*?)(?=<h[23]\b|<footer\b|</body)", re.IGNORECASE | re.DOTALL
)
# "(5 minute read)", "(GitHub Repo)", "(Sponsor)" — the suffix TLDR appends to
# every headline. Both newsletters carry reading times, so it is stripped from
# each of them rather than being left as a tell.
READ_SUFFIX = re.compile(r"\s*\((?:\d+\s*minute\s*read|sponsor|github\s*repo)\)\s*$", re.IGNORECASE)
_SPONSOR = re.compile(r"\(sponsor\)|sponsored\b", re.IGNORECASE)


def _clean(title: str) -> str:
    return READ_SUFFIX.sub("", plain(title)).strip()


def parse(raw: str) -> list[dict]:
    """Extract the issue's stories as `{title, summary}`, sponsors dropped."""
    blocks: list[tuple[str, str]] = []
    for match in _ARTICLE.finditer(raw):
        block = match.group(1)
        headline = _H3.search(block)
        if not headline:
            continue
        blocks.append((headline.group(1), _H3.sub(" ", block)))
    # Quick-links sections drop the <article> wrapper, and some issues drop it
    # everywhere. Whatever is left after the articles are removed is paired by
    # headline, so both shapes are read in one pass.
    blocks += [
        (m.group(1), m.group(2)) for m in _H3_PAIR.finditer(_ARTICLE.sub(" ", raw))
    ]

    stories = []
    for headline, body in blocks:
        if _SPONSOR.search(plain(headline)):
            continue
        title = _clean(headline)
        summary = READ_SUFFIX.sub("", plain(body)).strip()
        if not title or not summary:
            continue
        stories.append({"title": title, "summary": summary})
    return stories


def fetch(date: str, timeout: int = 20) -> list[dict]:
    """Today's issue, or `[]` when there is none — TLDR skips weekends."""
    try:
        raw = get_text(ISSUE_URL.format(date=date), timeout=timeout)
    except RuntimeError as exc:
        print(f"no tldr issue for {date}: {exc}")
        return []
    return parse(raw)

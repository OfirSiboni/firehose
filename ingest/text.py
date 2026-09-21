"""HTML to plain text. Feeds are HTML; the Judge should read prose."""

from __future__ import annotations

import html
import re

_TAGS = re.compile(r"<[^>]+>")


def plain(raw: str) -> str:
    """Strip tags, decode entities, collapse whitespace.

    Tags become a space, not nothing, so "<p>a</p><p>b</p>" is "a b" not "ab".
    Unescaping happens after stripping so escaped markup stays text.
    """
    return " ".join(html.unescape(_TAGS.sub(" ", raw)).split())

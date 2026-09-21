"""HTML to plain text. Feeds are HTML; the Judge should read prose."""

from __future__ import annotations

import html
import re

# Tag stripping alone keeps the *bodies* of script and style, so a feed with
# inline JS would hand minified code to the Judge as prose.
_BLOCKS = re.compile(r"<(script|style)\b[^>]*>.*?</\1\s*>", re.IGNORECASE | re.DOTALL)
_TAGS = re.compile(r"<[^>]+>")


def plain(raw: str) -> str:
    """Strip tags, decode entities, collapse whitespace.

    Tags become a space, not nothing, so "<p>a</p><p>b</p>" is "a b" not "ab".
    Unescaping happens after stripping so escaped markup stays text.
    """
    return " ".join(html.unescape(_TAGS.sub(" ", _BLOCKS.sub(" ", raw))).split())

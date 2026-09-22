"""Render the static site, the Markdown mirror and the RSS feed.

One template each, no framework.
"""

from __future__ import annotations

import html
import re
from datetime import datetime, timezone
from pathlib import Path

from store import REPO_ROOT, digests, pool, ranked

DOCS = REPO_ROOT / "docs"
SITE_URL = "https://ofirsiboni.github.io/firehose"

PAGE = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Firehose — {date}</title>
<link rel="alternate" type="application/rss+xml" href="feed.xml">
<style>
  :root {{ color-scheme: light dark; }}
  body {{ max-width: 42rem; margin: 2rem auto; padding: 0 1rem;
         font: 16px/1.6 system-ui, sans-serif; }}
  h1 {{ font-size: 1.4rem; }}
  article {{ margin: 1.75rem 0; }}
  h2 {{ font-size: 1.05rem; margin: 0 0 .35rem; }}
  .meta {{ opacity: .6; font-size: .85rem; }}
  .tail li {{ margin: .4rem 0; }}
  footer {{ margin-top: 3rem; opacity: .6; font-size: .85rem; }}
</style></head><body>
<h1>Firehose — {date}</h1>
{articles}
<h2>Also in the pool</h2>
<ul class="tail">{tail}</ul>
<footer><a href="feed.xml">RSS</a> · <a href="{date}.md">Markdown</a></footer>
</body></html>
"""

ARTICLE = """<article>
<h2><a href="{url}">{title}</a></h2>
<p>{summary}</p>
<p class="meta">{tier} · {source}</p>
</article>"""


def render_digest(digest: dict, tail: list[dict]) -> str:
    articles = "\n".join(
        ARTICLE.format(
            url=html.escape(item["url"]),
            title=html.escape(item["title"]),
            summary=html.escape(item.get("summary", "")),
            tier=html.escape(item.get("tier", "")),
            source=html.escape(item.get("source", "")),
        )
        for item in digest["items"]
    )
    tail_html = "\n".join(
        f'<li><a href="{html.escape(t["url"])}">{html.escape(t["title"])}</a>'
        f' <span class="meta">{html.escape(t.get("source", ""))}</span></li>'
        for t in tail
    )
    return PAGE.format(date=html.escape(digest["date"]), articles=articles, tail=tail_html)


# Only the characters that mean something *inline*: emphasis, code, link
# brackets and raw HTML. `+`, `#` and friends are block syntax — escaping them
# mid-sentence just litters the raw file, so they are handled at line start.
MD_SPECIAL = re.compile(r"([\\`*_\[\]<])")
MD_BULLET_START = re.compile(r"^([#>+-])")
MD_NUMBER_START = re.compile(r"^(\d+)([.)])")


def md_escape(text: str) -> str:
    """Neutralize markdown in text that goes into a link label or a paragraph."""
    escaped = MD_SPECIAL.sub(r"\\\1", str(text or "").replace("\n", " ")).strip()
    escaped = MD_BULLET_START.sub(r"\\\1", escaped)
    # A leading "1." would start an ordered list; the dot is the escapable part
    # (a backslash before a digit is not a markdown escape at all).
    return MD_NUMBER_START.sub(r"\1\\\2", escaped)


def md_url(url: str) -> str:
    """Make a URL safe as a markdown link target.

    Parens inside an inline link close it early, so percent-encode them; a
    stray space would do the same, so encode that too.
    """
    return str(url or "").replace("(", "%28").replace(")", "%29").replace(" ", "%20")


def render_markdown(digest: dict, tail: list[dict]) -> str:
    """The day's digest as Markdown, served alongside the HTML page.

    Deliberately no YAML front matter: GitHub Pages runs Jekyll, and front
    matter would make it render <date>.md into <date>.html, overwriting the
    page rendered above.
    """
    date = digest["date"]
    lines = [f"# Firehose — {date}", ""]

    for item in digest["items"]:
        lines += [
            f"## [{md_escape(item['title'])}]({md_url(item['url'])})",
            "",
            f"`{md_escape(item.get('tier', ''))}` · {md_escape(item.get('source', ''))}",
            "",
            md_escape(item.get("summary", "")),
            "",
        ]

    if tail:
        lines += ["## Also in the pool", ""]
        lines += [
            f"- [{md_escape(t['title'])}]({md_url(t['url'])}) — {md_escape(t.get('source', ''))}"
            for t in tail
        ]
        lines.append("")

    lines += ["---", "", f"[Web]({SITE_URL}/{date}.html) · [RSS]({SITE_URL}/feed.xml)", ""]
    return "\n".join(lines)


def render_feed(digest_list: list[dict]) -> str:
    entries = []
    for digest in digest_list:
        body = "<br><br>".join(
            f"<b>{html.escape(i['title'])}</b><br>{html.escape(i.get('summary', ''))}"
            f"<br><a href=\"{html.escape(i['url'])}\">link</a>"
            for i in digest["items"]
        )
        entries.append(
            "<item>"
            f"<title>Firehose — {digest['date']}</title>"
            f"<link>{SITE_URL}/{digest['date']}.html</link>"
            f"<guid isPermaLink=\"false\">{digest['date']}</guid>"
            f"<description>{html.escape(body)}</description>"
            "</item>"
        )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0"><channel>'
        "<title>Firehose</title>"
        f"<link>{SITE_URL}</link>"
        "<description>Daily AI stories worth your time.</description>"
        + "".join(entries)
        + "</channel></rss>"
    )


def main() -> int:
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    digest = digests.load_digest(date)
    if not digest:
        print("no digest today; nothing to publish")
        return 0

    sent_ids = {item["id"] for item in digest["items"]}
    try:
        payload = ranked.load_ranked({i.id for i in pool.load_pool()})
        # No exclusions here, deliberately: discussion threads can't be digest
        # items but are useful research, and the tail is where you go looking.
        tail = [i for i in ranked.top(payload, 28) if i["id"] not in sent_ids][:20]
    except Exception as exc:
        print(f"tail unavailable: {exc}")
        tail = []

    DOCS.mkdir(parents=True, exist_ok=True)
    page = render_digest(digest, tail)
    (DOCS / f"{date}.html").write_text(page, encoding="utf-8")
    (DOCS / "index.html").write_text(page, encoding="utf-8")

    markdown = render_markdown(digest, tail)
    (DOCS / f"{date}.md").write_text(markdown, encoding="utf-8")
    (DOCS / "latest.md").write_text(markdown, encoding="utf-8")

    (DOCS / "feed.xml").write_text(render_feed(digests.recent_digests(20)), encoding="utf-8")
    print(f"published {date} (html + md) with a {len(tail)}-item tail")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Render the static site and RSS feed. One template, no framework."""

from __future__ import annotations

import html
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
<footer><a href="feed.xml">RSS</a></footer>
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
    (DOCS / "feed.xml").write_text(render_feed(digests.recent_digests(20)), encoding="utf-8")
    print(f"published {date} with a {len(tail)}-item tail")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

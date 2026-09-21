from datetime import datetime, timedelta, timezone
from pathlib import Path

from ingest.sources import blogs

FIXTURE = Path(__file__).parent / "fixtures" / "blog_sample.xml"


def load(days: int = 100000):
    return blogs.parse(FIXTURE.read_text(encoding="utf-8"), "example.com", days=days)


def test_parses_every_entry():
    assert len(load()) == 2


def test_strips_tracking_params_from_the_link():
    assert load()[0].normalized_url == "https://example.com/blog/model-x"


def test_strips_html_from_the_description():
    assert load()[0].text == "Model X runs at 2x the speed."


def test_decodes_entities_that_survive_xml_unescaping():
    # Feeds routinely double-escape: the XML carries &amp;#x27;, feedparser
    # hands back &#x27;, and only plain() turns it into an apostrophe.
    assert load()[1].text == "Some photos from the team's retreat."


def test_records_the_feed_name_in_meta():
    assert load()[0].meta["feed"] == "example.com"


def test_source_is_blog():
    assert load()[0].source == "blog"


def test_load_feeds_ignores_comments_and_blank_lines(tmp_path):
    path = tmp_path / "feeds.txt"
    path.write_text(
        "# a comment\n\nhttps://a.com/rss\n   \nhttps://b.com/rss  \n",
        encoding="utf-8",
    )
    assert blogs.load_feeds(path) == ["https://a.com/rss", "https://b.com/rss"]


def _feed(pubdate_line: str) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel><title>T</title>
<item><title>Post</title><link>https://example.com/p</link>{pubdate_line}<description>d</description></item>
</channel></rss>"""


def _rfc822(dt: datetime) -> str:
    return dt.strftime("%a, %d %b %Y %H:%M:%S GMT")


def test_drops_entries_older_than_the_window():
    old = datetime.now(timezone.utc) - timedelta(days=400)
    assert blogs.parse(_feed(f"<pubDate>{_rfc822(old)}</pubDate>"), "example.com", days=14) == []


def test_keeps_entries_inside_the_window():
    fresh = datetime.now(timezone.utc) - timedelta(days=2)
    assert len(blogs.parse(_feed(f"<pubDate>{_rfc822(fresh)}</pubDate>"), "example.com", days=14)) == 1


def test_keeps_entries_with_no_date():
    assert len(blogs.parse(_feed(""), "example.com", days=14)) == 1


def test_published_is_normalized_to_utc_z():
    fresh = datetime.now(timezone.utc) - timedelta(days=2)
    item = blogs.parse(_feed(f"<pubDate>{_rfc822(fresh)}</pubDate>"), "example.com", days=14)[0]
    assert item.meta["published"] == fresh.strftime("%Y-%m-%dT%H:%M:%SZ")


def test_published_is_none_when_the_entry_carries_no_date():
    item = blogs.parse(_feed(""), "example.com", days=14)[0]
    assert item.meta["published"] is None


def test_text_is_not_truncated_at_the_old_two_thousand_cap():
    body = "word " * 1000  # ~5000 chars of prose
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel><title>T</title>
<item><title>Post</title><link>https://example.com/p</link><description>{body}</description></item>
</channel></rss>"""
    assert len(blogs.parse(xml, "example.com", days=14)[0].text) > 2000


def test_an_entry_with_a_hostless_link_does_not_lose_the_feed(capsys):
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel><title>T</title>
<item><title>Good</title><link>https://example.com/good</link><description>d</description></item>
<item><title>Relative</title><link>/relative/path</link><description>d</description></item>
</channel></rss>"""
    assert [i.title for i in blogs.parse(xml, "example.com", days=14)] == ["Good"]
    assert "skipped" in capsys.readouterr().err

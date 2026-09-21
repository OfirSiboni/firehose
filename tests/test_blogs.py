from pathlib import Path

from ingest.sources import blogs

FIXTURE = Path(__file__).parent / "fixtures" / "blog_sample.xml"


def load():
    return blogs.parse(FIXTURE.read_text(encoding="utf-8"), "example.com")


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

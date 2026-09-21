from send import publish

DIGEST = {
    "date": "2026-09-21",
    "sent": True,
    "items": [
        {"id": "a", "title": "Model X ships", "url": "https://x/a", "source": "blog",
         "tier": "headline", "summary": "It runs 2x faster. (3 minute read)"},
    ],
}
TAIL = [{"title": "Also worth a look", "url": "https://x/z", "source": "hn"}]


def test_digest_page_contains_the_headline_and_summary():
    html = publish.render_digest(DIGEST, TAIL)
    assert "Model X ships" in html
    assert "It runs 2x faster." in html


def test_digest_page_contains_the_tail():
    assert "Also worth a look" in publish.render_digest(DIGEST, TAIL)


def test_digest_page_escapes_html_in_titles():
    risky = {**DIGEST, "items": [{**DIGEST["items"][0], "title": "<script>x</script>"}]}
    assert "<script>x</script>" not in publish.render_digest(risky, [])


def test_feed_is_valid_rss_with_one_item_per_digest():
    xml = publish.render_feed([DIGEST])
    assert xml.startswith("<?xml")
    assert "<rss version=\"2.0\">" in xml
    assert xml.count("<item>") == 1
    assert "2026-09-21" in xml

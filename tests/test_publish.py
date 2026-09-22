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


def test_markdown_contains_the_headline_summary_and_link():
    md = publish.render_markdown(DIGEST, TAIL)
    assert "# Firehose — 2026-09-21" in md
    assert "## [Model X ships](https://x/a)" in md
    assert "It runs 2x faster." in md
    assert "`headline` · blog" in md


def test_markdown_contains_the_tail():
    md = publish.render_markdown(DIGEST, TAIL)
    assert "## Also in the pool" in md
    assert "- [Also worth a look](https://x/z) — hn" in md


def test_markdown_has_no_front_matter_so_jekyll_leaves_it_alone():
    # Front matter would make Pages render <date>.md over <date>.html.
    assert not publish.render_markdown(DIGEST, TAIL).startswith("---")


def test_markdown_escapes_syntax_in_titles():
    # The escaped brackets are what keep the link label from closing early.
    risky = {**DIGEST, "items": [{**DIGEST["items"][0], "title": "[x](y) *bold* <b>"}]}
    md = publish.render_markdown(risky, [])
    assert "## [\\[x\\](y) \\*bold\\* \\<b>](https://x/a)" in md


def test_markdown_leaves_block_punctuation_in_prose_alone():
    prose = {**DIGEST["items"][0], "summary": "Loss fell +2.23 to 0.1 (3 minute read)"}
    md = publish.render_markdown({**DIGEST, "items": [prose]}, [])
    assert "Loss fell +2.23 to 0.1 (3 minute read)" in md


def test_markdown_escapes_block_syntax_only_at_line_start():
    items = [
        {**DIGEST["items"][0], "summary": "- not a bullet"},
        {**DIGEST["items"][0], "summary": "1. not a list"},
        {**DIGEST["items"][0], "summary": "# not a heading"},
    ]
    md = publish.render_markdown({**DIGEST, "items": items}, [])
    assert "\\- not a bullet" in md
    assert "1\\. not a list" in md
    assert "\\# not a heading" in md


def test_markdown_encodes_parens_in_urls():
    risky = {**DIGEST, "items": [{**DIGEST["items"][0], "url": "https://x/a_(b)"}]}
    assert "(https://x/a_%28b%29)" in publish.render_markdown(risky, [])


def test_digest_page_links_to_the_markdown_mirror():
    assert 'href="2026-09-21.md"' in publish.render_digest(DIGEST, TAIL)


def test_feed_is_valid_rss_with_one_item_per_digest():
    xml = publish.render_feed([DIGEST])
    assert xml.startswith("<?xml")
    assert "<rss version=\"2.0\">" in xml
    assert xml.count("<item>") == 1
    assert "2026-09-21" in xml

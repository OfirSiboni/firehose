import pytest

from store.item import Item, dedupe, iso_utc, item_id, make_item, normalize_url


@pytest.mark.parametrize(
    "raw,expected",
    [
        # tracking params are stripped
        ("https://example.com/post?utm_source=x&utm_medium=y", "https://example.com/post"),
        ("https://example.com/post?ref=hn", "https://example.com/post"),
        # scheme and www are canonicalized
        ("http://www.example.com/post", "https://example.com/post"),
        # trailing slash is dropped, but the root path survives
        ("https://example.com/post/", "https://example.com/post"),
        ("https://example.com/", "https://example.com/"),
        # arxiv pdf and versioned urls collapse onto /abs/
        ("https://arxiv.org/pdf/2509.12345v2.pdf", "https://arxiv.org/abs/2509.12345"),
        ("https://arxiv.org/abs/2509.12345v1", "https://arxiv.org/abs/2509.12345"),
        ("https://arxiv.org/abs/2509.12345", "https://arxiv.org/abs/2509.12345"),
        # meaningful query params survive and are sorted
        ("https://example.com/a?b=2&a=1", "https://example.com/a?a=1&b=2"),
    ],
)
def test_normalize_url(raw, expected):
    assert normalize_url(raw) == expected


def test_normalize_url_strips_whitespace():
    assert normalize_url("  https://example.com/post  ") == "https://example.com/post"


def test_item_id_is_stable_and_short():
    a = item_id("https://example.com/post")
    b = item_id("https://example.com/post")
    assert a == b
    assert len(a) == 12


def test_item_id_differs_by_url():
    assert item_id("https://example.com/a") != item_id("https://example.com/b")


def test_make_item_populates_derived_fields():
    item = make_item(
        url="http://www.example.com/post/?utm_source=hn",
        title="A Title",
        source="hn",
        text="body",
        meta={"points": 100},
        now="2026-09-21T06:00:00Z",
    )
    assert item.normalized_url == "https://example.com/post"
    assert item.id == item_id("https://example.com/post")
    assert item.first_seen == "2026-09-21T06:00:00Z"
    assert item.source == "hn"
    assert item.meta == {"points": 100}
    assert item.sent_in is None


def test_make_item_defaults_now_to_utc_z():
    item = make_item(url="https://example.com/x", title="T", source="hn")
    assert item.first_seen.endswith("Z")
    assert item.text == ""
    assert item.meta == {}


def test_round_trip_dict():
    item = make_item(url="https://example.com/x", title="T", source="hn", text="b")
    assert Item.from_dict(item.to_dict()) == item


def test_dedupe_keeps_first_occurrence_of_equivalent_urls():
    a = make_item(url="https://example.com/post", title="First", source="hn")
    b = make_item(url="http://www.example.com/post/?utm_source=x", title="Second", source="blog")
    out = dedupe([a, b])
    assert len(out) == 1
    assert out[0].title == "First"


def test_dedupe_preserves_distinct_items():
    a = make_item(url="https://example.com/a", title="A", source="hn")
    b = make_item(url="https://example.com/b", title="B", source="hn")
    assert len(dedupe([a, b])) == 2


def test_make_item_rejects_a_url_with_no_host():
    # normalize_url("") is "https://", so an unguarded source would collapse
    # every malformed row onto one id and dedupe would eat real stories.
    with pytest.raises(ValueError, match="no host"):
        make_item(url="", title="T", source="hn")


def test_make_item_rejects_a_pathless_relative_url():
    with pytest.raises(ValueError, match="no host"):
        make_item(url="/relative/path", title="T", source="hn")


def test_make_item_rejects_a_non_string_url():
    with pytest.raises(ValueError):
        make_item(url=None, title="T", source="hn")


def test_make_item_rejects_a_non_string_title():
    # title.strip() on a None used to raise AttributeError out of parse(),
    # costing the whole source its run instead of one item.
    with pytest.raises(ValueError, match="title"):
        make_item(url="https://example.com/x", title=None, source="hn")


def test_make_item_rejects_a_blank_title():
    with pytest.raises(ValueError, match="title"):
        make_item(url="https://example.com/x", title="   ", source="hn")


def test_dedupe_merges_rather_than_dropping_the_duplicate():
    # The headline case: a blog post trends on HN. The HN row carries points
    # but no text; the blog row carries the excerpt. Neither may be lost.
    hn_row = make_item(
        url="https://example.com/post",
        title="First",
        source="hn",
        meta={"points": 45, "kind": "article"},
        now="2026-09-20T12:00:00Z",
    )
    blog_row = make_item(
        url="http://www.example.com/post/?utm_source=x",
        title="Second",
        source="blog",
        text="The full excerpt.",
        meta={"published": "2026-09-20T09:00:00Z"},
        now="2026-09-21T12:00:00Z",
    )
    out = dedupe([hn_row, blog_row])
    assert len(out) == 1
    assert out[0].text == "The full excerpt."
    assert out[0].meta["points"] == 45
    assert out[0].meta["published"] == "2026-09-20T09:00:00Z"
    assert out[0].first_seen == "2026-09-20T12:00:00Z"
    assert out[0].title == "First"


def test_dedupe_keeps_the_longer_text_whichever_side_it_is_on():
    a = make_item(url="https://example.com/p", title="A", source="blog", text="long body")
    b = make_item(url="https://example.com/p", title="B", source="hn", text="")
    assert dedupe([a, b])[0].text == "long body"


def test_from_dict_ignores_unknown_keys():
    # One unknown key in a future pool row must cost that key, not the run.
    row = make_item(url="https://example.com/x", title="T", source="hn").to_dict()
    row["future_field"] = "whatever"
    assert Item.from_dict(row).title == "T"


def test_iso_utc_normalizes_the_shapes_sources_send():
    assert iso_utc("2026-09-21T06:00:00.000Z") == "2026-09-21T06:00:00Z"
    assert iso_utc("2026-09-21T06:00:00Z") == "2026-09-21T06:00:00Z"
    assert iso_utc("2026-09-21T08:00:00+02:00") == "2026-09-21T06:00:00Z"
    assert iso_utc(None) is None
    assert iso_utc("") is None

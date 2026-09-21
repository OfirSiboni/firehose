import pytest

from store.item import Item, dedupe, item_id, make_item, normalize_url


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

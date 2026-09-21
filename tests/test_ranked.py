import pytest

from store import ranked
from store.item import make_item

POOL_IDS = {"aaa111", "bbb222"}


def payload(**overrides):
    base = {
        "generated_at": "2026-09-21T07:02:11Z",
        "pool_size": 2,
        "read_count": 1,
        "items": [
            {
                "id": "aaa111", "url": "https://x/a", "title": "A", "source": "hn",
                "tier": "headline", "score": 9.0, "saturation": 0.9,
                "reason": "Big release.", "read": True,
                "key_facts": ["ships today"], "dedupe_of": None,
            },
            {
                "id": "bbb222", "url": "https://x/b", "title": "B", "source": "arxiv",
                "tier": "discovery", "score": 4.0, "saturation": 0.1,
                "reason": "Incremental, no code.", "read": False,
                "key_facts": [], "dedupe_of": None,
            },
        ],
    }
    base.update(overrides)
    return base


def test_valid_payload_passes():
    ranked.validate_ranked(payload(), POOL_IDS)


def test_missing_items_key_is_rejected():
    with pytest.raises(ranked.ValidationError, match="items"):
        ranked.validate_ranked({"generated_at": "x"}, POOL_IDS)


def test_unknown_id_is_rejected():
    bad = payload()
    bad["items"][0]["id"] = "ghost9"
    with pytest.raises(ranked.ValidationError, match="not in pool"):
        ranked.validate_ranked(bad, POOL_IDS)


def test_duplicate_ids_are_rejected():
    bad = payload()
    bad["items"][1]["id"] = "aaa111"
    with pytest.raises(ranked.ValidationError, match="duplicate"):
        ranked.validate_ranked(bad, POOL_IDS)


def test_out_of_range_score_is_rejected():
    bad = payload()
    bad["items"][0]["score"] = 42
    with pytest.raises(ranked.ValidationError, match="score"):
        ranked.validate_ranked(bad, POOL_IDS)


def test_bad_tier_is_rejected():
    bad = payload()
    bad["items"][0]["tier"] = "amazing"
    with pytest.raises(ranked.ValidationError, match="tier"):
        ranked.validate_ranked(bad, POOL_IDS)


def test_missing_reason_is_rejected():
    bad = payload()
    bad["items"][0]["reason"] = ""
    with pytest.raises(ranked.ValidationError, match="reason"):
        ranked.validate_ranked(bad, POOL_IDS)


def test_top_returns_highest_scores_first():
    assert [i["id"] for i in ranked.top(payload(), 2)] == ["aaa111", "bbb222"]


def test_top_caps_the_count():
    assert len(ranked.top(payload(), 1)) == 1


def test_top_skips_excluded_ids_however_high_they_score():
    out = ranked.top(payload(), 2, exclude_ids=frozenset({"aaa111"}))
    assert [i["id"] for i in out] == ["bbb222"]


def test_unpublishable_ids_selects_only_discussions():
    article = make_item(
        url="https://x/a", title="A", source="hn", meta={"kind": "article"}
    )
    thread = make_item(
        url="https://news.ycombinator.com/item?id=1",
        title="Ask HN: something",
        source="hn",
        meta={"kind": "discussion"},
    )
    # Sources other than HN set no "kind" at all; absence must not exclude them.
    paper = make_item(url="https://arxiv.org/abs/2509.1", title="P", source="arxiv")
    assert ranked.unpublishable_ids([article, thread, paper]) == frozenset({thread.id})

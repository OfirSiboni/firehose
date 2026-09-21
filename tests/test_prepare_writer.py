from agents import prepare_writer


def payload():
    return {
        "generated_at": "2026-09-21T07:00:00Z",
        "pool_size": 3,
        "read_count": 2,
        "items": [
            {"id": "a", "url": "https://x/a", "title": "A", "source": "hn",
             "tier": "headline", "score": 9.0, "saturation": 0.9, "reason": "r",
             "read": True, "key_facts": ["fact a"], "dedupe_of": None},
            {"id": "b", "url": "https://x/b", "title": "B", "source": "arxiv",
             "tier": "discovery", "score": 7.0, "saturation": 0.1, "reason": "r",
             "read": True, "key_facts": ["fact b"], "dedupe_of": None},
            {"id": "c", "url": "https://x/c", "title": "C", "source": "blog",
             "tier": "discovery", "score": 2.0, "saturation": 0.4, "reason": "r",
             "read": False, "key_facts": [], "dedupe_of": None},
        ],
    }


def test_build_takes_the_top_n_by_score():
    out = prepare_writer.build(payload(), n=2)
    assert [i["id"] for i in out["stories"]] == ["a", "b"]


def test_build_carries_key_facts_through():
    out = prepare_writer.build(payload(), n=2)
    assert out["stories"][0]["key_facts"] == ["fact a"]


def test_build_drops_scoring_internals():
    out = prepare_writer.build(payload(), n=1)
    assert "saturation" not in out["stories"][0]
    assert "score" not in out["stories"][0]


def test_build_sets_the_date():
    out = prepare_writer.build(payload(), n=1)
    assert len(out["date"]) == 10


def test_build_never_hands_the_writer_an_excluded_story():
    out = prepare_writer.build(payload(), n=2, exclude_ids=frozenset({"a"}))
    assert [i["id"] for i in out["stories"]] == ["b", "c"]

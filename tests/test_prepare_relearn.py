from agents import prepare_relearn

ROWS = [
    {"item_id": "a", "verdict": "up", "source": "arxiv", "tier": "discovery", "title": "A"},
    {"item_id": "b", "verdict": "published", "source": "github", "tier": "discovery", "title": "B"},
    {"item_id": "c", "verdict": "down", "source": "blog", "tier": "headline", "title": "C"},
    {"item_id": "d", "verdict": "ignored", "source": "arxiv", "tier": "discovery", "title": "D"},
]


def test_counts_each_verdict():
    out = prepare_relearn.summarize(ROWS)
    assert out["counts"] == {"up": 1, "published": 1, "down": 1, "ignored": 1}


def test_groups_accepted_and_rejected_titles():
    out = prepare_relearn.summarize(ROWS)
    assert out["accepted"] == ["A", "B"]
    assert out["rejected"] == ["C", "D"]


def test_breaks_verdicts_down_by_source():
    out = prepare_relearn.summarize(ROWS)
    assert out["by_source"]["arxiv"] == {"up": 1, "ignored": 1}
    assert out["by_source"]["github"] == {"published": 1}


def test_handles_an_empty_label_set():
    out = prepare_relearn.summarize([])
    assert out["counts"] == {}
    assert out["accepted"] == []

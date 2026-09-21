from store import health


def test_dead_sources_needs_three_consecutive_zero_runs(tmp_path, monkeypatch):
    monkeypatch.setattr(health, "HEALTH_PATH", tmp_path / "health.json")
    health.record({"hn": 10, "arxiv": 0})
    health.record({"hn": 10, "arxiv": 0})
    assert health.dead_sources(3) == []
    health.record({"hn": 10, "arxiv": 0})
    assert health.dead_sources(3) == ["arxiv"]


def test_a_single_good_run_clears_a_source(tmp_path, monkeypatch):
    monkeypatch.setattr(health, "HEALTH_PATH", tmp_path / "health.json")
    for _ in range(3):
        health.record({"arxiv": 0})
    health.record({"arxiv": 5})
    assert health.dead_sources(3) == []


def test_dead_sources_is_empty_with_no_history(tmp_path, monkeypatch):
    monkeypatch.setattr(health, "HEALTH_PATH", tmp_path / "health.json")
    assert health.dead_sources() == []


def test_record_keeps_only_the_last_n_runs(tmp_path, monkeypatch):
    monkeypatch.setattr(health, "HEALTH_PATH", tmp_path / "health.json")
    for i in range(12):
        health.record({"hn": i}, keep=8)
    import json
    assert len(json.loads((tmp_path / "health.json").read_text(encoding="utf-8"))) == 8

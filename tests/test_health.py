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


def test_records_failed_units_alongside_the_item_count(tmp_path, monkeypatch):
    import json

    monkeypatch.setattr(health, "HEALTH_PATH", tmp_path / "health.json")
    health.record({"github": {"items": 12, "failed": 4}})
    stored = json.loads((tmp_path / "health.json").read_text(encoding="utf-8"))
    assert stored == [{"github": {"items": 12, "failed": 4}}]


def test_dead_sources_reads_the_richer_shape(tmp_path, monkeypatch):
    monkeypatch.setattr(health, "HEALTH_PATH", tmp_path / "health.json")
    for _ in range(3):
        health.record({"hn": {"items": 10, "failed": 0}, "blog": {"items": 0, "failed": 6}})
    assert health.dead_sources(3) == ["blog"]


def test_dead_sources_reads_a_legacy_entry_without_crashing(tmp_path, monkeypatch):
    # The committed history predates failure counts; the first run after this
    # change must not choke on its own file.
    monkeypatch.setattr(health, "HEALTH_PATH", tmp_path / "health.json")
    health.record({"hn": 53, "arxiv": 0})
    health.record({"hn": {"items": 51, "failed": 0}, "arxiv": {"items": 0, "failed": 1}})
    health.record({"hn": {"items": 49, "failed": 0}, "arxiv": {"items": 0, "failed": 1}})
    assert health.dead_sources(3) == ["arxiv"]

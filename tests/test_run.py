from ingest import run
from store.item import make_item


def _one(name: str, failed: int = 0):
    def fetch():
        item = make_item(
            url=f"https://example.com/{name}", title=name.upper(), source=name
        )
        return [item], failed

    return fetch


def _boom():
    raise RuntimeError("upstream exploded")


def test_a_raising_source_does_not_lose_the_others(monkeypatch):
    monkeypatch.setattr(run, "SOURCES", {"a": _one("a"), "boom": _boom, "b": _one("b")})
    items, counts = run.collect()
    assert counts == {
        "a": {"items": 1, "failed": 0},
        "boom": {"items": 0, "failed": 1},
        "b": {"items": 1, "failed": 0},
    }
    assert sorted(i.title for i in items) == ["A", "B"]


def test_collect_does_not_raise_when_every_source_fails(monkeypatch):
    monkeypatch.setattr(run, "SOURCES", {"x": _boom, "y": _boom})
    items, counts = run.collect()
    assert items == []
    assert counts == {"x": {"items": 0, "failed": 1}, "y": {"items": 0, "failed": 1}}


def test_collect_reports_which_source_failed(monkeypatch, capsys):
    monkeypatch.setattr(run, "SOURCES", {"boom": _boom})
    run.collect()
    assert "upstream exploded" in capsys.readouterr().err


def test_partial_failure_inside_a_source_is_counted(monkeypatch):
    # Four of five GitHub topics dying still returns items; without the count
    # that run is indistinguishable from a healthy one.
    monkeypatch.setattr(run, "SOURCES", {"github": _one("github", failed=4)})
    _items, counts = run.collect()
    assert counts == {"github": {"items": 1, "failed": 4}}


def test_partial_failure_is_reported_on_stdout(monkeypatch, capsys):
    monkeypatch.setattr(run, "SOURCES", {"github": _one("github", failed=4)})
    run.collect()
    assert "4 unit(s) failed" in capsys.readouterr().out


def test_the_blog_source_is_keyed_the_way_items_are_labelled():
    # dead_sources() names come from here; pool rows say "blog".
    assert "blog" in run.SOURCES and "blogs" not in run.SOURCES


def test_collect_feedback_handles_append_labels_failure(monkeypatch):
    """Feedback failures must not abort ingest before pool.save_pool(kept)."""
    def mock_get_updates(token: str, offset: int, allowed=None):
        return [{"update_id": 1, "message_reaction": {"message_id": 10, "new_reaction": []}}]

    def mock_append_labels_raises(rows):
        raise RuntimeError("database write failed")

    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "test-token")
    monkeypatch.setattr(run, "get_updates", mock_get_updates)
    monkeypatch.setattr(run.labels, "append_labels", mock_append_labels_raises)

    # Should return 0 and not raise, even though append_labels fails
    result = run.collect_feedback()
    assert result == 0

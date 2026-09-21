from ingest import run
from store.item import make_item


def _one(name: str):
    def fetch():
        return [make_item(url=f"https://example.com/{name}", title=name.upper(), source=name)]
    return fetch


def _boom():
    raise RuntimeError("upstream exploded")


def test_a_raising_source_does_not_lose_the_others(monkeypatch):
    monkeypatch.setattr(run, "SOURCES", {"a": _one("a"), "boom": _boom, "b": _one("b")})
    items, counts = run.collect()
    assert counts == {"a": 1, "boom": 0, "b": 1}
    assert sorted(i.title for i in items) == ["A", "B"]


def test_collect_does_not_raise_when_every_source_fails(monkeypatch):
    monkeypatch.setattr(run, "SOURCES", {"x": _boom, "y": _boom})
    items, counts = run.collect()
    assert items == []
    assert counts == {"x": 0, "y": 0}


def test_collect_reports_which_source_failed(monkeypatch, capsys):
    monkeypatch.setattr(run, "SOURCES", {"boom": _boom})
    run.collect()
    assert "upstream exploded" in capsys.readouterr().err

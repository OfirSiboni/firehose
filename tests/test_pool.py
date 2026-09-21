import json
from datetime import datetime, timezone

import pytest

from store import pool
from store.item import make_item


def at(day: int, hour: int = 12) -> str:
    return f"2026-09-{day:02d}T{hour:02d}:00:00Z"


NOW = datetime(2026, 9, 21, 12, 0, 0, tzinfo=timezone.utc)


def test_save_and_load_round_trip(tmp_path):
    path = tmp_path / "pool.jsonl"
    items = [make_item(url="https://example.com/a", title="A", source="hn", now=at(21))]
    pool.save_pool(items, path)
    assert pool.load_pool(path) == items


def test_load_returns_empty_when_file_is_absent(tmp_path):
    assert pool.load_pool(tmp_path / "nope.jsonl") == []


def test_merge_adds_only_new_items():
    existing = [make_item(url="https://example.com/a", title="A", source="hn", now=at(20))]
    incoming = [
        make_item(url="https://example.com/a", title="A again", source="hn", now=at(21)),
        make_item(url="https://example.com/b", title="B", source="hn", now=at(21)),
    ]
    merged, new_count = pool.merge(existing, incoming)
    assert new_count == 1
    assert len(merged) == 2


def test_merge_keeps_the_original_first_seen():
    existing = [make_item(url="https://example.com/a", title="A", source="hn", now=at(20))]
    incoming = [make_item(url="https://example.com/a", title="A", source="hn", now=at(21))]
    merged, _ = pool.merge(existing, incoming)
    assert merged[0].first_seen == at(20)


def test_expire_drops_items_older_than_the_window():
    items = [
        make_item(url="https://example.com/old", title="Old", source="hn", now=at(10)),
        make_item(url="https://example.com/new", title="New", source="hn", now=at(20)),
    ]
    kept = pool.expire(items, now=NOW, days=7)
    assert [i.title for i in kept] == ["New"]


def test_unsent_since_filters_by_age_and_sent_flag():
    fresh = make_item(url="https://example.com/fresh", title="Fresh", source="hn", now=at(21, 0))
    stale = make_item(url="https://example.com/stale", title="Stale", source="hn", now=at(18))
    already = make_item(url="https://example.com/sent", title="Sent", source="hn", now=at(21, 0))
    already.sent_in = "2026-09-21"
    out = pool.unsent_since([fresh, stale, already], hours=36, now=NOW)
    assert [i.title for i in out] == ["Fresh"]


def test_mark_sent_stamps_only_the_named_ids():
    a = make_item(url="https://example.com/a", title="A", source="hn", now=at(21))
    b = make_item(url="https://example.com/b", title="B", source="hn", now=at(21))
    out = pool.mark_sent([a, b], [a.id], "2026-09-21")
    assert out[0].sent_in == "2026-09-21"
    assert out[1].sent_in is None


def test_merge_refreshes_volatile_meta_on_a_known_id():
    # The Judge reads saturation straight off points: a story frozen at its
    # first-sight count is mis-tiered as a discovery forever.
    existing = [
        make_item(
            url="https://example.com/a",
            title="A",
            source="hn",
            meta={"points": 45, "comments": 3},
            now=at(20),
        )
    ]
    incoming = [
        make_item(
            url="https://example.com/a",
            title="A, retitled upstream",
            source="hn",
            meta={"points": 2000, "comments": 410},
            now=at(21),
        )
    ]
    merged, new_count = pool.merge(existing, incoming)
    assert new_count == 0
    assert merged[0].meta["points"] == 2000
    assert merged[0].meta["comments"] == 410
    assert merged[0].title == "A, retitled upstream"


def test_merge_refreshing_does_not_move_first_seen():
    existing = [
        make_item(url="https://example.com/a", title="A", source="hn",
                  meta={"points": 45}, now=at(20))
    ]
    incoming = [
        make_item(url="https://example.com/a", title="A", source="hn",
                  meta={"points": 2000}, now=at(21))
    ]
    merged, _ = pool.merge(existing, incoming)
    assert merged[0].first_seen == at(20)


def test_merge_does_not_unsend_an_already_sent_item():
    existing = [make_item(url="https://example.com/a", title="A", source="hn", now=at(20))]
    existing[0].sent_in = "2026-09-20"
    incoming = [make_item(url="https://example.com/a", title="A", source="hn", now=at(21))]
    merged, _ = pool.merge(existing, incoming)
    assert merged[0].sent_in == "2026-09-20"
    assert merged[0].id == existing[0].id


def test_merge_keeps_the_longer_text_and_unions_meta():
    existing = [
        make_item(url="https://example.com/a", title="A", source="hn",
                  meta={"kind": "article"}, now=at(20))
    ]
    incoming = [
        make_item(url="https://example.com/a", title="A", source="blog",
                  text="The excerpt.", meta={"feed": "example.com"}, now=at(21))
    ]
    merged, _ = pool.merge(existing, incoming)
    assert merged[0].text == "The excerpt."
    assert merged[0].meta == {"kind": "article", "feed": "example.com"}


def test_load_skips_a_bad_row_without_losing_the_file(tmp_path, capsys):
    path = tmp_path / "pool.jsonl"
    good = make_item(url="https://example.com/a", title="A", source="hn", now=at(21))
    path.write_text(
        json.dumps(good.to_dict()) + "\nnot json at all\n" + json.dumps({"id": "x"}) + "\n",
        encoding="utf-8",
    )
    loaded = pool.load_pool(path)
    assert [i.title for i in loaded] == ["A"]
    assert "skipped bad row" in capsys.readouterr().err


def test_load_tolerates_a_row_with_an_unknown_field(tmp_path):
    path = tmp_path / "pool.jsonl"
    row = make_item(url="https://example.com/a", title="A", source="hn", now=at(21)).to_dict()
    row["added_by_a_later_version"] = True
    path.write_text(json.dumps(row) + "\n", encoding="utf-8")
    assert [i.title for i in pool.load_pool(path)] == ["A"]


def test_save_leaves_the_old_pool_intact_when_the_write_fails(tmp_path, monkeypatch):
    path = tmp_path / "pool.jsonl"
    first = [make_item(url="https://example.com/a", title="A", source="hn", now=at(21))]
    pool.save_pool(first, path)

    def boom(src, dst):
        raise OSError("interrupted")

    monkeypatch.setattr(pool.os, "replace", boom)
    with pytest.raises(OSError):
        pool.save_pool(
            [make_item(url="https://example.com/b", title="B", source="hn", now=at(21))],
            path,
        )
    assert [i.title for i in pool.load_pool(path)] == ["A"]
    assert list(tmp_path.glob("*.tmp")) == []

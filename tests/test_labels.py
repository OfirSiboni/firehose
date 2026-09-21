from store import labels

DIGEST = {
    "date": "2026-09-21",
    "sent": True,
    "items": [
        {"id": "aaa111", "title": "A", "url": "https://x/a", "source": "hn",
         "tier": "headline", "summary": "", "message_id": 10},
        {"id": "bbb222", "title": "B", "url": "https://x/b", "source": "arxiv",
         "tier": "discovery", "summary": "", "message_id": 11},
    ],
}


def update(message_id: int, emoji: str) -> dict:
    return {
        "update_id": 500,
        "message_reaction": {
            "message_id": message_id,
            "date": 1758440000,
            "new_reaction": [{"type": "emoji", "emoji": emoji}],
        },
    }


def test_build_message_index_maps_message_id_to_item():
    index = labels.build_message_index([DIGEST])
    assert index[10]["id"] == "aaa111"
    assert index[11]["digest_date"] == "2026-09-21"


def test_thumbs_up_becomes_an_up_verdict():
    rows = labels.reactions_to_labels([update(10, "👍")], labels.build_message_index([DIGEST]))
    assert len(rows) == 1
    assert rows[0]["verdict"] == "up"
    assert rows[0]["item_id"] == "aaa111"
    assert rows[0]["tier"] == "headline"


def test_thumbs_down_becomes_a_down_verdict():
    rows = labels.reactions_to_labels([update(11, "👎")], labels.build_message_index([DIGEST]))
    assert rows[0]["verdict"] == "down"


def test_writing_hand_becomes_a_published_verdict():
    rows = labels.reactions_to_labels([update(10, "✍")], labels.build_message_index([DIGEST]))
    assert rows[0]["verdict"] == "published"


def test_unknown_emoji_is_ignored():
    rows = labels.reactions_to_labels([update(10, "🎉")], labels.build_message_index([DIGEST]))
    assert rows == []


def test_reaction_on_an_unknown_message_is_ignored():
    rows = labels.reactions_to_labels([update(999, "👍")], labels.build_message_index([DIGEST]))
    assert rows == []


def test_cleared_reaction_produces_no_row():
    cleared = {"update_id": 501, "message_reaction": {"message_id": 10, "new_reaction": []}}
    rows = labels.reactions_to_labels([cleared], labels.build_message_index([DIGEST]))
    assert rows == []


def test_mark_ignored_covers_items_with_no_existing_label(tmp_path, monkeypatch):
    monkeypatch.setattr(labels, "LABELS_PATH", tmp_path / "labels.jsonl")
    labels.append_labels([{"item_id": "aaa111", "verdict": "up", "digest_date": "2026-09-21"}])
    rows = labels.mark_ignored(DIGEST)
    assert [r["item_id"] for r in rows] == ["bbb222"]
    assert rows[0]["verdict"] == "ignored"


def test_append_and_load_round_trip(tmp_path, monkeypatch):
    monkeypatch.setattr(labels, "LABELS_PATH", tmp_path / "labels.jsonl")
    labels.append_labels([{"item_id": "x", "verdict": "up"}])
    labels.append_labels([{"item_id": "y", "verdict": "down"}])
    assert [r["item_id"] for r in labels.load_labels()] == ["x", "y"]


def test_recent_labels_returns_the_tail(tmp_path, monkeypatch):
    monkeypatch.setattr(labels, "LABELS_PATH", tmp_path / "labels.jsonl")
    labels.append_labels([{"item_id": str(i), "verdict": "up"} for i in range(30)])
    assert len(labels.recent_labels(20)) == 20
    assert labels.recent_labels(20)[-1]["item_id"] == "29"

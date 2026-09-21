from store import digests


def test_save_and_load_round_trip(tmp_path, monkeypatch):
    monkeypatch.setattr(digests, "DIGEST_DIR", tmp_path)
    payload = {
        "date": "2026-09-21",
        "sent": True,
        "items": [
            {
                "id": "a3f9c21b4e07",
                "title": "T",
                "url": "https://example.com/a",
                "source": "hn",
                "tier": "headline",
                "summary": "S",
                "message_id": 42,
            }
        ],
    }
    digests.save_digest(payload, "2026-09-21")
    assert digests.load_digest("2026-09-21") == payload


def test_load_returns_none_when_absent(tmp_path, monkeypatch):
    monkeypatch.setattr(digests, "DIGEST_DIR", tmp_path)
    assert digests.load_digest("2026-01-01") is None


def test_recent_digests_are_newest_first(tmp_path, monkeypatch):
    monkeypatch.setattr(digests, "DIGEST_DIR", tmp_path)
    for date in ["2026-09-19", "2026-09-20", "2026-09-21"]:
        digests.save_digest({"date": date, "sent": True, "items": []}, date)
    assert [d["date"] for d in digests.recent_digests(2)] == ["2026-09-21", "2026-09-20"]

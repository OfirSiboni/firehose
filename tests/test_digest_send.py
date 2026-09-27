"""Contract tests for send.digest: HTML escaping and the sent-digest no-op path."""

from __future__ import annotations

import send.digest as digest_module
from store import digests


def test_render_escapes_html_in_title():
    item = {
        "title": "<script>alert(1)</script>",
        "tier": "headline",
        "source": "hn",
        "url": "https://example.com",
        "reason": "why this matters",
    }
    rendered = digest_module.render(item)
    assert "<script>" not in rendered
    assert "&lt;script&gt;" in rendered


def test_main_sends_nothing_when_newest_digest_already_sent(monkeypatch, tmp_path):
    monkeypatch.setattr(digests, "DIGEST_DIR", tmp_path)
    digests.save_digest({"date": "2026-09-21", "sent": True, "items": []}, "2026-09-21")

    def fail_if_called(*args, **kwargs):
        raise AssertionError("send_message must not be called for an already-sent digest")

    monkeypatch.setattr(digest_module, "send_message", fail_if_called)
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "token")
    monkeypatch.setenv("TELEGRAM_CHAT_ID", "chat")

    assert digest_module.main() == 0


def _sent_texts(monkeypatch, tmp_path, critique_dir):
    """Run main() against a one-item digest, collecting the Telegram calls."""
    from store import critique, health, pool, ranked

    monkeypatch.setattr(digests, "DIGEST_DIR", tmp_path / "digests")
    monkeypatch.setattr(critique, "CRITIQUE_DIR", critique_dir)
    monkeypatch.setattr(pool, "load_pool", lambda: [])
    monkeypatch.setattr(pool, "save_pool", lambda items: None)
    monkeypatch.setattr(pool, "mark_sent", lambda items, ids, date: items)
    monkeypatch.setattr(ranked, "load_ranked", lambda ids: (_ for _ in ()).throw(OSError))
    monkeypatch.setattr(health, "dead_sources", lambda days: [])
    digests.save_digest(
        {
            "date": "2026-09-22",
            "sent": False,
            "items": [
                {
                    "id": "a",
                    "title": "T",
                    "url": "https://x/a",
                    "source": "hn",
                    "tier": "headline",
                    "summary": "s",
                }
            ],
        },
        "2026-09-22",
    )

    texts = []

    def record(text, token, chat_id):
        texts.append(text)
        return len(texts)

    monkeypatch.setattr(digest_module, "send_message", record)
    monkeypatch.setattr(digest_module.time, "sleep", lambda s: None)
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "token")
    monkeypatch.setenv("TELEGRAM_CHAT_ID", "chat")
    assert digest_module.main() == 0
    return texts


def test_main_appends_the_blind_verdict_when_one_exists(monkeypatch, tmp_path):
    from store import critique

    monkeypatch.setattr(critique, "CRITIQUE_DIR", tmp_path / "critique")
    critique.save_critique(
        {"date": "2026-09-22", "winner": "Firehose", "verdict": "ours read tighter"},
        "2026-09-22",
    )
    texts = _sent_texts(monkeypatch, tmp_path, tmp_path / "critique")
    assert "Blind verdict" in texts[-1]
    assert "ours read tighter" in texts[-1]


def test_main_sends_no_verdict_when_there_is_none(monkeypatch, tmp_path):
    texts = _sent_texts(monkeypatch, tmp_path, tmp_path / "critique")
    assert not any("Blind verdict" in t for t in texts)

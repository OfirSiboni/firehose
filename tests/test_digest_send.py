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

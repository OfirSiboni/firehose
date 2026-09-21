"""Telegram Bot API. stdlib only."""

from __future__ import annotations

import json
import urllib.parse
import urllib.request

BASE = "https://api.telegram.org/bot{token}/{method}"


def api(method: str, token: str, params: dict) -> dict:
    url = BASE.format(token=token, method=method)
    data = urllib.parse.urlencode(
        {k: (json.dumps(v) if isinstance(v, (list, dict)) else v)
         for k, v in params.items()}
    ).encode("utf-8")
    with urllib.request.urlopen(urllib.request.Request(url, data=data), timeout=30) as r:
        payload = json.loads(r.read().decode("utf-8"))
    if not payload.get("ok"):
        raise RuntimeError(f"telegram {method} failed: {payload}")
    return payload["result"]


def send_message(text: str, token: str, chat_id: str) -> int:
    result = api(
        "sendMessage",
        token,
        {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": "true",
        },
    )
    return result["message_id"]


def get_updates(token: str, offset: int, allowed: list[str] | None = None) -> list[dict]:
    """Drain pending updates. Reactions require message_reaction in allowed_updates."""
    return api(
        "getUpdates",
        token,
        {
            "offset": offset,
            "timeout": 0,
            "allowed_updates": allowed or ["message_reaction"],
        },
    )

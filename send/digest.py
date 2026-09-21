"""Send the newest digest to Telegram. Idempotent: a re-run after `sent: true` is a no-op."""

from __future__ import annotations

import html
import os
import time

from send.telegram import send_message
from store import digests, health, pool, ranked

TIER_LABEL = {"headline": "📰", "discovery": "🔍"}


def render(item: dict) -> str:
    # Judge items carry `reason`; Writer-drafted items carry `summary` and no
    # `reason`. Both shapes flow through here, so neither key is assumed.
    icon = TIER_LABEL.get(item["tier"], "•")
    body = item.get("summary") or item.get("reason", "")
    return (
        f"{icon} <b>{html.escape(item['title'])}</b>\n"
        f"{html.escape(body)}\n"
        f"{html.escape(item['source'])} · <a href=\"{html.escape(item['url'])}\">link</a>"
    )


def main() -> int:
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    recent = digests.recent_digests(1)
    digest = recent[0] if recent else None
    if digest is None:
        print("no digest to send")
        return 0
    if digest.get("sent"):
        print(f"{digest['date']} already sent; nothing to do")
        return 0

    date = digest["date"]
    selected = digest.get("items", [])
    if not selected:
        print("digest has no items; sending nothing")
        return 0

    items = pool.load_pool()
    header = f"<b>Firehose — {date}</b>\n{len(selected)} stories"
    try:
        payload = ranked.load_ranked({i.id for i in items})
        header += (
            f" · {payload['pool_size']} candidates · "
            f"{payload['read_count']} read in full"
        )
    except Exception:
        pass  # the header must not block sending
    dead = health.dead_sources(3)
    if dead:
        header += f"\n⚠️ no items from: {', '.join(dead)}"
    send_message(header, token, chat_id)

    records = []
    for item in selected:
        message_id = send_message(render(item), token, chat_id)
        records.append({**item, "message_id": message_id})
        time.sleep(0.5)

    digests.save_digest({**digest, "sent": True, "items": records}, date)
    pool.save_pool(pool.mark_sent(items, [r["id"] for r in records], date))
    print(f"sent {len(records)} items")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

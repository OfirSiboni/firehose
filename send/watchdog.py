"""The only failure detector for the judgment half: a dead routine holds no
Telegram token and can't report its own failure, so this runs on a clock instead."""

from __future__ import annotations

import os
from datetime import datetime, timezone

from send.telegram import send_message
from store import digests


def main() -> int:
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if digests.load_digest(date) is None:
        token = os.environ["TELEGRAM_BOT_TOKEN"]
        chat_id = os.environ["TELEGRAM_CHAT_ID"]
        send_message(
            "⚠️ <b>no digest today</b>\n"
            f"The curator routine did not commit data/digests/{date}.json.",
            token,
            chat_id,
        )
        return 0
    print("ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

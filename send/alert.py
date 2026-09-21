"""Posted by the workflow's failure branch, so a dead job is visible."""

from __future__ import annotations

import os

from send.telegram import send_message


def main() -> int:
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    run_url = os.environ.get("RUN_URL", "(no run url)")
    text = os.environ.get(
        "ALERT_TEXT",
        f"⚠️ <b>digest failed</b>\nNo digest today.\n<a href=\"{run_url}\">run log</a>",
    )
    send_message(text, token, chat_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Minimal HTTP helpers. stdlib only, one retry, always a User-Agent."""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request

UA = "tldrcreator/1.0 (+https://github.com/tldrcreator)"


def _get(url: str, timeout: int, accept: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
    last: Exception | None = None
    for attempt in range(2):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read()
        except (urllib.error.URLError, TimeoutError) as exc:
            last = exc
            if attempt == 0:
                time.sleep(2)
    raise RuntimeError(f"GET failed: {url}") from last


def get_json(url: str, timeout: int = 20) -> dict:
    return json.loads(_get(url, timeout, "application/json").decode("utf-8"))


def get_text(url: str, timeout: int = 20) -> str:
    return _get(url, timeout, "*/*").decode("utf-8", errors="replace")

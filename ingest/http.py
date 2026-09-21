"""Minimal HTTP helpers. stdlib only, one retry, always a User-Agent."""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request

UA = "tldrcreator/1.0 (+https://github.com/tldrcreator)"

# A hostile or broken feed must not be able to exhaust the runner's memory.
MAX_BYTES = 16 * 1024 * 1024


def _get(url: str, timeout: int, accept: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
    last: Exception | None = None
    for attempt in range(2):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                body = response.read(MAX_BYTES + 1)
                if len(body) > MAX_BYTES:
                    raise RuntimeError(f"GET too large (>{MAX_BYTES} bytes): {url}")
                return body
        except urllib.error.HTTPError as exc:
            # HTTPError subclasses URLError, so it has to be caught first. A
            # 4xx other than 429 means the request itself is wrong: retrying
            # it just doubles the latency of a diagnosis (an arXiv 406 cost
            # two sessions). Rate limits and 5xx are worth a second attempt.
            if 400 <= exc.code < 500 and exc.code != 429:
                raise RuntimeError(f"GET failed: {url}: {exc}") from exc
            last = exc
            if attempt == 0:
                time.sleep(2)
        except (urllib.error.URLError, TimeoutError) as exc:
            last = exc
            if attempt == 0:
                time.sleep(2)
    # The status code or socket error is the whole diagnosis; keep it in the
    # message, because that is all the ingest log will show.
    raise RuntimeError(f"GET failed: {url}: {last}") from last


def get_json(url: str, timeout: int = 20) -> dict:
    return json.loads(_get(url, timeout, "application/json").decode("utf-8"))


def get_text(url: str, timeout: int = 20) -> str:
    return _get(url, timeout, "*/*").decode("utf-8", errors="replace")

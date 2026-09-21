import urllib.error

import pytest

from ingest import http


class _Response:
    def __init__(self, body: bytes):
        self.body = body

    def read(self, amount: int | None = None) -> bytes:
        return self.body if amount is None else self.body[:amount]

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def _patch(monkeypatch, outcomes):
    """Serve `outcomes` in order; each is bytes to return or an exc to raise."""
    calls = []

    def fake_urlopen(request, timeout=None):
        outcome = outcomes[min(len(calls), len(outcomes) - 1)]
        calls.append(request.full_url)
        if isinstance(outcome, Exception):
            raise outcome
        return _Response(outcome)

    monkeypatch.setattr(http.urllib.request, "urlopen", fake_urlopen)
    monkeypatch.setattr(http.time, "sleep", lambda _seconds: None)
    return calls


def _http_error(code: int) -> urllib.error.HTTPError:
    return urllib.error.HTTPError("https://x.test/a", code, "Nope", None, None)


def test_returns_the_body(monkeypatch):
    _patch(monkeypatch, [b'{"a": 1}'])
    assert http.get_json("https://x.test/a") == {"a": 1}


def test_a_4xx_is_not_retried(monkeypatch):
    calls = _patch(monkeypatch, [_http_error(406)])
    with pytest.raises(RuntimeError):
        http.get_text("https://x.test/a")
    assert len(calls) == 1


def test_a_429_is_retried(monkeypatch):
    calls = _patch(monkeypatch, [_http_error(429)])
    with pytest.raises(RuntimeError):
        http.get_text("https://x.test/a")
    assert len(calls) == 2


def test_a_5xx_is_retried(monkeypatch):
    calls = _patch(monkeypatch, [_http_error(503)])
    with pytest.raises(RuntimeError):
        http.get_text("https://x.test/a")
    assert len(calls) == 2


def test_a_transient_failure_succeeds_on_the_second_try(monkeypatch):
    _patch(monkeypatch, [urllib.error.URLError("reset"), b"ok"])
    assert http.get_text("https://x.test/a") == "ok"


def test_the_failure_message_names_the_status(monkeypatch):
    _patch(monkeypatch, [_http_error(406)])
    with pytest.raises(RuntimeError, match="406"):
        http.get_text("https://x.test/a")


def test_the_failure_message_names_the_underlying_error(monkeypatch):
    _patch(monkeypatch, [urllib.error.URLError("connection reset")])
    with pytest.raises(RuntimeError, match="connection reset"):
        http.get_text("https://x.test/a")


def test_an_oversized_response_is_refused(monkeypatch):
    monkeypatch.setattr(http, "MAX_BYTES", 32)
    _patch(monkeypatch, [b"x" * 64])
    with pytest.raises(RuntimeError, match="too large"):
        http.get_text("https://x.test/a")


def test_a_response_at_the_cap_is_allowed(monkeypatch):
    monkeypatch.setattr(http, "MAX_BYTES", 32)
    _patch(monkeypatch, [b"x" * 32])
    assert http.get_text("https://x.test/a") == "x" * 32

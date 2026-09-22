from pathlib import Path

from ingest import tldr

SAMPLE = (Path(__file__).parent / "fixtures" / "tldr_sample.html").read_text(encoding="utf-8")


def stories():
    return tldr.parse(SAMPLE)


def test_parse_reads_article_blocks():
    titles = [s["title"] for s in stories()]
    assert "Xiaomi Ships MiMo v2.6" in titles
    assert "How KV-Cache Eviction Actually Works" in titles


def test_parse_also_reads_unwrapped_headlines():
    titles = [s["title"] for s in stories()]
    assert "A 12-Chapter Book on AI Infrastructure" in titles


def test_parse_drops_sponsors():
    assert not any("Acme" in s["title"] for s in stories())


def test_parse_drops_items_with_no_body():
    assert not any(s["title"] == "Empty Blurb" for s in stories())


def test_parse_strips_reading_time_from_titles():
    assert not any("minute read" in s["title"] for s in stories())


def test_parse_keeps_summaries_as_plain_text():
    story = next(s for s in stories() if s["title"] == "Xiaomi Ships MiMo v2.6")
    assert "SWE-bench Verified" in story["summary"]
    assert "<" not in story["summary"]


def test_parse_ignores_the_footer():
    assert not any("subscription" in s["summary"] for s in stories())


def test_parse_of_a_missing_issue_is_empty():
    assert tldr.parse("<html><body><h1>Not found</h1></body></html>") == []

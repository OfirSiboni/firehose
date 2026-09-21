from pathlib import Path

from ingest.sources import arxiv

FIXTURE = Path(__file__).parent / "fixtures" / "arxiv_sample.xml"


def load():
    return arxiv.parse(FIXTURE.read_text(encoding="utf-8"))


def test_parses_every_entry():
    assert len(load()) == 2


def test_collapses_versioned_url_to_abs():
    assert load()[0].normalized_url == "https://arxiv.org/abs/2509.12345"


def test_sets_source_and_title():
    first = load()[0]
    assert first.source == "arxiv"
    assert first.title == "Cache Eviction Policies for Long-Context Inference"


def test_abstract_is_whitespace_collapsed_into_text():
    assert load()[0].text == (
        "We introduce a KV-cache eviction policy that achieves 3.1x "
        "throughput at equal quality."
    )


def test_authors_and_category_land_in_meta():
    first = load()[0]
    assert first.meta["authors"] == ["Jane Doe", "Wei Zhang"]
    assert first.meta["primary_category"] == "cs.LG"
    assert first.meta["published"] == "2026-09-20T17:21:03Z"

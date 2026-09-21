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


def test_skips_entries_with_no_link_or_id():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry><title>No link anywhere</title><summary>Body.</summary></entry>
</feed>"""
    assert arxiv.parse(xml) == []


def test_skips_entries_with_no_title():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry><id>http://arxiv.org/abs/2509.00001v1</id><summary>Body.</summary></entry>
</feed>"""
    assert arxiv.parse(xml) == []


def test_one_malformed_entry_does_not_lose_the_others():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry><id>http://arxiv.org/abs/2509.00001v1</id><title>Good one</title><summary>A.</summary></entry>
  <entry><title>Broken, no link or id</title><summary>B.</summary></entry>
  <entry><id>http://arxiv.org/abs/2509.00003v1</id><title>Also good</title><summary>C.</summary></entry>
</feed>"""
    assert [i.title for i in arxiv.parse(xml)] == ["Good one", "Also good"]

import json
from pathlib import Path

from ingest.sources import hn

FIXTURE = Path(__file__).parent / "fixtures" / "hn_sample.json"


def load():
    return hn.parse(json.loads(FIXTURE.read_text(encoding="utf-8")))


def test_parses_every_hit():
    assert len(load()) == 3


def test_sets_source_and_title():
    first = load()[0]
    assert first.source == "hn"
    assert first.title == "Llama 4 released with 10M context"


def test_normalizes_the_target_url():
    first = load()[0]
    assert first.normalized_url == "https://ai.meta.com/blog/llama-4"


def test_carries_points_and_comments_into_meta():
    first = load()[0]
    assert first.meta["points"] == 842
    assert first.meta["comments"] == 310
    assert first.meta["hn_url"] == "https://news.ycombinator.com/item?id=41000001"


def test_text_post_falls_back_to_the_hn_permalink():
    ask_hn = load()[2]
    assert ask_hn.url == "https://news.ycombinator.com/item?id=41000003"


def test_story_text_is_cleaned_of_html():
    ask_hn = load()[2]
    assert ask_hn.text == "I'm curious what people actually keep loaded. Especially on 24GB cards."


def test_link_submissions_are_tagged_as_articles():
    assert load()[0].meta["kind"] == "article"


def test_text_posts_are_tagged_as_discussions():
    assert load()[2].meta["kind"] == "discussion"


def test_skips_hits_with_no_title():
    items = hn.parse({"hits": [{"objectID": "1", "title": None, "url": "https://x.com/a"}]})
    assert items == []

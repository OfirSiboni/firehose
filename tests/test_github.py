import json
from pathlib import Path

from ingest.sources import github

FIXTURE = Path(__file__).parent / "fixtures" / "github_sample.json"


def load():
    return github.parse(json.loads(FIXTURE.read_text(encoding="utf-8")))


def test_parses_every_repo():
    assert len(load()) == 2


def test_title_is_the_full_name():
    assert load()[0].title == "vllm-project/flashserve"


def test_description_becomes_text():
    assert load()[0].text == "Low-latency serving runtime with speculative decoding."


def test_missing_description_becomes_empty_text():
    assert load()[1].text == ""


def test_stars_and_topics_land_in_meta():
    first = load()[0]
    assert first.meta["stars"] == 1840
    assert first.meta["topics"] == ["llm", "inference"]
    assert first.meta["language"] == "Python"
    assert first.meta["created_at"] == "2026-08-30T10:00:00Z"


def test_source_is_github():
    assert load()[0].source == "github"


def test_skips_repos_missing_required_fields():
    payload = {"items": [
        {"description": "no url or name", "stargazers_count": 999},
        {"full_name": "a/b", "stargazers_count": 10},
    ]}
    assert github.parse(payload) == []


def test_one_malformed_repo_does_not_lose_the_others():
    payload = {"items": [
        {"full_name": "good/one", "html_url": "https://github.com/good/one",
         "description": "d", "stargazers_count": 5},
        {"description": "broken, no url or full_name"},
        {"full_name": "also/good", "html_url": "https://github.com/also/good",
         "description": "d", "stargazers_count": 7},
    ]}
    assert [i.title for i in github.parse(payload)] == ["good/one", "also/good"]

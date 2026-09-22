import random

from agents import finalize_critic, prepare_critic
from send import digest


def ours():
    return [
        {
            "id": "a",
            "title": "Firehose Picks a Winner",
            "url": "https://x/a",
            "source": "hn",
            "tier": "headline",
            "summary": "A model shipped with 71.2 on SWE-bench. (3 minute read)",
        },
        {
            "id": "b",
            "title": "Second Story",
            "url": "https://x/b",
            "source": "arxiv",
            "tier": "discovery",
            "summary": "Something else happened. (2 minute read)",
        },
    ]


def theirs(n=2):
    return [{"title": f"Their Story {i}", "summary": f"Their summary {i}."} for i in range(n)]


def blind(seed=0, mine=None, rival=None):
    return prepare_critic.blind(
        mine or ours(), rival or theirs(), random.Random(seed)
    )


def test_blind_strips_every_identifying_field():
    payload, _ = blind()
    for side in ("newsletter_a", "newsletter_b"):
        for item in payload[side]:
            assert set(item) == {"title", "summary"}


def test_blind_strips_reading_times_from_our_side():
    payload, key = blind()
    mine = payload["newsletter_a" if key["A"] == "firehose" else "newsletter_b"]
    assert not any("minute read" in i["summary"] for i in mine)


def test_blind_redacts_brand_names():
    payload, key = blind()
    mine = payload["newsletter_a" if key["A"] == "firehose" else "newsletter_b"]
    assert "Firehose" not in mine[0]["title"]
    assert "[redacted]" in mine[0]["title"]


def test_blind_caps_both_sides_at_the_same_length():
    payload, _ = blind(rival=theirs(30))
    assert len(payload["newsletter_b"]) <= prepare_critic.LIMIT
    assert len(payload["newsletter_a"]) <= prepare_critic.LIMIT


def test_blind_shuffles_both_ways_across_runs():
    seen = {blind(seed)[1]["A"] for seed in range(10)}
    assert seen == {"firehose", "tldr"}


def test_blind_key_covers_both_sides():
    _, key = blind()
    assert sorted(key.values()) == ["firehose", "tldr"]


VERDICT = {
    "winner": "A",
    "verdict": "{{A}} led with numbers; {{B}} hedged.",
    "a_strength": "concrete facts",
    "b_strength": "broad range",
    "a_weakness": "thin on research",
    "b_weakness": "filler summaries",
}


def test_build_names_the_winner_from_the_key():
    built = finalize_critic.build(VERDICT, {"date": "2026-09-22", "A": "tldr", "B": "firehose"})
    assert built["winner"] == "TLDR AI"


def test_build_substitutes_placeholders():
    built = finalize_critic.build(VERDICT, {"date": "2026-09-22", "A": "firehose", "B": "tldr"})
    assert built["verdict"] == "Firehose led with numbers; TLDR AI hedged."
    assert "{{" not in built["verdict"]


def test_build_maps_notes_back_to_each_newsletter():
    built = finalize_critic.build(VERDICT, {"date": "2026-09-22", "A": "tldr", "B": "firehose"})
    assert built["ours"] == {"strength": "broad range", "weakness": "filler summaries"}
    assert built["theirs"] == {"strength": "concrete facts", "weakness": "thin on research"}


def test_build_accepts_a_tie():
    built = finalize_critic.build(
        {**VERDICT, "winner": "tie"}, {"date": "2026-09-22", "A": "firehose", "B": "tldr"}
    )
    assert built["winner"] == "tie"


def test_render_critique_is_telegram_html():
    built = finalize_critic.build(VERDICT, {"date": "2026-09-22", "A": "firehose", "B": "tldr"})
    text = digest.render_critique(built)
    assert "Blind verdict — 2026-09-22" in text
    assert "Winner: <b>Firehose</b>" in text
    assert "today we were A" in text


def test_render_critique_escapes_html():
    built = finalize_critic.build(
        {**VERDICT, "verdict": "a <b>bold</b> claim"},
        {"date": "2026-09-22", "A": "firehose", "B": "tldr"},
    )
    assert "&lt;b&gt;bold&lt;/b&gt;" in digest.render_critique(built)


def test_render_critique_survives_a_sparse_verdict():
    text = digest.render_critique({"date": "2026-09-22", "winner": "tie", "verdict": "too close"})
    assert "too close" in text

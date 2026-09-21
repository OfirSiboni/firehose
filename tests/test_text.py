from ingest.text import plain


def test_strips_tags():
    assert plain("<p>Model X runs at <b>2x</b> the speed.</p>") == "Model X runs at 2x the speed."


def test_decodes_entities():
    assert plain("I&#x27;m a 24 y&#x2F;o engineer") == "I'm a 24 y/o engineer"


def test_adjacent_blocks_do_not_run_together():
    assert plain("<p>first</p><p>second</p>") == "first second"


def test_collapses_whitespace_and_newlines():
    assert plain("  lots\n\n  of   space  ") == "lots of space"


def test_decodes_after_stripping_so_escaped_markup_survives_as_text():
    assert plain("&lt;script&gt;alert(1)&lt;/script&gt;") == "<script>alert(1)</script>"


def test_empty_input():
    assert plain("") == ""

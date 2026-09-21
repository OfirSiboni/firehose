# TLDR AI Curator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A GitHub-Actions-hosted daily pipeline that collects AI news from HN, arXiv, GitHub and company blogs, has a Claude agent rank and draft the best 6–8 stories, delivers them to a Telegram channel and a static site, and learns the operator's taste from emoji-reaction feedback.

**Architecture:** Two cron workflows. `ingest.yml` (every 3h) is plain Python: fetch, normalize, dedupe into `data/pool.jsonl`, and drain Telegram reactions into `data/labels.jsonl`. `digest.yml` (daily) runs two Claude Code agents in sequence — Judge (scores the pool, writes `data/ranked.json`) then Writer (drafts the top 8) — then plain Python sends to Telegram and publishes static HTML/RSS. All state is files in the repo; there is no database.

**Tech Stack:** Python 3.11, stdlib `urllib` for HTTP, `feedparser` for RSS/Atom, `pytest` for tests. GitHub Actions. `anthropics/claude-code-action@v1` authenticated with `CLAUDE_CODE_OAUTH_TOKEN`. GitHub Pages from `/docs`.

**Spec:** `docs/superpowers/specs/2026-09-21-tldr-curator-design.md`

## Global Constraints

- Python 3.11. Dependencies limited to `feedparser` and `pytest` — everything else stdlib.
- No database. All persistent state is files under `data/` committed to the repo.
- Every source fetch is individually wrapped in try/except. Ingest must never fail wholesale because one source broke.
- Timestamps are UTC ISO-8601 with a `Z` suffix: `2026-09-21T07:02:11Z`.
- Item ids are `sha1(normalized_url).hexdigest()[:12]`.
- Agent output is validated against a schema before anything is sent. A malformed agent run fails the job and sends nothing.
- Never pad a digest to reach 8 items. Fewer is correct.
- Repo is public. Secrets live only in GitHub Actions secrets: `CLAUDE_CODE_OAUTH_TOKEN`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`.
- Tests never assert on agent-generated prose. Agent tests are contract tests only.

---

### Task 1: Project scaffold and the Item model

The `Item` model plus URL normalization is the foundation every other task imports. URL
normalization is where near-duplicate stories leak through and make a digest look sloppy, so
it gets real tests first.yes

**Files:**
- Create: `requirements.txt`
- Create: `.gitignore`
- Create: `store/__init__.py`
- Create: `store/item.py`
- Create: `tests/__init__.py`
- Test: `tests/test_item.py`

**Interfaces:**
- Consumes: nothing (first task)
- Produces:
  - `Item` dataclass with fields `id: str`, `url: str`, `normalized_url: str`, `title: str`, `source: str`, `first_seen: str`, `text: str`, `meta: dict`, `sent_in: str | None`
  - `Item.to_dict() -> dict` and `Item.from_dict(d: dict) -> Item`
  - `normalize_url(url: str) -> str`
  - `item_id(normalized_url: str) -> str`
  - `make_item(url: str, title: str, source: str, text: str = "", meta: dict | None = None, now: str | None = None) -> Item`
  - `dedupe(items: list[Item]) -> list[Item]`

- [ ] **Step 1: Create the scaffold files**

`requirements.txt`:

```
feedparser==6.0.11
pytest==8.3.4
```

`.gitignore`:

```
__pycache__/
*.pyc
.pytest_cache/
.venv/
```

Create empty `store/__init__.py` and `tests/__init__.py`.

Then install:

```bash
python -m venv .venv && .venv/Scripts/pip install -r requirements.txt
```

- [ ] **Step 2: Write the failing test**

`tests/test_item.py`:

```python
import pytest

from store.item import Item, dedupe, item_id, make_item, normalize_url


@pytest.mark.parametrize(
    "raw,expected",
    [
        # tracking params are stripped
        ("https://example.com/post?utm_source=x&utm_medium=y", "https://example.com/post"),
        ("https://example.com/post?ref=hn", "https://example.com/post"),
        # scheme and www are canonicalized
        ("http://www.example.com/post", "https://example.com/post"),
        # trailing slash is dropped, but the root path survives
        ("https://example.com/post/", "https://example.com/post"),
        ("https://example.com/", "https://example.com/"),
        # arxiv pdf and versioned urls collapse onto /abs/
        ("https://arxiv.org/pdf/2509.12345v2.pdf", "https://arxiv.org/abs/2509.12345"),
        ("https://arxiv.org/abs/2509.12345v1", "https://arxiv.org/abs/2509.12345"),
        ("https://arxiv.org/abs/2509.12345", "https://arxiv.org/abs/2509.12345"),
        # meaningful query params survive and are sorted
        ("https://example.com/a?b=2&a=1", "https://example.com/a?a=1&b=2"),
    ],
)
def test_normalize_url(raw, expected):
    assert normalize_url(raw) == expected


def test_normalize_url_strips_whitespace():
    assert normalize_url("  https://example.com/post  ") == "https://example.com/post"


def test_item_id_is_stable_and_short():
    a = item_id("https://example.com/post")
    b = item_id("https://example.com/post")
    assert a == b
    assert len(a) == 12


def test_item_id_differs_by_url():
    assert item_id("https://example.com/a") != item_id("https://example.com/b")


def test_make_item_populates_derived_fields():
    item = make_item(
        url="http://www.example.com/post/?utm_source=hn",
        title="A Title",
        source="hn",
        text="body",
        meta={"points": 100},
        now="2026-09-21T06:00:00Z",
    )
    assert item.normalized_url == "https://example.com/post"
    assert item.id == item_id("https://example.com/post")
    assert item.first_seen == "2026-09-21T06:00:00Z"
    assert item.source == "hn"
    assert item.meta == {"points": 100}
    assert item.sent_in is None


def test_make_item_defaults_now_to_utc_z():
    item = make_item(url="https://example.com/x", title="T", source="hn")
    assert item.first_seen.endswith("Z")
    assert item.text == ""
    assert item.meta == {}


def test_round_trip_dict():
    item = make_item(url="https://example.com/x", title="T", source="hn", text="b")
    assert Item.from_dict(item.to_dict()) == item


def test_dedupe_keeps_first_occurrence_of_equivalent_urls():
    a = make_item(url="https://example.com/post", title="First", source="hn")
    b = make_item(url="http://www.example.com/post/?utm_source=x", title="Second", source="blog")
    out = dedupe([a, b])
    assert len(out) == 1
    assert out[0].title == "First"


def test_dedupe_preserves_distinct_items():
    a = make_item(url="https://example.com/a", title="A", source="hn")
    b = make_item(url="https://example.com/b", title="B", source="hn")
    assert len(dedupe([a, b])) == 2
```

- [ ] **Step 3: Run the test to verify it fails**

```bash
.venv/Scripts/python -m pytest tests/test_item.py -v
```

Expected: FAIL with `ModuleNotFoundError: No module named 'store.item'`

- [ ] **Step 4: Write the implementation**

`store/item.py`:

```python
"""Canonical item model and URL normalization."""

from __future__ import annotations

import hashlib
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

# Params that carry no meaning and would otherwise split one story into several.
TRACKING_PREFIXES = ("utm_",)
TRACKING_EXACT = {"ref", "fbclid", "gclid", "igshid", "mc_cid", "mc_eid"}

_ARXIV_PATH = re.compile(r"^/(?:abs|pdf)/(.+?)(?:v\d+)?(?:\.pdf)?$")


def utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def normalize_url(url: str) -> str:
    """Collapse cosmetically different URLs onto one canonical form."""
    parts = urlsplit(url.strip())
    host = parts.netloc.lower()
    if host.startswith("www."):
        host = host[4:]

    path = parts.path
    if host == "arxiv.org":
        match = _ARXIV_PATH.match(path)
        if match:
            path = f"/abs/{match.group(1)}"
    if len(path) > 1 and path.endswith("/"):
        path = path[:-1]

    query = sorted(
        (k, v)
        for k, v in parse_qsl(parts.query, keep_blank_values=True)
        if k.lower() not in TRACKING_EXACT
        and not k.lower().startswith(TRACKING_PREFIXES)
    )
    return urlunsplit(("https", host, path, urlencode(query), ""))


def item_id(normalized_url: str) -> str:
    return hashlib.sha1(normalized_url.encode("utf-8")).hexdigest()[:12]


@dataclass
class Item:
    id: str
    url: str
    normalized_url: str
    title: str
    source: str
    first_seen: str
    text: str = ""
    meta: dict = field(default_factory=dict)
    sent_in: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Item":
        return cls(**data)


def make_item(
    url: str,
    title: str,
    source: str,
    text: str = "",
    meta: dict | None = None,
    now: str | None = None,
) -> Item:
    normalized = normalize_url(url)
    return Item(
        id=item_id(normalized),
        url=url.strip(),
        normalized_url=normalized,
        title=title.strip(),
        source=source,
        first_seen=now or utcnow(),
        text=text,
        meta=meta or {},
    )


def dedupe(items: list[Item]) -> list[Item]:
    """Keep the first occurrence of each id, preserving order."""
    seen: set[str] = set()
    out: list[Item] = []
    for item in items:
        if item.id in seen:
            continue
        seen.add(item.id)
        out.append(item)
    return out
```

- [ ] **Step 5: Run the test to verify it passes**

```bash
.venv/Scripts/python -m pytest tests/test_item.py -v
```

Expected: PASS, 17 tests (the parametrized case expands to 9, plus 8 others)

- [ ] **Step 6: Commit**

```bash
git add requirements.txt .gitignore store tests
git commit -m "feat: item model and URL normalization"
```

---

### Task 2: HTTP helper and Hacker News source

Folds in the shared HTTP helper, since HN is its first consumer. Sources are split into a
pure `parse()` (tested offline against a recorded fixture) and a thin `fetch()` (network).
Only `parse()` is unit tested — that is where the logic lives.

**Files:**
- Create: `ingest/__init__.py`
- Create: `ingest/http.py`
- Create: `ingest/text.py`
- Create: `ingest/sources/__init__.py`
- Create: `ingest/sources/hn.py`
- Create: `tests/fixtures/hn_sample.json`
- Test: `tests/test_text.py`
- Test: `tests/test_hn.py`

**Interfaces:**
- Consumes: `store.item.make_item`, `store.item.Item`
- Produces:
  - `ingest.http.get_json(url: str, timeout: int = 20) -> dict`
  - `ingest.http.get_text(url: str, timeout: int = 20) -> str`
  - `ingest.text.plain(raw: str) -> str` — strips tags, decodes entities, collapses whitespace
  - `ingest.sources.hn.parse(payload: dict) -> list[Item]`
  - `ingest.sources.hn.fetch(hours: int = 24, min_points: int = 30) -> list[Item]`
  - Every HN item carries `meta["kind"]` of `"article"` or `"discussion"`

**Two things the fixture exists to pin.** Algolia returns `url: null` for text posts
(`Ask HN`, `Tell HN`, most job posts) — the content *is* the HN thread. Passing that `None`
into `normalize_url` raises `AttributeError` and takes down the whole HN fetch, so the
permalink fallback is load-bearing. And `story_text` arrives as **HTML** — real responses
contain `<p>` tags and entities like `&#x27;` — which must be cleaned before the Judge reads
it.

Text posts are tagged `kind: "discussion"`. They stay in the pool because they are useful
research signal, but Task 11 makes them ineligible for the digest: a TLDR item must link to a
readable artifact, and a discussion thread is not one.

- [ ] **Step 1: Create the fixture**

`tests/fixtures/hn_sample.json` — a trimmed real Algolia response. The third hit is a text
post: `url: null`, with HTML in `story_text`:

```json
{
  "hits": [
    {
      "objectID": "41000001",
      "title": "Llama 4 released with 10M context",
      "url": "https://ai.meta.com/blog/llama-4/?utm_source=hn",
      "points": 842,
      "num_comments": 310,
      "created_at_i": 1758434400,
      "story_text": null
    },
    {
      "objectID": "41000002",
      "title": "vLLM v0.9 adds speculative decoding",
      "url": "https://blog.vllm.ai/2026/09/v09.html",
      "points": 210,
      "num_comments": 44,
      "created_at_i": 1758430800,
      "story_text": null
    },
    {
      "objectID": "41000003",
      "title": "Ask HN: What are you running locally in 2026?",
      "url": null,
      "points": 156,
      "num_comments": 289,
      "created_at_i": 1758427200,
      "story_text": "I&#x27;m curious what people actually keep loaded.<p>Especially on 24GB cards."
    }
  ]
}
```

- [ ] **Step 2: Write the shared HTML-to-text helper**

Both HN (`story_text`) and blogs (RSS `description`) deliver HTML. One helper, used by both,
so the Judge never reads `&#x27;` or a stray `<p>`.

`tests/test_text.py`:

```python
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
```

Run it and watch it fail:

```bash
.venv/Scripts/python -m pytest tests/test_text.py -v
```

Expected: FAIL with `ModuleNotFoundError: No module named 'ingest'`

Create empty `ingest/__init__.py` and `ingest/sources/__init__.py`, then `ingest/text.py`:

```python
"""HTML to plain text. Feeds are HTML; the Judge should read prose."""

from __future__ import annotations

import html
import re

_TAGS = re.compile(r"<[^>]+>")


def plain(raw: str) -> str:
    """Strip tags, decode entities, collapse whitespace.

    Tags become a space, not nothing, so "<p>a</p><p>b</p>" is "a b" not "ab".
    Unescaping happens after stripping so escaped markup stays text.
    """
    return " ".join(html.unescape(_TAGS.sub(" ", raw)).split())
```

```bash
.venv/Scripts/python -m pytest tests/test_text.py -v
```

Expected: PASS, 6 tests

- [ ] **Step 3: Write the failing HN test**

`tests/test_hn.py`:

```python
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
```

- [ ] **Step 4: Run the test to verify it fails**

```bash
.venv/Scripts/python -m pytest tests/test_hn.py -v
```

Expected: FAIL with `ImportError: cannot import name 'hn'`

- [ ] **Step 5: Write the implementation**

`ingest/http.py`:

```python
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
```

`ingest/sources/hn.py`:

```python
"""Hacker News via the Algolia search API."""

from __future__ import annotations

import time

from ingest.http import get_json
from ingest.text import plain
from store.item import Item, make_item

API = "https://hn.algolia.com/api/v1/search_by_date"


def parse(payload: dict) -> list[Item]:
    items: list[Item] = []
    for hit in payload.get("hits", []):
        title = hit.get("title")
        if not title:
            continue
        permalink = f"https://news.ycombinator.com/item?id={hit['objectID']}"
        # No url means a text post (Ask HN, Tell HN, jobs): the thread *is* the
        # content. Keep it as research signal, but mark it unpublishable — a
        # TLDR item has to link to something readable.
        external = hit.get("url")
        items.append(
            make_item(
                url=external or permalink,
                title=title,
                source="hn",
                text=plain(hit.get("story_text") or ""),
                meta={
                    "points": hit.get("points", 0),
                    "comments": hit.get("num_comments", 0),
                    "hn_url": permalink,
                    "kind": "article" if external else "discussion",
                },
            )
        )
    return items


def fetch(hours: int = 24, min_points: int = 30) -> list[Item]:
    cutoff = int(time.time()) - hours * 3600
    url = (
        f"{API}?tags=story"
        f"&numericFilters=points>{min_points},created_at_i>{cutoff}"
        f"&hitsPerPage=100"
    )
    return parse(get_json(url))
```

- [ ] **Step 6: Run the test to verify it passes**

```bash
.venv/Scripts/python -m pytest tests/test_hn.py -v
```

Expected: PASS, 9 tests

- [ ] **Step 7: Verify the live endpoint works**

```bash
.venv/Scripts/python -c "from ingest.sources import hn; items = hn.fetch(); print(len(items)); print(items[0].title)"
```

Expected: a count above 0 and a real headline. If it fails, the Algolia URL shape changed —
fix `fetch()` before continuing; `parse()` and its tests should not need to change.

- [ ] **Step 8: Commit**

```bash
git add ingest tests/test_text.py tests/test_hn.py tests/fixtures/hn_sample.json
git commit -m "feat: http helper, html-to-text, and Hacker News source"
```

---

### Task 3: arXiv source

arXiv returns Atom, so `feedparser` handles it — the same dependency the blog source will
use, so no new one is added.

**Files:**
- Create: `ingest/sources/arxiv.py`
- Create: `tests/fixtures/arxiv_sample.xml`
- Test: `tests/test_arxiv.py`

**Interfaces:**
- Consumes: `store.item.make_item`, `store.item.Item`, `ingest.http.get_text`
- Produces:
  - `ingest.sources.arxiv.parse(xml: str) -> list[Item]`
  - `ingest.sources.arxiv.fetch(max_results: int = 100) -> list[Item]`

- [ ] **Step 1: Create the fixture**

`tests/fixtures/arxiv_sample.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <id>http://arxiv.org/abs/2509.12345v1</id>
    <updated>2026-09-20T17:21:03Z</updated>
    <published>2026-09-20T17:21:03Z</published>
    <title>Cache Eviction Policies for Long-Context Inference</title>
    <summary>  We introduce a KV-cache eviction policy that achieves 3.1x
  throughput at equal quality.
  </summary>
    <author><name>Jane Doe</name></author>
    <author><name>Wei Zhang</name></author>
    <link href="http://arxiv.org/abs/2509.12345v1" rel="alternate" type="text/html"/>
    <category term="cs.LG" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2509.99999v2</id>
    <updated>2026-09-20T09:00:00Z</updated>
    <published>2026-09-19T09:00:00Z</published>
    <title>A Survey of Surveys</title>
    <summary>We survey surveys.</summary>
    <author><name>John Roe</name></author>
    <link href="http://arxiv.org/abs/2509.99999v2" rel="alternate" type="text/html"/>
    <category term="cs.AI" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
</feed>
```

- [ ] **Step 2: Write the failing test**

`tests/test_arxiv.py`:

```python
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
```

- [ ] **Step 3: Run the test to verify it fails**

```bash
.venv/Scripts/python -m pytest tests/test_arxiv.py -v
```

Expected: FAIL with `ImportError: cannot import name 'arxiv'`

- [ ] **Step 4: Write the implementation**

`ingest/sources/arxiv.py`:

```python
"""arXiv cs.AI / cs.LG / cs.CL via the Atom export API."""

from __future__ import annotations

import feedparser

from ingest.http import get_text
from store.item import Item, make_item

API = "http://export.arxiv.org/api/query"
CATEGORIES = "cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL"


def parse(xml: str) -> list[Item]:
    feed = feedparser.parse(xml)
    items: list[Item] = []
    for entry in feed.entries:
        title = " ".join(entry.get("title", "").split())
        if not title:
            continue
        link = entry.get("link") or entry.get("id", "")
        categories = [t.get("term") for t in entry.get("tags", []) if t.get("term")]
        items.append(
            make_item(
                url=link,
                title=title,
                source="arxiv",
                text=" ".join(entry.get("summary", "").split()),
                meta={
                    "authors": [a.get("name") for a in entry.get("authors", [])],
                    "primary_category": categories[0] if categories else None,
                    "published": entry.get("published"),
                },
            )
        )
    return items


def fetch(max_results: int = 100) -> list[Item]:
    url = (
        f"{API}?search_query={CATEGORIES}"
        f"&sortBy=submittedDate&sortOrder=descending&max_results={max_results}"
    )
    return parse(get_text(url))
```

- [ ] **Step 5: Run the test to verify it passes**

```bash
.venv/Scripts/python -m pytest tests/test_arxiv.py -v
```

Expected: PASS, 5 tests

- [ ] **Step 6: Verify the live endpoint works**

```bash
.venv/Scripts/python -c "from ingest.sources import arxiv; items = arxiv.fetch(5); print(len(items)); print(items[0].title)"
```

Expected: 5 items and a real paper title.

- [ ] **Step 7: Commit**

```bash
git add ingest/sources/arxiv.py tests/test_arxiv.py tests/fixtures/arxiv_sample.xml
git commit -m "feat: arXiv source"
```

---

### Task 4: GitHub source

Uses the repository search API for recently created repos with traction. Star *velocity*
would be a better signal than star count, but GitHub does not expose it; because `meta`
records `stars` on every run, velocity becomes derivable from our own pool history later.
That seam is free, so take it now and compute nothing.

**Files:**
- Create: `ingest/sources/github.py`
- Create: `tests/fixtures/github_sample.json`
- Test: `tests/test_github.py`

**Interfaces:**
- Consumes: `store.item.make_item`, `store.item.Item`, `ingest.http.get_json`
- Produces:
  - `ingest.sources.github.parse(payload: dict) -> list[Item]`
  - `ingest.sources.github.fetch(days: int = 60, min_stars: int = 150) -> list[Item]`

- [ ] **Step 1: Create the fixture**

`tests/fixtures/github_sample.json`:

```json
{
  "items": [
    {
      "full_name": "vllm-project/flashserve",
      "html_url": "https://github.com/vllm-project/flashserve",
      "description": "Low-latency serving runtime with speculative decoding.",
      "stargazers_count": 1840,
      "created_at": "2026-08-30T10:00:00Z",
      "pushed_at": "2026-09-20T22:10:00Z",
      "language": "Python",
      "topics": ["llm", "inference"]
    },
    {
      "full_name": "someone/no-description-repo",
      "html_url": "https://github.com/someone/no-description-repo",
      "description": null,
      "stargazers_count": 220,
      "created_at": "2026-09-01T10:00:00Z",
      "pushed_at": "2026-09-19T10:00:00Z",
      "language": null,
      "topics": []
    }
  ]
}
```

- [ ] **Step 2: Write the failing test**

`tests/test_github.py`:

```python
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
```

- [ ] **Step 3: Run the test to verify it fails**

```bash
.venv/Scripts/python -m pytest tests/test_github.py -v
```

Expected: FAIL with `ImportError: cannot import name 'github'`

- [ ] **Step 4: Write the implementation**

`ingest/sources/github.py`:

```python
"""Recently created AI repos with traction, via the GitHub search API."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

from ingest.http import get_json
from store.item import Item, make_item

API = "https://api.github.com/search/repositories"
TOPICS = ["llm", "ai-agents", "machine-learning", "inference", "rag"]


def parse(payload: dict) -> list[Item]:
    items: list[Item] = []
    for repo in payload.get("items", []):
        items.append(
            make_item(
                url=repo["html_url"],
                title=repo["full_name"],
                source="github",
                text=repo.get("description") or "",
                meta={
                    "stars": repo.get("stargazers_count", 0),
                    "topics": repo.get("topics", []),
                    "language": repo.get("language"),
                    "created_at": repo.get("created_at"),
                    "pushed_at": repo.get("pushed_at"),
                },
            )
        )
    return items


def fetch(days: int = 60, min_stars: int = 150) -> list[Item]:
    since = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    items: list[Item] = []
    for topic in TOPICS:
        query = f"topic:{topic}+created:>{since}+stars:>{min_stars}"
        url = f"{API}?q={query}&sort=stars&order=desc&per_page=20"
        items.extend(parse(get_json(url)))
    return items
```

- [ ] **Step 5: Run the test to verify it passes**

```bash
.venv/Scripts/python -m pytest tests/test_github.py -v
```

Expected: PASS, 6 tests

- [ ] **Step 6: Verify the live endpoint works**

```bash
.venv/Scripts/python -c "from ingest.sources import github; items = github.fetch(); print(len(items)); print(items[0].title, items[0].meta['stars'])"
```

Expected: a count above 0. Unauthenticated GitHub search allows 10 requests/minute; five
topic queries per run is comfortably inside that.

- [ ] **Step 7: Commit**

```bash
git add ingest/sources/github.py tests/test_github.py tests/fixtures/github_sample.json
git commit -m "feat: GitHub source"
```

---

### Task 5: Blog source and the feed list

The feed list is a plain text file rather than YAML or JSON so it can carry comments with no
extra dependency. Adding a blog must never require touching code.

**Files:**
- Create: `ingest/feeds.txt`
- Create: `ingest/sources/blogs.py`
- Create: `tests/fixtures/blog_sample.xml`
- Test: `tests/test_blogs.py`

**Interfaces:**
- Consumes: `store.item.make_item`, `store.item.Item`, `ingest.http.get_text`, `ingest.text.plain`
- Produces:
  - `ingest.sources.blogs.load_feeds(path: Path | None = None) -> list[str]`
  - `ingest.sources.blogs.parse(xml: str, feed_name: str) -> list[Item]`
  - `ingest.sources.blogs.fetch(path: Path | None = None) -> list[Item]`

- [ ] **Step 1: Create the feed list and fixture**

`ingest/feeds.txt`:

```
# AI company and practitioner blogs. One URL per line, # starts a comment.
# Verify with: python -m ingest.run --smoke
https://openai.com/blog/rss.xml
https://www.anthropic.com/news/rss.xml
https://deepmind.google/blog/rss.xml
https://ai.meta.com/blog/rss/
https://huggingface.co/blog/feed.xml
https://blog.google/technology/ai/rss/
https://mistral.ai/news/feed.xml
https://simonwillison.net/atom/everything/
https://lilianweng.github.io/index.xml
```

`tests/fixtures/blog_sample.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Example AI Blog</title>
    <item>
      <title>Introducing Model X</title>
      <link>https://example.com/blog/model-x?utm_campaign=rss</link>
      <pubDate>Sat, 20 Sep 2026 12:00:00 GMT</pubDate>
      <description>&lt;p&gt;Model X runs at &lt;b&gt;2x&lt;/b&gt; the speed.&lt;/p&gt;</description>
    </item>
    <item>
      <title>Company Retreat Photos</title>
      <link>https://example.com/blog/retreat</link>
      <pubDate>Fri, 19 Sep 2026 12:00:00 GMT</pubDate>
      <description>Some photos from the team&amp;#x27;s retreat.</description>
    </item>
  </channel>
</rss>
```

- [ ] **Step 2: Write the failing test**

`tests/test_blogs.py`:

```python
from pathlib import Path

from ingest.sources import blogs

FIXTURE = Path(__file__).parent / "fixtures" / "blog_sample.xml"


def load():
    return blogs.parse(FIXTURE.read_text(encoding="utf-8"), "example.com")


def test_parses_every_entry():
    assert len(load()) == 2


def test_strips_tracking_params_from_the_link():
    assert load()[0].normalized_url == "https://example.com/blog/model-x"


def test_strips_html_from_the_description():
    assert load()[0].text == "Model X runs at 2x the speed."


def test_decodes_entities_that_survive_xml_unescaping():
    # Feeds routinely double-escape: the XML carries &amp;#x27;, feedparser
    # hands back &#x27;, and only plain() turns it into an apostrophe.
    assert load()[1].text == "Some photos from the team's retreat."


def test_records_the_feed_name_in_meta():
    assert load()[0].meta["feed"] == "example.com"


def test_source_is_blog():
    assert load()[0].source == "blog"


def test_load_feeds_ignores_comments_and_blank_lines(tmp_path):
    path = tmp_path / "feeds.txt"
    path.write_text(
        "# a comment\n\nhttps://a.com/rss\n   \nhttps://b.com/rss  \n",
        encoding="utf-8",
    )
    assert blogs.load_feeds(path) == ["https://a.com/rss", "https://b.com/rss"]
```

- [ ] **Step 3: Run the test to verify it fails**

```bash
.venv/Scripts/python -m pytest tests/test_blogs.py -v
```

Expected: FAIL with `ImportError: cannot import name 'blogs'`

- [ ] **Step 4: Write the implementation**

`ingest/sources/blogs.py`:

```python
"""AI company and practitioner blogs via RSS/Atom."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import urlsplit

import feedparser

from ingest.http import get_text
from ingest.text import plain
from store.item import Item, make_item

FEEDS_PATH = Path(__file__).resolve().parent.parent / "feeds.txt"


def load_feeds(path: Path | None = None) -> list[str]:
    lines = (path or FEEDS_PATH).read_text(encoding="utf-8").splitlines()
    return [
        stripped
        for line in lines
        if (stripped := line.strip()) and not stripped.startswith("#")
    ]


def parse(xml: str, feed_name: str) -> list[Item]:
    feed = feedparser.parse(xml)
    items: list[Item] = []
    for entry in feed.entries:
        title = " ".join(entry.get("title", "").split())
        link = entry.get("link")
        if not title or not link:
            continue
        body = entry.get("summary") or entry.get("description") or ""
        items.append(
            make_item(
                url=link,
                title=title,
                source="blog",
                text=plain(body)[:2000],
                meta={"feed": feed_name, "published": entry.get("published")},
            )
        )
    return items


def fetch(path: Path | None = None) -> list[Item]:
    items: list[Item] = []
    for url in load_feeds(path):
        name = urlsplit(url).netloc.lower().removeprefix("www.")
        try:
            items.extend(parse(get_text(url), name))
        except Exception as exc:  # one dead feed must not kill the rest
            print(f"[blogs] {name} failed: {exc}")
    return items
```

- [ ] **Step 5: Run the test to verify it passes**

```bash
.venv/Scripts/python -m pytest tests/test_blogs.py -v
```

Expected: PASS, 7 tests

- [ ] **Step 6: Verify the feed list live and prune what is broken**

```bash
.venv/Scripts/python -c "from ingest.sources import blogs; items = blogs.fetch(); print(len(items))"
```

Feed URLs move. Any feed printing a `failed:` line should be corrected or removed from
`ingest/feeds.txt` now — a permanently dead feed is noise in every future run's logs.

- [ ] **Step 7: Commit**

```bash
git add ingest/feeds.txt ingest/sources/blogs.py tests/test_blogs.py tests/fixtures/blog_sample.xml
git commit -m "feat: blog RSS source and feed list"
```

---

### Task 6: Pool store and the ingest runner

The pool is an append-only JSONL file with a 7-day window. This task also adds the runner
that ties the four sources together with per-source isolation.

**Files:**
- Create: `store/pool.py`
- Create: `store/health.py`
- Create: `ingest/run.py`
- Test: `tests/test_pool.py`
- Test: `tests/test_health.py`

**Interfaces:**
- Consumes: `store.item.Item`, `store.item.dedupe`, all four `fetch()` functions
- Produces:
  - `store.health.record(counts: dict[str, int], keep: int = 8) -> None`
  - `store.health.dead_sources(runs: int = 3) -> list[str]` — sources with zero items across the last `runs` runs
  - `store.health.HEALTH_PATH` — `Path("data/source_health.json")`
  - `store.pool.load_pool(path: Path = POOL_PATH) -> list[Item]`
  - `store.pool.save_pool(items: list[Item], path: Path = POOL_PATH) -> None`
  - `store.pool.merge(existing: list[Item], incoming: list[Item]) -> tuple[list[Item], int]` — returns the merged list and the count of genuinely new items
  - `store.pool.expire(items: list[Item], now: datetime | None = None, days: int = 7) -> list[Item]`
  - `store.pool.unsent_since(items: list[Item], hours: int = 36, now: datetime | None = None) -> list[Item]`
  - `store.pool.mark_sent(items: list[Item], ids: list[str], digest_date: str) -> list[Item]`
  - `store.pool.POOL_PATH` — `Path("data/pool.jsonl")`

- [ ] **Step 1: Write the failing test**

`tests/test_pool.py`:

```python
from datetime import datetime, timezone

from store import pool
from store.item import make_item


def at(day: int, hour: int = 12) -> str:
    return f"2026-09-{day:02d}T{hour:02d}:00:00Z"


NOW = datetime(2026, 9, 21, 12, 0, 0, tzinfo=timezone.utc)


def test_save_and_load_round_trip(tmp_path):
    path = tmp_path / "pool.jsonl"
    items = [make_item(url="https://example.com/a", title="A", source="hn", now=at(21))]
    pool.save_pool(items, path)
    assert pool.load_pool(path) == items


def test_load_returns_empty_when_file_is_absent(tmp_path):
    assert pool.load_pool(tmp_path / "nope.jsonl") == []


def test_merge_adds_only_new_items():
    existing = [make_item(url="https://example.com/a", title="A", source="hn", now=at(20))]
    incoming = [
        make_item(url="https://example.com/a", title="A again", source="hn", now=at(21)),
        make_item(url="https://example.com/b", title="B", source="hn", now=at(21)),
    ]
    merged, new_count = pool.merge(existing, incoming)
    assert new_count == 1
    assert len(merged) == 2


def test_merge_keeps_the_original_first_seen():
    existing = [make_item(url="https://example.com/a", title="A", source="hn", now=at(20))]
    incoming = [make_item(url="https://example.com/a", title="A", source="hn", now=at(21))]
    merged, _ = pool.merge(existing, incoming)
    assert merged[0].first_seen == at(20)


def test_expire_drops_items_older_than_the_window():
    items = [
        make_item(url="https://example.com/old", title="Old", source="hn", now=at(10)),
        make_item(url="https://example.com/new", title="New", source="hn", now=at(20)),
    ]
    kept = pool.expire(items, now=NOW, days=7)
    assert [i.title for i in kept] == ["New"]


def test_unsent_since_filters_by_age_and_sent_flag():
    fresh = make_item(url="https://example.com/fresh", title="Fresh", source="hn", now=at(21, 0))
    stale = make_item(url="https://example.com/stale", title="Stale", source="hn", now=at(18))
    already = make_item(url="https://example.com/sent", title="Sent", source="hn", now=at(21, 0))
    already.sent_in = "2026-09-21"
    out = pool.unsent_since([fresh, stale, already], hours=36, now=NOW)
    assert [i.title for i in out] == ["Fresh"]


def test_mark_sent_stamps_only_the_named_ids():
    a = make_item(url="https://example.com/a", title="A", source="hn", now=at(21))
    b = make_item(url="https://example.com/b", title="B", source="hn", now=at(21))
    out = pool.mark_sent([a, b], [a.id], "2026-09-21")
    assert out[0].sent_in == "2026-09-21"
    assert out[1].sent_in is None
```

- [ ] **Step 2: Run the test to verify it fails**

```bash
.venv/Scripts/python -m pytest tests/test_pool.py -v
```

Expected: FAIL with `ImportError: cannot import name 'pool'`

- [ ] **Step 3: Write the pool implementation**

`store/pool.py`:

```python
"""The rolling candidate pool, stored as JSONL in the repo."""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

from store.item import Item

POOL_PATH = Path("data/pool.jsonl")


def _parse_ts(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def load_pool(path: Path = POOL_PATH) -> list[Item]:
    if not path.exists():
        return []
    return [
        Item.from_dict(json.loads(line))
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def save_pool(items: list[Item], path: Path = POOL_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    body = "\n".join(json.dumps(i.to_dict(), ensure_ascii=False) for i in items)
    path.write_text(body + "\n" if body else "", encoding="utf-8")


def merge(existing: list[Item], incoming: list[Item]) -> tuple[list[Item], int]:
    """Add items we have not seen. Existing entries win — first_seen is preserved."""
    known = {item.id for item in existing}
    fresh = []
    for item in incoming:
        if item.id in known:
            continue
        known.add(item.id)
        fresh.append(item)
    return existing + fresh, len(fresh)


def expire(items: list[Item], now: datetime | None = None, days: int = 7) -> list[Item]:
    cutoff = (now or datetime.now(timezone.utc)) - timedelta(days=days)
    return [i for i in items if _parse_ts(i.first_seen) >= cutoff]


def unsent_since(
    items: list[Item], hours: int = 36, now: datetime | None = None
) -> list[Item]:
    cutoff = (now or datetime.now(timezone.utc)) - timedelta(hours=hours)
    return [
        i for i in items if i.sent_in is None and _parse_ts(i.first_seen) >= cutoff
    ]


def mark_sent(items: list[Item], ids: list[str], digest_date: str) -> list[Item]:
    targets = set(ids)
    for item in items:
        if item.id in targets:
            item.sent_in = digest_date
    return items
```

- [ ] **Step 4: Run the test to verify it passes**

```bash
.venv/Scripts/python -m pytest tests/test_pool.py -v
```

Expected: PASS, 7 tests

- [ ] **Step 5: Write the source-health tracker**

A source that dies quietly is the failure mode that degrades the digest without anyone
noticing. This records per-run counts and reports what has been silent.

`tests/test_health.py`:

```python
from store import health


def test_dead_sources_needs_three_consecutive_zero_runs(tmp_path, monkeypatch):
    monkeypatch.setattr(health, "HEALTH_PATH", tmp_path / "health.json")
    health.record({"hn": 10, "arxiv": 0})
    health.record({"hn": 10, "arxiv": 0})
    assert health.dead_sources(3) == []
    health.record({"hn": 10, "arxiv": 0})
    assert health.dead_sources(3) == ["arxiv"]


def test_a_single_good_run_clears_a_source(tmp_path, monkeypatch):
    monkeypatch.setattr(health, "HEALTH_PATH", tmp_path / "health.json")
    for _ in range(3):
        health.record({"arxiv": 0})
    health.record({"arxiv": 5})
    assert health.dead_sources(3) == []


def test_dead_sources_is_empty_with_no_history(tmp_path, monkeypatch):
    monkeypatch.setattr(health, "HEALTH_PATH", tmp_path / "health.json")
    assert health.dead_sources() == []


def test_record_keeps_only_the_last_n_runs(tmp_path, monkeypatch):
    monkeypatch.setattr(health, "HEALTH_PATH", tmp_path / "health.json")
    for i in range(12):
        health.record({"hn": i}, keep=8)
    import json
    assert len(json.loads((tmp_path / "health.json").read_text(encoding="utf-8"))) == 8
```

Run it and watch it fail:

```bash
.venv/Scripts/python -m pytest tests/test_health.py -v
```

Expected: FAIL with `ImportError: cannot import name 'health'`

`store/health.py`:

```python
"""Per-run source counts, so a quietly dead source becomes visible."""

from __future__ import annotations

import json
from pathlib import Path

HEALTH_PATH = Path("data/source_health.json")


def _load() -> list[dict[str, int]]:
    if not HEALTH_PATH.exists():
        return []
    return json.loads(HEALTH_PATH.read_text(encoding="utf-8"))


def record(counts: dict[str, int], keep: int = 8) -> None:
    history = (_load() + [counts])[-keep:]
    HEALTH_PATH.parent.mkdir(parents=True, exist_ok=True)
    HEALTH_PATH.write_text(json.dumps(history, indent=2), encoding="utf-8")


def dead_sources(runs: int = 3) -> list[str]:
    """Sources that returned nothing across the last `runs` runs."""
    history = _load()[-runs:]
    if len(history) < runs:
        return []
    names = {name for run in history for name in run}
    return sorted(n for n in names if all(run.get(n, 0) == 0 for run in history))
```

Run it again:

```bash
.venv/Scripts/python -m pytest tests/test_health.py -v
```

Expected: PASS, 4 tests

- [ ] **Step 6: Write the ingest runner**

`ingest/run.py`:

```python
"""Fetch every source, merge into the pool, expire the tail."""

from __future__ import annotations

import sys

from ingest.sources import arxiv, blogs, github, hn
from store import health, pool
from store.item import dedupe

SOURCES = {
    "hn": hn.fetch,
    "arxiv": arxiv.fetch,
    "github": github.fetch,
    "blogs": blogs.fetch,
}


def collect() -> tuple[list, dict[str, int]]:
    """Fetch every source in isolation. One failure must not lose the others."""
    items, counts = [], {}
    for name, fetch in SOURCES.items():
        try:
            found = fetch()
            counts[name] = len(found)
            items.extend(found)
            print(f"[{name}] {len(found)} items")
        except Exception as exc:
            counts[name] = 0
            print(f"[{name}] FAILED: {exc}", file=sys.stderr)
    return items, counts


def main(smoke: bool = False) -> int:
    items, counts = collect()
    if smoke:
        dead = [name for name, count in counts.items() if count == 0]
        print(f"\nsmoke: {counts}")
        if dead:
            print(f"smoke: NO ITEMS from {dead}", file=sys.stderr)
            return 1
        return 0

    health.record(counts)
    existing = pool.load_pool()
    merged, new_count = pool.merge(existing, dedupe(items))
    kept = pool.expire(merged)
    pool.save_pool(kept)
    print(f"\n+{new_count} new, {len(kept)} in pool")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(smoke="--smoke" in sys.argv))
```

- [ ] **Step 7: Run the smoke check and then a real ingest**

```bash
.venv/Scripts/python -m ingest.run --smoke
```

Expected: per-source counts, all above 0, exit 0.

```bash
.venv/Scripts/python -m ingest.run
```

Expected: `+N new, N in pool` and a populated `data/pool.jsonl`.

- [ ] **Step 8: Commit**

```bash
git add store/pool.py store/health.py ingest/run.py tests/test_pool.py tests/test_health.py data/
git commit -m "feat: pool store, source health, and ingest runner"
```

---

### Task 7: The ingest workflow

First cron. After this lands, the pool fills on its own — which is the input to the Phase 1
gate: let it run for three days and read `data/pool.jsonl` before building any ranking.

**Files:**
- Create: `.github/workflows/ingest.yml`
- Create: `README.md`

**Interfaces:**
- Consumes: `ingest.run.main`
- Produces: `data/pool.jsonl` committed every 3 hours on `main`

- [ ] **Step 1: Write the workflow**

`.github/workflows/ingest.yml`:

```yaml
name: ingest

on:
  schedule:
    - cron: "0 */3 * * *"
  workflow_dispatch:

# Ingest and digest both write data/. Queue rather than race.
concurrency:
  group: data-write
  cancel-in-progress: false

permissions:
  contents: write

jobs:
  ingest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: pip

      - run: pip install -r requirements.txt

      - name: Fetch sources into the pool
        run: python -m ingest.run

      - name: Commit the pool
        run: |
          git config user.name "tldr-bot"
          git config user.email "tldr-bot@users.noreply.github.com"
          git add data/
          git diff --staged --quiet && echo "no changes" && exit 0
          git commit -m "chore: ingest $(date -u +%Y-%m-%dT%H:%MZ)"
          git pull --rebase
          git push
```

- [ ] **Step 2: Write the README**

`README.md`:

```markdown
# tldrcreator

A daily AI-news curator. Collects from Hacker News, arXiv, GitHub and AI company
blogs; a Claude agent ranks and drafts the best 6-8 stories; the result goes to a
Telegram channel and a static site.

Selection stays human. The system raises recall and removes blank-page cost, and
learns which stories are worth surfacing from emoji-reaction feedback.

## How it runs

| Workflow | Cadence | What it does |
|---|---|---|
| `ingest.yml` | every 3h | Fetch sources, dedupe into `data/pool.jsonl`, collect Telegram reactions |
| `digest.yml` | daily 07:00 UTC | Judge agent ranks, Writer agent drafts, send to Telegram, publish `docs/` |

## Local use

```bash
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt
.venv/Scripts/python -m ingest.run --smoke   # check every source is alive
.venv/Scripts/python -m ingest.run           # fetch into data/pool.jsonl
.venv/Scripts/python -m pytest -q
```

## Layout

- `store/` — item model, pool, labels, digests, schema validation
- `ingest/` — one module per source, plus `feeds.txt` (the blog list; edit this, not code)
- `send/` — Telegram delivery and static-site publication
- `.claude/skills/` — the Judge, Writer and relearn agent prompts
- `taste/profile.md` — what counts as a good story. Hand-edit the `## Mine` half freely.

## Design

`docs/superpowers/specs/2026-09-21-tldr-curator-design.md`
```

- [ ] **Step 3: Commit and push, then trigger a run**

```bash
git add .github/workflows/ingest.yml README.md
git commit -m "ci: ingest workflow on a 3h cron"
git push -u origin main
```

Then trigger it manually from the Actions tab (`workflow_dispatch`) rather than waiting for
the cron.

- [ ] **Step 4: Verify the workflow succeeded**

Confirm in the Actions tab that the run is green and that it produced a `chore: ingest ...`
commit touching `data/pool.jsonl`. If the push step failed on permissions, check that
Settings → Actions → General → Workflow permissions is set to "Read and write".

- [ ] **Step 5: PHASE 1 GATE — let it run, then read the pool**

Leave it running for three days. Then read `data/pool.jsonl` and answer one question: **are
the stories you would have picked actually in there?**

If they are not, the sources are wrong, and no amount of ranking fixes that — go back and
add or adjust sources in `ingest/feeds.txt` and `ingest/sources/` before continuing. Recall
precedes ranking; an absent story cannot be ranked.

---

### Task 8: Telegram delivery and the recency baseline

Deliberately ships **without** Claude. This creates the daily habit, the feedback surface,
and a dumb baseline the Judge must later beat.

**Files:**
- Create: `send/__init__.py`
- Create: `send/telegram.py`
- Create: `store/digests.py`
- Create: `send/baseline.py`
- Test: `tests/test_digests.py`

**Interfaces:**
- Consumes: `store.pool`, `store.item.Item`
- Produces:
  - `send.telegram.send_message(text: str, token: str, chat_id: str) -> int` — returns `message_id`
  - `send.telegram.api(method: str, token: str, params: dict) -> dict`
  - `store.digests.digest_path(date: str) -> Path`
  - `store.digests.save_digest(digest: dict, date: str) -> None`
  - `store.digests.load_digest(date: str) -> dict | None`
  - `store.digests.recent_digests(days: int = 7) -> list[dict]`
  - Digest dict shape: `{"date": str, "sent": bool, "items": [{"id", "title", "url", "source", "tier", "summary", "message_id"}]}`

- [ ] **Step 1: Set up the bot and channel**

Do this by hand, once:

1. Message **@BotFather** on Telegram, send `/newbot`, and save the token.
2. Create a **private channel**, then add the bot as an **administrator** with post rights.
3. Post any message in the channel, then read the channel id:
   ```bash
   curl "https://api.telegram.org/bot<TOKEN>/getUpdates"
   ```
   The channel id looks like `-1001234567890`.
4. Add both as GitHub Actions secrets: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`.

- [ ] **Step 2: Write the failing test**

`tests/test_digests.py`:

```python
from store import digests


def test_save_and_load_round_trip(tmp_path, monkeypatch):
    monkeypatch.setattr(digests, "DIGEST_DIR", tmp_path)
    payload = {
        "date": "2026-09-21",
        "sent": True,
        "items": [
            {
                "id": "a3f9c21b4e07",
                "title": "T",
                "url": "https://example.com/a",
                "source": "hn",
                "tier": "headline",
                "summary": "S",
                "message_id": 42,
            }
        ],
    }
    digests.save_digest(payload, "2026-09-21")
    assert digests.load_digest("2026-09-21") == payload


def test_load_returns_none_when_absent(tmp_path, monkeypatch):
    monkeypatch.setattr(digests, "DIGEST_DIR", tmp_path)
    assert digests.load_digest("2026-01-01") is None


def test_recent_digests_are_newest_first(tmp_path, monkeypatch):
    monkeypatch.setattr(digests, "DIGEST_DIR", tmp_path)
    for date in ["2026-09-19", "2026-09-20", "2026-09-21"]:
        digests.save_digest({"date": date, "sent": True, "items": []}, date)
    assert [d["date"] for d in digests.recent_digests(2)] == ["2026-09-21", "2026-09-20"]
```

- [ ] **Step 3: Run the test to verify it fails**

```bash
.venv/Scripts/python -m pytest tests/test_digests.py -v
```

Expected: FAIL with `ImportError: cannot import name 'digests'`

- [ ] **Step 4: Write the implementation**

`store/digests.py`:

```python
"""Per-day digest records: what was sent, and which Telegram message carries it."""

from __future__ import annotations

import json
from pathlib import Path

DIGEST_DIR = Path("data/digests")


def digest_path(date: str) -> Path:
    return DIGEST_DIR / f"{date}.json"


def save_digest(digest: dict, date: str) -> None:
    DIGEST_DIR.mkdir(parents=True, exist_ok=True)
    digest_path(date).write_text(
        json.dumps(digest, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def load_digest(date: str) -> dict | None:
    path = digest_path(date)
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def recent_digests(days: int = 7) -> list[dict]:
    if not DIGEST_DIR.exists():
        return []
    paths = sorted(DIGEST_DIR.glob("*.json"), reverse=True)[:days]
    return [json.loads(p.read_text(encoding="utf-8")) for p in paths]
```

Create empty `send/__init__.py`.

`send/telegram.py`:

```python
"""Telegram Bot API. stdlib only."""

from __future__ import annotations

import json
import urllib.parse
import urllib.request

BASE = "https://api.telegram.org/bot{token}/{method}"


def api(method: str, token: str, params: dict) -> dict:
    url = BASE.format(token=token, method=method)
    data = urllib.parse.urlencode(
        {k: (json.dumps(v) if isinstance(v, (list, dict)) else v)
         for k, v in params.items()}
    ).encode("utf-8")
    with urllib.request.urlopen(urllib.request.Request(url, data=data), timeout=30) as r:
        payload = json.loads(r.read().decode("utf-8"))
    if not payload.get("ok"):
        raise RuntimeError(f"telegram {method} failed: {payload}")
    return payload["result"]


def send_message(text: str, token: str, chat_id: str) -> int:
    result = api(
        "sendMessage",
        token,
        {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": "true",
        },
    )
    return result["message_id"]
```

`send/baseline.py`:

```python
"""Phase 2 baseline: send the 20 most recent unsent pool items, no ranking.

Exists to create the daily habit, the feedback surface, and a baseline the
Judge agent has to beat. Deleted once Task 12 lands.
"""

from __future__ import annotations

import html
import os
import time
from datetime import datetime, timezone

from send.telegram import send_message
from store import digests, pool


def main() -> int:
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    existing = digests.load_digest(date)
    if existing and existing.get("sent"):
        print(f"{date} already sent; nothing to do")
        return 0

    items = pool.load_pool()
    candidates = sorted(
        pool.unsent_since(items, hours=36), key=lambda i: i.first_seen, reverse=True
    )[:20]
    if not candidates:
        print("nothing to send")
        return 0

    send_message(
        f"<b>Baseline digest — {date}</b>\n{len(candidates)} most recent, unranked.",
        token,
        chat_id,
    )

    records = []
    for item in candidates:
        text = (
            f"<b>{html.escape(item.title)}</b>\n"
            f"{html.escape(item.source)} · <a href=\"{html.escape(item.url)}\">link</a>"
        )
        message_id = send_message(text, token, chat_id)
        records.append(
            {
                "id": item.id,
                "title": item.title,
                "url": item.url,
                "source": item.source,
                "tier": "baseline",
                "summary": "",
                "message_id": message_id,
            }
        )
        time.sleep(0.5)  # stay well inside Telegram's rate limit

    digests.save_digest({"date": date, "sent": True, "items": records}, date)
    pool.save_pool(pool.mark_sent(items, [r["id"] for r in records], date))
    print(f"sent {len(records)} items")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 5: Run the test to verify it passes**

```bash
.venv/Scripts/python -m pytest tests/test_digests.py -v
```

Expected: PASS, 3 tests

- [ ] **Step 6: Send a real digest to the channel**

```bash
TELEGRAM_BOT_TOKEN=<token> TELEGRAM_CHAT_ID=<chat_id> .venv/Scripts/python -m send.baseline
```

Expected: a header plus up to 20 messages in the channel, and a new `data/digests/<today>.json`
where every item has a `message_id`.

- [ ] **Step 7: Commit**

```bash
git add send store/digests.py tests/test_digests.py data/
git commit -m "feat: telegram delivery and recency baseline"
```

---

### Task 9: Reaction collection

Reactions are attributed to items through the `message_id` recorded in each digest. Items
that receive no reaction within 24 hours are recorded as a weak negative — that is most of
the data, and discarding it would throw away the majority of the signal.

**Files:**
- Create: `store/labels.py`
- Modify: `send/telegram.py` (add `get_updates`)
- Modify: `ingest/run.py` (drain reactions at the end of `main`)
- Test: `tests/test_labels.py`

**Interfaces:**
- Consumes: `store.digests.recent_digests`, `store.digests.load_digest`, `store.digests.save_digest`
- Produces:
  - `send.telegram.get_updates(token: str, offset: int, allowed: list[str] | None = None) -> list[dict]`
  - `store.labels.append_labels(rows: list[dict]) -> None`
  - `store.labels.load_labels() -> list[dict]`
  - `store.labels.recent_labels(n: int = 20) -> list[dict]`
  - `store.labels.reactions_to_labels(updates: list[dict], message_index: dict[int, dict]) -> list[dict]`
  - `store.labels.build_message_index(digests: list[dict]) -> dict[int, dict]`
  - `store.labels.mark_ignored(digest: dict) -> list[dict]`
  - `store.labels.LABELS_PATH`, `store.labels.OFFSET_PATH`, `store.labels.read_offset()`, `store.labels.write_offset(value: int)`
  - Verdict vocabulary: `up`, `down`, `published`, `ignored`

- [ ] **Step 1: Write the failing test**

`tests/test_labels.py`:

```python
from store import labels

DIGEST = {
    "date": "2026-09-21",
    "sent": True,
    "items": [
        {"id": "aaa111", "title": "A", "url": "https://x/a", "source": "hn",
         "tier": "headline", "summary": "", "message_id": 10},
        {"id": "bbb222", "title": "B", "url": "https://x/b", "source": "arxiv",
         "tier": "discovery", "summary": "", "message_id": 11},
    ],
}


def update(message_id: int, emoji: str) -> dict:
    return {
        "update_id": 500,
        "message_reaction": {
            "message_id": message_id,
            "date": 1758440000,
            "new_reaction": [{"type": "emoji", "emoji": emoji}],
        },
    }


def test_build_message_index_maps_message_id_to_item():
    index = labels.build_message_index([DIGEST])
    assert index[10]["id"] == "aaa111"
    assert index[11]["digest_date"] == "2026-09-21"


def test_thumbs_up_becomes_an_up_verdict():
    rows = labels.reactions_to_labels([update(10, "👍")], labels.build_message_index([DIGEST]))
    assert len(rows) == 1
    assert rows[0]["verdict"] == "up"
    assert rows[0]["item_id"] == "aaa111"
    assert rows[0]["tier"] == "headline"


def test_thumbs_down_becomes_a_down_verdict():
    rows = labels.reactions_to_labels([update(11, "👎")], labels.build_message_index([DIGEST]))
    assert rows[0]["verdict"] == "down"


def test_writing_hand_becomes_a_published_verdict():
    rows = labels.reactions_to_labels([update(10, "✍")], labels.build_message_index([DIGEST]))
    assert rows[0]["verdict"] == "published"


def test_unknown_emoji_is_ignored():
    rows = labels.reactions_to_labels([update(10, "🎉")], labels.build_message_index([DIGEST]))
    assert rows == []


def test_reaction_on_an_unknown_message_is_ignored():
    rows = labels.reactions_to_labels([update(999, "👍")], labels.build_message_index([DIGEST]))
    assert rows == []


def test_cleared_reaction_produces_no_row():
    cleared = {"update_id": 501, "message_reaction": {"message_id": 10, "new_reaction": []}}
    rows = labels.reactions_to_labels([cleared], labels.build_message_index([DIGEST]))
    assert rows == []


def test_mark_ignored_covers_items_with_no_existing_label(tmp_path, monkeypatch):
    monkeypatch.setattr(labels, "LABELS_PATH", tmp_path / "labels.jsonl")
    labels.append_labels([{"item_id": "aaa111", "verdict": "up", "digest_date": "2026-09-21"}])
    rows = labels.mark_ignored(DIGEST)
    assert [r["item_id"] for r in rows] == ["bbb222"]
    assert rows[0]["verdict"] == "ignored"


def test_append_and_load_round_trip(tmp_path, monkeypatch):
    monkeypatch.setattr(labels, "LABELS_PATH", tmp_path / "labels.jsonl")
    labels.append_labels([{"item_id": "x", "verdict": "up"}])
    labels.append_labels([{"item_id": "y", "verdict": "down"}])
    assert [r["item_id"] for r in labels.load_labels()] == ["x", "y"]


def test_recent_labels_returns_the_tail(tmp_path, monkeypatch):
    monkeypatch.setattr(labels, "LABELS_PATH", tmp_path / "labels.jsonl")
    labels.append_labels([{"item_id": str(i), "verdict": "up"} for i in range(30)])
    assert len(labels.recent_labels(20)) == 20
    assert labels.recent_labels(20)[-1]["item_id"] == "29"
```

- [ ] **Step 2: Run the test to verify it fails**

```bash
.venv/Scripts/python -m pytest tests/test_labels.py -v
```

Expected: FAIL with `ImportError: cannot import name 'labels'`

- [ ] **Step 3: Write the labels store**

`store/labels.py`:

```python
"""Feedback labels, append-only."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

LABELS_PATH = Path("data/labels.jsonl")
OFFSET_PATH = Path("data/tg_offset.txt")

# Emoji vocabulary. Telegram sends the writing hand with and without VS16.
VERDICTS = {
    "👍": "up",
    "👎": "down",
    "✍": "published",
    "✍️": "published",
}


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_labels() -> list[dict]:
    if not LABELS_PATH.exists():
        return []
    return [
        json.loads(line)
        for line in LABELS_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def append_labels(rows: list[dict]) -> None:
    if not rows:
        return
    LABELS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LABELS_PATH.open("a", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def recent_labels(n: int = 20) -> list[dict]:
    return load_labels()[-n:]


def read_offset() -> int:
    if not OFFSET_PATH.exists():
        return 0
    return int(OFFSET_PATH.read_text(encoding="utf-8").strip() or 0)


def write_offset(value: int) -> None:
    OFFSET_PATH.parent.mkdir(parents=True, exist_ok=True)
    OFFSET_PATH.write_text(str(value), encoding="utf-8")


def build_message_index(digest_list: list[dict]) -> dict[int, dict]:
    """message_id -> the item it carries, stamped with its digest date."""
    index: dict[int, dict] = {}
    for digest in digest_list:
        for item in digest.get("items", []):
            message_id = item.get("message_id")
            if message_id is None:
                continue
            index[message_id] = {**item, "digest_date": digest["date"]}
    return index


def reactions_to_labels(
    updates: list[dict], message_index: dict[int, dict]
) -> list[dict]:
    rows: list[dict] = []
    for update in updates:
        reaction = update.get("message_reaction")
        if not reaction:
            continue
        item = message_index.get(reaction.get("message_id"))
        if item is None:
            continue
        for entry in reaction.get("new_reaction", []):
            verdict = VERDICTS.get(entry.get("emoji", ""))
            if verdict is None:
                continue
            rows.append(
                {
                    "ts": _now(),
                    "digest_date": item["digest_date"],
                    "item_id": item["id"],
                    "url": item["url"],
                    "title": item["title"],
                    "tier": item["tier"],
                    "source": item["source"],
                    "verdict": verdict,
                }
            )
    return rows


def mark_ignored(digest: dict) -> list[dict]:
    """Every item in `digest` with no label yet becomes a weak negative."""
    labelled = {row["item_id"] for row in load_labels()}
    return [
        {
            "ts": _now(),
            "digest_date": digest["date"],
            "item_id": item["id"],
            "url": item["url"],
            "title": item["title"],
            "tier": item["tier"],
            "source": item["source"],
            "verdict": "ignored",
        }
        for item in digest.get("items", [])
        if item["id"] not in labelled
    ]
```

- [ ] **Step 4: Run the test to verify it passes**

```bash
.venv/Scripts/python -m pytest tests/test_labels.py -v
```

Expected: PASS, 10 tests

- [ ] **Step 5: Add `get_updates` to the Telegram client**

Append to `send/telegram.py`:

```python
def get_updates(token: str, offset: int, allowed: list[str] | None = None) -> list[dict]:
    """Drain pending updates. Reactions require message_reaction in allowed_updates."""
    return api(
        "getUpdates",
        token,
        {
            "offset": offset,
            "timeout": 0,
            "allowed_updates": allowed or ["message_reaction"],
        },
    )
```

- [ ] **Step 6: Drain reactions from the ingest runner**

Add to `ingest/run.py`, above `main`:

```python
import os

from send.telegram import get_updates
from store import digests, labels


def collect_feedback() -> int:
    """Sole consumer of getUpdates — a second consumer would race the offset."""
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        print("[feedback] no token, skipping")
        return 0
    try:
        updates = get_updates(token, labels.read_offset())
    except Exception as exc:
        print(f"[feedback] FAILED: {exc}", file=sys.stderr)
        return 0
    if not updates:
        return 0

    index = labels.build_message_index(digests.recent_digests(7))
    rows = labels.reactions_to_labels(updates, index)
    labels.append_labels(rows)
    labels.write_offset(max(u["update_id"] for u in updates) + 1)
    print(f"[feedback] {len(rows)} labels from {len(updates)} updates")
    return len(rows)
```

And call it in `main`, immediately before `pool.save_pool(kept)`:

```python
    collect_feedback()
```

- [ ] **Step 7: Verify reactions actually arrive**

This is the one open risk in the design. React 👍 to a message the baseline posted, then:

```bash
TELEGRAM_BOT_TOKEN=<token> .venv/Scripts/python -c "from send.telegram import get_updates; print(get_updates('<token>', 0))"
```

Expected: an update containing `message_reaction`.

If the list is empty, the bot is not receiving channel reactions. Confirm it is a channel
**administrator**. If it still does not work, fall back to inline `👍`/`👎` buttons:
add `reply_markup` with `callback_data` of `"{item_id}:{up|down}"` in `send/baseline.py`,
read `callback_query` instead of `message_reaction` here, and accept the delayed
acknowledgement. Do not proceed past this step with feedback unverified — every later phase
depends on labels accumulating.

- [ ] **Step 8: Commit**

```bash
git add store/labels.py send/telegram.py ingest/run.py tests/test_labels.py
git commit -m "feat: collect telegram reactions as feedback labels"
```

---

### Task 10: The digest workflow and failure alerting

Adds the second cron, still running the baseline sender. The failure alert matters more than
it looks: without it, an expired OAuth token means digests silently stop and nobody notices
for days.

**Files:**
- Create: `.github/workflows/digest.yml`
- Create: `send/alert.py`
- Create: `send/close_yesterday.py`

**Interfaces:**
- Consumes: `send.telegram.send_message`, `store.labels.mark_ignored`, `store.digests.recent_digests`
- Produces:
  - `send.alert.main() -> int` — reads `RUN_URL` from env and posts a failure notice
  - `send.close_yesterday.main() -> int` — writes `ignored` labels for the previous digest

- [ ] **Step 1: Write the alert and close-out scripts**

`send/alert.py`:

```python
"""Posted by the workflow's failure branch, so a dead job is visible."""

from __future__ import annotations

import os

from send.telegram import send_message


def main() -> int:
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    run_url = os.environ.get("RUN_URL", "(no run url)")
    send_message(
        f"⚠️ <b>digest failed</b>\nNo digest today.\n<a href=\"{run_url}\">run log</a>",
        token,
        chat_id,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`send/close_yesterday.py`:

```python
"""Anything in the previous digest with no reaction becomes a weak negative."""

from __future__ import annotations

from store import digests, labels


def main() -> int:
    recent = digests.recent_digests(2)
    previous = next((d for d in recent if d.get("sent")), None)
    if previous is None:
        print("no previous digest to close")
        return 0
    rows = labels.mark_ignored(previous)
    labels.append_labels(rows)
    print(f"closed {previous['date']}: {len(rows)} ignored")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: Write the workflow**

`.github/workflows/digest.yml`:

```yaml
name: digest

on:
  schedule:
    - cron: "0 7 * * *"
  workflow_dispatch:

concurrency:
  group: data-write
  cancel-in-progress: false

permissions:
  contents: write

jobs:
  digest:
    runs-on: ubuntu-latest
    env:
      TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
      TELEGRAM_CHAT_ID: ${{ secrets.TELEGRAM_CHAT_ID }}
    steps:
      - uses: actions/checkout@v6

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: pip

      - run: pip install -r requirements.txt

      - name: Close out yesterday's digest
        run: python -m send.close_yesterday

      - name: Send the digest
        run: python -m send.baseline

      - name: Commit
        run: |
          git config user.name "tldr-bot"
          git config user.email "tldr-bot@users.noreply.github.com"
          git add data/ docs/
          git diff --staged --quiet && echo "no changes" && exit 0
          git commit -m "chore: digest $(date -u +%Y-%m-%d)"
          git pull --rebase
          git push

      - name: Report failure to Telegram
        if: failure()
        env:
          RUN_URL: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}
        run: python -m send.alert
```

- [ ] **Step 3: Commit and push**

```bash
git add .github/workflows/digest.yml send/alert.py send/close_yesterday.py
git commit -m "ci: digest workflow with failure alerting"
git push
```

- [ ] **Step 4: Verify both paths**

Trigger `digest` manually from the Actions tab. Expected: green run, messages in the channel,
a `chore: digest ...` commit.

Then verify the alert path — temporarily change the "Send the digest" step's command to
`python -c "raise SystemExit(1)"`, push, run it manually, confirm the ⚠️ message arrives, then
revert that change and push again.

- [ ] **Step 5: PHASE 2 GATE — live with it for a week**

React to the messages daily. The point is to accumulate labels against the dumb baseline
before the Judge exists, so there is something to compare it against. Confirm
`data/labels.jsonl` is growing and that `ignored` rows appear the day after each digest.

---

### Task 11: Taste profile, Judge agent, and output validation

The validator is the safety gate — a malformed Judge run must fail the job rather than reach
the channel. It is written and tested first, before the agent that produces the file.

**Files:**
- Create: `taste/profile.md`
- Create: `taste/voice.md`
- Create: `store/ranked.py`
- Create: `.claude/skills/judge/SKILL.md`
- Create: `agents/prepare_judge.py`
- Test: `tests/test_ranked.py`

**Interfaces:**
- Consumes: `store.pool.unsent_since`, `store.labels.recent_labels`, `store.digests.recent_digests`
- Produces:
  - `store.ranked.RANKED_PATH` — `Path("data/ranked.json")`
  - `store.ranked.validate_ranked(payload: dict, pool_ids: set[str]) -> None` — raises `store.ranked.ValidationError`
  - `store.ranked.load_ranked(pool_ids: set[str]) -> dict` — loads and validates
  - `store.ranked.top(payload: dict, n: int = 8, exclude_ids: frozenset[str] = frozenset()) -> list[dict]`
  - `store.ranked.unpublishable_ids(items: list[Item]) -> frozenset[str]` — pool ids whose `meta["kind"]` is `"discussion"`
  - `agents.prepare_judge.main() -> int` — writes `data/judge_input.json`

- [ ] **Step 1: Write the taste files**

`taste/profile.md` — replace the example bullets with real preferences:

```markdown
# Taste profile

## Mine (authoritative — never auto-edited)

Always surface:
- Inference infrastructure: serving, quantization, KV-cache, throughput
- Evaluation methodology, especially new benchmarks and benchmark criticism
- Open-weight model releases with published weights

Never surface:
- Funding rounds under $50M
- Crypto, unless it is a genuine AI systems result
- "X is dead" / "the end of Y" takes
- Model rumors with no primary source
- Conference and webinar announcements

Weighting notes:
- I care more about how models are served than how they are trained
- A repo with running code beats a paper describing the same idea
- If it is already at 1000+ points on HN, I have seen it — surface it as a
  headline, briefly, and spend the slots on things I have not seen

## Learned (regenerated weekly from labels — edit freely, it will be overwritten)

_No data yet._
```

`taste/voice.md`:

```markdown
# Writing voice

Each summary is 2-3 sentences, 40-60 words.

Rules:
- Lead with what changed, never with who announced it.
  Not: "OpenAI has announced a new model that..."
  Yes: "GPT-5.5 runs 40% cheaper per token, with the same benchmark scores."
- Numbers instead of adjectives. "3.1x throughput", not "dramatically faster".
- Banned words: revolutionary, game-changing, groundbreaking, breakthrough,
  seamless, cutting-edge, unprecedented.
- Assume the reader knows what a transformer, a benchmark, and quantization are.
  Do not define terms.
- No editorializing and no hedging. If it is hype, the Judge should have cut it.
- End with the concrete takeaway: what someone could now do that they could not
  do yesterday.
- Close with reading time in parentheses: "(4 minute read)".
```

- [ ] **Step 2: Write the failing validator test**

`tests/test_ranked.py`:

```python
import pytest

from store import ranked
from store.item import make_item

POOL_IDS = {"aaa111", "bbb222"}


def payload(**overrides):
    base = {
        "generated_at": "2026-09-21T07:02:11Z",
        "pool_size": 2,
        "read_count": 1,
        "items": [
            {
                "id": "aaa111", "url": "https://x/a", "title": "A", "source": "hn",
                "tier": "headline", "score": 9.0, "saturation": 0.9,
                "reason": "Big release.", "read": True,
                "key_facts": ["ships today"], "dedupe_of": None,
            },
            {
                "id": "bbb222", "url": "https://x/b", "title": "B", "source": "arxiv",
                "tier": "discovery", "score": 4.0, "saturation": 0.1,
                "reason": "Incremental, no code.", "read": False,
                "key_facts": [], "dedupe_of": None,
            },
        ],
    }
    base.update(overrides)
    return base


def test_valid_payload_passes():
    ranked.validate_ranked(payload(), POOL_IDS)


def test_missing_items_key_is_rejected():
    with pytest.raises(ranked.ValidationError, match="items"):
        ranked.validate_ranked({"generated_at": "x"}, POOL_IDS)


def test_unknown_id_is_rejected():
    bad = payload()
    bad["items"][0]["id"] = "ghost9"
    with pytest.raises(ranked.ValidationError, match="not in pool"):
        ranked.validate_ranked(bad, POOL_IDS)


def test_duplicate_ids_are_rejected():
    bad = payload()
    bad["items"][1]["id"] = "aaa111"
    with pytest.raises(ranked.ValidationError, match="duplicate"):
        ranked.validate_ranked(bad, POOL_IDS)


def test_out_of_range_score_is_rejected():
    bad = payload()
    bad["items"][0]["score"] = 42
    with pytest.raises(ranked.ValidationError, match="score"):
        ranked.validate_ranked(bad, POOL_IDS)


def test_bad_tier_is_rejected():
    bad = payload()
    bad["items"][0]["tier"] = "amazing"
    with pytest.raises(ranked.ValidationError, match="tier"):
        ranked.validate_ranked(bad, POOL_IDS)


def test_missing_reason_is_rejected():
    bad = payload()
    bad["items"][0]["reason"] = ""
    with pytest.raises(ranked.ValidationError, match="reason"):
        ranked.validate_ranked(bad, POOL_IDS)


def test_top_returns_highest_scores_first():
    assert [i["id"] for i in ranked.top(payload(), 2)] == ["aaa111", "bbb222"]


def test_top_caps_the_count():
    assert len(ranked.top(payload(), 1)) == 1


def test_top_skips_excluded_ids_however_high_they_score():
    out = ranked.top(payload(), 2, exclude_ids=frozenset({"aaa111"}))
    assert [i["id"] for i in out] == ["bbb222"]


def test_unpublishable_ids_selects_only_discussions():
    article = make_item(
        url="https://x/a", title="A", source="hn", meta={"kind": "article"}
    )
    thread = make_item(
        url="https://news.ycombinator.com/item?id=1",
        title="Ask HN: something",
        source="hn",
        meta={"kind": "discussion"},
    )
    # Sources other than HN set no "kind" at all; absence must not exclude them.
    paper = make_item(url="https://arxiv.org/abs/2509.1", title="P", source="arxiv")
    assert ranked.unpublishable_ids([article, thread, paper]) == frozenset({thread.id})
```

- [ ] **Step 3: Run the test to verify it fails**

```bash
.venv/Scripts/python -m pytest tests/test_ranked.py -v
```

Expected: FAIL with `ImportError: cannot import name 'ranked'`

- [ ] **Step 4: Write the validator**

`store/ranked.py`:

```python
"""Validation gate for Judge output. Nothing is sent unless this passes."""

from __future__ import annotations

import json
from pathlib import Path

RANKED_PATH = Path("data/ranked.json")
TIERS = {"headline", "discovery"}
REQUIRED = ("id", "url", "title", "source", "tier", "score", "saturation", "reason", "read")


class ValidationError(Exception):
    pass


def validate_ranked(payload: dict, pool_ids: set[str]) -> None:
    items = payload.get("items")
    if not isinstance(items, list) or not items:
        raise ValidationError("payload has no non-empty 'items' list")

    seen: set[str] = set()
    for index, item in enumerate(items):
        where = f"items[{index}]"
        missing = [key for key in REQUIRED if key not in item]
        if missing:
            raise ValidationError(f"{where} missing keys: {missing}")
        if item["id"] in seen:
            raise ValidationError(f"{where} duplicate id {item['id']}")
        seen.add(item["id"])
        if item["id"] not in pool_ids:
            raise ValidationError(f"{where} id {item['id']} not in pool")
        if item["tier"] not in TIERS:
            raise ValidationError(f"{where} bad tier {item['tier']!r}")
        if not isinstance(item["score"], (int, float)) or not 0 <= item["score"] <= 10:
            raise ValidationError(f"{where} score out of range: {item['score']!r}")
        if not isinstance(item["saturation"], (int, float)) or not 0 <= item["saturation"] <= 1:
            raise ValidationError(f"{where} saturation out of range")
        if not str(item.get("reason", "")).strip():
            raise ValidationError(f"{where} has an empty reason")


def load_ranked(pool_ids: set[str], path: Path = RANKED_PATH) -> dict:
    if not path.exists():
        raise ValidationError(f"{path} was not produced")
    payload = json.loads(path.read_text(encoding="utf-8"))
    validate_ranked(payload, pool_ids)
    return payload


def unpublishable_ids(items) -> frozenset[str]:
    """Pool items that must never reach a digest.

    A TLDR item links to something readable. An HN text post is a discussion
    thread, not an artifact — worth keeping in the pool as research signal, and
    worth showing in the site's tail, but never publishable.
    """
    return frozenset(i.id for i in items if i.meta.get("kind") == "discussion")


def top(
    payload: dict, n: int = 8, exclude_ids: frozenset[str] = frozenset()
) -> list[dict]:
    """Highest scores first, minus anything unpublishable.

    `exclude_ids` is derived from the pool, which only Python writes. So the
    Judge cannot promote a discussion thread into the digest even if it scores
    it 10 — the rule is enforced here rather than hoped for in a prompt.
    """
    eligible = [i for i in payload["items"] if i["id"] not in exclude_ids]
    return sorted(eligible, key=lambda i: i["score"], reverse=True)[:n]
```

- [ ] **Step 5: Run the test to verify it passes**

```bash
.venv/Scripts/python -m pytest tests/test_ranked.py -v
```

Expected: PASS, 11 tests

- [ ] **Step 6: Write the Judge input preparer**

Gathering inputs in Python keeps the agent's job small and its context clean.

`agents/prepare_judge.py` (create an empty `agents/__init__.py` alongside it):

```python
"""Assemble everything the Judge needs into one file."""

from __future__ import annotations

import json
from pathlib import Path

from store import digests, labels, pool

INPUT_PATH = Path("data/judge_input.json")


def main() -> int:
    candidates = pool.unsent_since(pool.load_pool(), hours=36)
    payload = {
        "candidates": [
            {
                "id": i.id, "url": i.url, "title": i.title, "source": i.source,
                "first_seen": i.first_seen, "text": i.text[:1500], "meta": i.meta,
            }
            for i in candidates
        ],
        "recent_labels": labels.recent_labels(20),
        "recently_sent_titles": [
            item["title"] for digest in digests.recent_digests(7)
            for item in digest.get("items", [])
        ],
    }
    INPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    INPUT_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"judge input: {len(payload['candidates'])} candidates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 7: Write the Judge skill**

`.claude/skills/judge/SKILL.md`:

```markdown
---
name: judge
description: Score today's candidate pool and write data/ranked.json
allowed-tools: Read, Write, WebFetch, Grep
---

# Judge

Score every candidate in `data/judge_input.json` and write `data/ranked.json`.

## Read first

1. `data/judge_input.json` — `candidates`, `recent_labels`, `recently_sent_titles`
2. `taste/profile.md` — both halves. The `## Mine` half is authoritative and
   overrides anything you infer.

`recent_labels` are the operator's verdicts on recent picks: `up` (good pick),
`down` (should not have been surfaced), `published` (strongest positive — they
actually used it), `ignored` (weak negative). Treat them as worked examples of
the operator's taste, not as rules.

## Method

1. Triage all candidates on title, source and metadata alone.
2. Choose 12-15 that look non-obvious or consequential and **fetch and read them**.
   Do not exceed 20 fetches. Ranking on titles alone is the failure mode this
   whole step exists to avoid.
3. Score every candidate, read or not.

**Discussion threads.** A candidate whose `meta.kind` is `"discussion"` is an HN text post —
an Ask HN or Tell HN thread. It has no article behind it, so it can never be a digest item:
a TLDR entry links to something readable. Do not spend fetches trying to rank one for
selection. They are still worth skimming, because a thread often names the paper or repo that
*is* the story — if you find one, look for it among the other candidates and let that finding
raise its score. Score discussion threads normally; the selection step filters them out, so
your score for them only affects the site's tail.

## Scoring

Two tiers, and the distinction matters:

- `headline` — big enough that not knowing it is a gap. Usually already
  saturated. Target about 3 per day.
- `discovery` — high signal, low saturation. The thing the operator would have
  found at 11pm if they kept scrolling. Target about 5 per day.

`saturation` (0-1) estimates how likely the operator has already seen it. A
2000-point HN post is ~0.95. A 14-hour-old arXiv paper with no traction is ~0.1.
**High saturation lowers a `discovery` score but does not lower a `headline`
score** — that is the whole point of having two tiers.

`score` (0-10) weighs:
- Does this change what a working engineer or researcher would do?
- Is it new information, or a rehash? Check `recently_sent_titles` and
  `data/digests/` before scoring something highly.
- Is it verifiable — a paper, a repo, an official post — rather than a rumor?
- Running code beats a description of the same idea.

Set `dedupe_of` to another candidate's `id` when two entries cover the same news,
and score the duplicate low.

## Output

Write `data/ranked.json`. Every candidate gets an entry, including rejects.

{
  "generated_at": "<UTC ISO-8601 with Z>",
  "pool_size": <int>,
  "read_count": <int>,
  "items": [
    {
      "id": "<candidate id, unchanged>",
      "url": "<candidate url>",
      "title": "<candidate title>",
      "source": "<candidate source>",
      "tier": "headline" | "discovery",
      "score": <0-10>,
      "saturation": <0-1>,
      "reason": "<one line: why this matters, or why it does not>",
      "read": <true if you fetched it>,
      "key_facts": ["<concrete facts from the article>"],
      "dedupe_of": <id or null>
    }
  ]
}

`reason` is required on **every** item, rejects included — it is what makes a bad
day debuggable. `key_facts` is how the Writer gets article content without
re-fetching, so fill it for everything you read: concrete, numeric, no adjectives.

Write the file and stop. Do not send anything.
```

- [ ] **Step 8: Verify the Judge locally against the real pool**

```bash
.venv/Scripts/python -m agents.prepare_judge
claude "/judge"
.venv/Scripts/python -c "
from store import pool, ranked
items = pool.load_pool()
payload = ranked.load_ranked({i.id for i in items})
blocked = ranked.unpublishable_ids(items)
print('valid:', len(payload['items']), 'items,', payload['read_count'], 'read')
print('unpublishable (discussion threads):', len(blocked))
for item in ranked.top(payload, 8, blocked):
    print(f\"{item['score']:>4}  {item['tier']:<9} {item['title'][:60]}\")
    print(f\"      {item['reason']}\")
"
```

Expected: validation passes and the top 8 look defensible. Compare them against what the
baseline was sending. If the picks are poor, tune `taste/profile.md` and
`.claude/skills/judge/SKILL.md` and re-run — this is the tuning loop.

- [ ] **Step 9: Save a golden day**

```bash
cp data/pool.jsonl tests/fixtures/golden_pool.jsonl
```

After any future change to the Judge prompt, re-run it against this file and read the picks.
Selection is a judgment task, so this is not an automated assertion — but it makes prompt
changes comparable instead of vibes-based.

- [ ] **Step 10: Commit**

```bash
git add taste/ store/ranked.py agents/ .claude/skills/judge/SKILL.md tests/test_ranked.py tests/fixtures/golden_pool.jsonl
git commit -m "feat: taste profile, judge agent, and ranked output validation"
```

---

### Task 12: Wire the Judge into the digest workflow

Replaces the recency baseline with ranked output. The Writer does not exist yet, so this
sends titles plus the Judge's `reason` — already a better digest than the baseline, and it
isolates any problem to the Judge before a second agent is added.

**Files:**
- Create: `send/digest.py`
- Modify: `.github/workflows/digest.yml`
- Delete: `send/baseline.py`

**Interfaces:**
- Consumes: `store.ranked.load_ranked`, `store.ranked.top`, `send.telegram.send_message`, `store.pool`, `store.digests`, `store.health.dead_sources`
- Produces: `send.digest.main() -> int`

- [ ] **Step 1: Write the digest sender**

`send/digest.py`:

```python
"""Send the ranked digest. Uses Writer summaries when present, reasons otherwise."""

from __future__ import annotations

import html
import os
import time
from datetime import datetime, timezone

from send.telegram import send_message
from store import digests, health, pool, ranked

TIER_LABEL = {"headline": "📰", "discovery": "🔍"}


def render(item: dict) -> str:
    # Judge items carry `reason`; Writer-drafted items carry `summary` and no
    # `reason`. Both shapes flow through here, so neither key is assumed.
    icon = TIER_LABEL.get(item["tier"], "•")
    body = item.get("summary") or item.get("reason", "")
    return (
        f"{icon} <b>{html.escape(item['title'])}</b>\n"
        f"{html.escape(body)}\n"
        f"{html.escape(item['source'])} · <a href=\"{html.escape(item['url'])}\">link</a>"
    )


def main() -> int:
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    existing = digests.load_digest(date)
    if existing and existing.get("sent"):
        print(f"{date} already sent; nothing to do")
        return 0

    items = pool.load_pool()
    payload = ranked.load_ranked({i.id for i in items})

    # Written by the Writer agent when it has run; falls back to Judge output.
    drafted = existing.get("items") if existing else None
    selected = drafted or ranked.top(payload, 8, ranked.unpublishable_ids(items))

    if not selected:
        print("nothing cleared the bar; sending nothing")
        return 0

    header = (
        f"<b>TLDR AI — {date}</b>\n"
        f"{len(selected)} of {payload['pool_size']} candidates · "
        f"{payload['read_count']} read in full"
    )
    dead = health.dead_sources(3)
    if dead:
        header += f"\n⚠️ no items from: {', '.join(dead)}"
    send_message(header, token, chat_id)

    records = []
    for item in selected:
        message_id = send_message(render(item), token, chat_id)
        records.append({**item, "message_id": message_id})
        time.sleep(0.5)

    digests.save_digest({"date": date, "sent": True, "items": records}, date)
    pool.save_pool(pool.mark_sent(items, [r["id"] for r in records], date))
    print(f"sent {len(records)} items")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: Update the workflow**

In `.github/workflows/digest.yml`, add `CLAUDE_CODE_OAUTH_TOKEN` handling and replace the
"Send the digest" step. The steps between "Close out yesterday's digest" and "Commit" become:

```yaml
      - name: Prepare judge input
        run: python -m agents.prepare_judge

      - name: Judge
        uses: anthropics/claude-code-action@v1
        with:
          claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
          prompt: "/judge"
          claude_args: |
            --max-turns 40
            --allowedTools "Read,Write,WebFetch,Grep"

      - name: Send the digest
        run: python -m send.digest
```

Also add `id-token: write` under `permissions:` in the job, alongside `contents: write`.

- [ ] **Step 3: Delete the baseline**

```bash
git rm send/baseline.py
```

Its job is done: it created the habit and the labels the Judge now trains against.

- [ ] **Step 4: Generate the OAuth token and add it as a secret**

```bash
claude setup-token
```

Add the printed token as the repository secret `CLAUDE_CODE_OAUTH_TOKEN`. It is long-lived
but expires; when it does, the digest job fails and the Task 10 alert is what tells you.

- [ ] **Step 5: Commit, push, and run**

```bash
git add send/digest.py .github/workflows/digest.yml
git commit -m "feat: judge-ranked digest replaces the recency baseline"
git push
```

Trigger `digest` manually. Expected: green run; the channel receives a header plus up to 8
ranked stories, each with the Judge's reason. Confirm `data/ranked.json` was committed.

- [ ] **Step 6: Verify the validation gate actually blocks**

```bash
echo '{"items": []}' > data/ranked.json
TELEGRAM_BOT_TOKEN=<token> TELEGRAM_CHAT_ID=<id> .venv/Scripts/python -m send.digest
```

Expected: a `ValidationError` and a non-zero exit — nothing sent. Then restore the real file
with `git checkout data/ranked.json`.

---

### Task 13: Writer agent

Drafts real summaries for the top 8 using the `key_facts` the Judge already gathered, so no
article is fetched twice.

**Files:**
- Create: `.claude/skills/writer/SKILL.md`
- Create: `agents/prepare_writer.py`
- Modify: `.github/workflows/digest.yml`
- Test: `tests/test_prepare_writer.py`

**Interfaces:**
- Consumes: `store.ranked.load_ranked`, `store.ranked.top`, `store.pool.load_pool`
- Produces:
  - `agents.prepare_writer.build(payload: dict, n: int = 8, exclude_ids: frozenset[str] = frozenset()) -> dict`
  - `agents.prepare_writer.main() -> int` — writes `data/writer_input.json`
  - Writer writes `data/digests/<today>.json` with `sent: false` and a `summary` on each item

- [ ] **Step 1: Write the failing test**

`tests/test_prepare_writer.py`:

```python
from agents import prepare_writer


def payload():
    return {
        "generated_at": "2026-09-21T07:00:00Z",
        "pool_size": 3,
        "read_count": 2,
        "items": [
            {"id": "a", "url": "https://x/a", "title": "A", "source": "hn",
             "tier": "headline", "score": 9.0, "saturation": 0.9, "reason": "r",
             "read": True, "key_facts": ["fact a"], "dedupe_of": None},
            {"id": "b", "url": "https://x/b", "title": "B", "source": "arxiv",
             "tier": "discovery", "score": 7.0, "saturation": 0.1, "reason": "r",
             "read": True, "key_facts": ["fact b"], "dedupe_of": None},
            {"id": "c", "url": "https://x/c", "title": "C", "source": "blog",
             "tier": "discovery", "score": 2.0, "saturation": 0.4, "reason": "r",
             "read": False, "key_facts": [], "dedupe_of": None},
        ],
    }


def test_build_takes_the_top_n_by_score():
    out = prepare_writer.build(payload(), n=2)
    assert [i["id"] for i in out["stories"]] == ["a", "b"]


def test_build_carries_key_facts_through():
    out = prepare_writer.build(payload(), n=2)
    assert out["stories"][0]["key_facts"] == ["fact a"]


def test_build_drops_scoring_internals():
    out = prepare_writer.build(payload(), n=1)
    assert "saturation" not in out["stories"][0]
    assert "score" not in out["stories"][0]


def test_build_sets_the_date():
    out = prepare_writer.build(payload(), n=1)
    assert len(out["date"]) == 10


def test_build_never_hands_the_writer_an_excluded_story():
    out = prepare_writer.build(payload(), n=2, exclude_ids=frozenset({"a"}))
    assert [i["id"] for i in out["stories"]] == ["b", "c"]
```

- [ ] **Step 2: Run the test to verify it fails**

```bash
.venv/Scripts/python -m pytest tests/test_prepare_writer.py -v
```

Expected: FAIL with `ImportError: cannot import name 'prepare_writer'`

- [ ] **Step 3: Write the implementation**

`agents/prepare_writer.py`:

```python
"""Hand the Writer only the top stories and the facts already gathered."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from store import pool, ranked

INPUT_PATH = Path("data/writer_input.json")
KEEP = ("id", "url", "title", "source", "tier", "reason", "key_facts")


def build(
    payload: dict, n: int = 8, exclude_ids: frozenset[str] = frozenset()
) -> dict:
    return {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "stories": [
            {key: story[key] for key in KEEP}
            for story in ranked.top(payload, n, exclude_ids)
        ],
    }


def main() -> int:
    items = pool.load_pool()
    payload = ranked.load_ranked({i.id for i in items})
    built = build(payload, exclude_ids=ranked.unpublishable_ids(items))
    INPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    INPUT_PATH.write_text(json.dumps(built, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"writer input: {len(built['stories'])} stories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the test to verify it passes**

```bash
.venv/Scripts/python -m pytest tests/test_prepare_writer.py -v
```

Expected: PASS, 5 tests

- [ ] **Step 5: Write the Writer skill**

`.claude/skills/writer/SKILL.md`:

```markdown
---
name: writer
description: Draft TLDR-style summaries for today's selected stories
allowed-tools: Read, Write
---

# Writer

Draft a summary for every story in `data/writer_input.json`.

## Read first

1. `data/writer_input.json` — `date` and `stories`, each with `key_facts`
   already extracted from the article by the Judge
2. `taste/voice.md` — the style rules. Follow them exactly.

Write from `key_facts` and `title`. Do not fetch anything: the facts were
gathered when the article was read, and re-fetching wastes turns.

If a story's `key_facts` is empty, write from the title and `reason` alone and
keep it to a single sentence rather than inventing detail. Never state a number
that is not in `key_facts`.

## Output

Write `data/digests/<date>.json`, using the `date` from the input:

{
  "date": "<date from input>",
  "sent": false,
  "items": [
    {
      "id": "<unchanged>",
      "title": "<rewritten headline, under 80 characters>",
      "url": "<unchanged>",
      "source": "<unchanged>",
      "tier": "<unchanged>",
      "summary": "<2-3 sentences per taste/voice.md, ending with reading time>"
    }
  ]
}

Keep `items` in the input's order. `sent` stays `false` — the sender sets it.
Write the file and stop. Do not send anything.
```

- [ ] **Step 6: Add the Writer to the workflow**

In `.github/workflows/digest.yml`, insert between the "Judge" step and "Send the digest":

```yaml
      - name: Prepare writer input
        run: python -m agents.prepare_writer

      - name: Writer
        uses: anthropics/claude-code-action@v1
        with:
          claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
          prompt: "/writer"
          claude_args: |
            --max-turns 10
            --allowedTools "Read,Write"
```

`send/digest.py` already prefers an existing digest file's items over raw Judge output, so no
change is needed there.

- [ ] **Step 7: Verify end to end locally**

```bash
.venv/Scripts/python -m agents.prepare_writer
claude "/writer"
.venv/Scripts/python -c "
from datetime import datetime, timezone
from store import digests
d = digests.load_digest(datetime.now(timezone.utc).strftime('%Y-%m-%d'))
for item in d['items']:
    print(f\"{item['tier']:<9} {item['title']}\")
    print(f\"  {item['summary']}\n\")
"
```

Expected: 8 drafted summaries that follow `taste/voice.md`. If the voice is off, edit
`taste/voice.md` — not the skill — and re-run.

- [ ] **Step 8: Commit, push, and run the full pipeline**

```bash
git add .claude/skills/writer/SKILL.md agents/prepare_writer.py .github/workflows/digest.yml tests/test_prepare_writer.py
git commit -m "feat: writer agent drafts the digest summaries"
git push
```

Trigger `digest` manually and confirm the channel receives 8 written summaries.

---

### Task 14: Static site and RSS

Publishes the archive and the long tail the Telegram digest deliberately omits. RSS is how
the "email" requirement is met without building email.

**Files:**
- Create: `send/publish.py`
- Modify: `.github/workflows/digest.yml`
- Test: `tests/test_publish.py`

**Interfaces:**
- Consumes: `store.digests.recent_digests`, `store.ranked.load_ranked`, `store.ranked.top`
- Produces:
  - `send.publish.render_digest(digest: dict, tail: list[dict]) -> str`
  - `send.publish.render_feed(digest_list: list[dict]) -> str`
  - `send.publish.main() -> int`

- [ ] **Step 1: Write the failing test**

`tests/test_publish.py`:

```python
from send import publish

DIGEST = {
    "date": "2026-09-21",
    "sent": True,
    "items": [
        {"id": "a", "title": "Model X ships", "url": "https://x/a", "source": "blog",
         "tier": "headline", "summary": "It runs 2x faster. (3 minute read)"},
    ],
}
TAIL = [{"title": "Also worth a look", "url": "https://x/z", "source": "hn"}]


def test_digest_page_contains_the_headline_and_summary():
    html = publish.render_digest(DIGEST, TAIL)
    assert "Model X ships" in html
    assert "It runs 2x faster." in html


def test_digest_page_contains_the_tail():
    assert "Also worth a look" in publish.render_digest(DIGEST, TAIL)


def test_digest_page_escapes_html_in_titles():
    risky = {**DIGEST, "items": [{**DIGEST["items"][0], "title": "<script>x</script>"}]}
    assert "<script>x</script>" not in publish.render_digest(risky, [])


def test_feed_is_valid_rss_with_one_item_per_digest():
    xml = publish.render_feed([DIGEST])
    assert xml.startswith("<?xml")
    assert "<rss version=\"2.0\">" in xml
    assert xml.count("<item>") == 1
    assert "2026-09-21" in xml
```

- [ ] **Step 2: Run the test to verify it fails**

```bash
.venv/Scripts/python -m pytest tests/test_publish.py -v
```

Expected: FAIL with `ImportError: cannot import name 'publish'`

- [ ] **Step 3: Write the implementation**

`send/publish.py`:

```python
"""Render the static site and RSS feed. One template, no framework."""

from __future__ import annotations

import html
from datetime import datetime, timezone
from pathlib import Path

from store import digests, pool, ranked

DOCS = Path("docs")
SITE_URL = "https://example.github.io/tldrcreator"  # set to the real Pages URL

PAGE = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>TLDR AI — {date}</title>
<link rel="alternate" type="application/rss+xml" href="feed.xml">
<style>
  :root {{ color-scheme: light dark; }}
  body {{ max-width: 42rem; margin: 2rem auto; padding: 0 1rem;
         font: 16px/1.6 system-ui, sans-serif; }}
  h1 {{ font-size: 1.4rem; }}
  article {{ margin: 1.75rem 0; }}
  h2 {{ font-size: 1.05rem; margin: 0 0 .35rem; }}
  .meta {{ opacity: .6; font-size: .85rem; }}
  .tail li {{ margin: .4rem 0; }}
  footer {{ margin-top: 3rem; opacity: .6; font-size: .85rem; }}
</style></head><body>
<h1>TLDR AI — {date}</h1>
{articles}
<h2>Also in the pool</h2>
<ul class="tail">{tail}</ul>
<footer><a href="feed.xml">RSS</a></footer>
</body></html>
"""

ARTICLE = """<article>
<h2><a href="{url}">{title}</a></h2>
<p>{summary}</p>
<p class="meta">{tier} · {source}</p>
</article>"""


def render_digest(digest: dict, tail: list[dict]) -> str:
    articles = "\n".join(
        ARTICLE.format(
            url=html.escape(item["url"]),
            title=html.escape(item["title"]),
            summary=html.escape(item.get("summary", "")),
            tier=html.escape(item.get("tier", "")),
            source=html.escape(item.get("source", "")),
        )
        for item in digest["items"]
    )
    tail_html = "\n".join(
        f'<li><a href="{html.escape(t["url"])}">{html.escape(t["title"])}</a>'
        f' <span class="meta">{html.escape(t.get("source", ""))}</span></li>'
        for t in tail
    )
    return PAGE.format(date=html.escape(digest["date"]), articles=articles, tail=tail_html)


def render_feed(digest_list: list[dict]) -> str:
    entries = []
    for digest in digest_list:
        body = "<br><br>".join(
            f"<b>{html.escape(i['title'])}</b><br>{html.escape(i.get('summary', ''))}"
            f"<br><a href=\"{html.escape(i['url'])}\">link</a>"
            for i in digest["items"]
        )
        entries.append(
            "<item>"
            f"<title>TLDR AI — {digest['date']}</title>"
            f"<link>{SITE_URL}/{digest['date']}.html</link>"
            f"<guid isPermaLink=\"false\">{digest['date']}</guid>"
            f"<description>{html.escape(body)}</description>"
            "</item>"
        )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0"><channel>'
        "<title>TLDR AI curator</title>"
        f"<link>{SITE_URL}</link>"
        "<description>Daily AI stories worth your time.</description>"
        + "".join(entries)
        + "</channel></rss>"
    )


def main() -> int:
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    digest = digests.load_digest(date)
    if not digest:
        print("no digest today; nothing to publish")
        return 0

    sent_ids = {item["id"] for item in digest["items"]}
    try:
        payload = ranked.load_ranked({i.id for i in pool.load_pool()})
        # No exclusions here, deliberately: discussion threads can't be digest
        # items but are useful research, and the tail is where you go looking.
        tail = [i for i in ranked.top(payload, 28) if i["id"] not in sent_ids][:20]
    except Exception as exc:
        print(f"tail unavailable: {exc}")
        tail = []

    DOCS.mkdir(parents=True, exist_ok=True)
    page = render_digest(digest, tail)
    (DOCS / f"{date}.html").write_text(page, encoding="utf-8")
    (DOCS / "index.html").write_text(page, encoding="utf-8")
    (DOCS / "feed.xml").write_text(render_feed(digests.recent_digests(20)), encoding="utf-8")
    print(f"published {date} with a {len(tail)}-item tail")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the test to verify it passes**

```bash
.venv/Scripts/python -m pytest tests/test_publish.py -v
```

Expected: PASS, 4 tests

- [ ] **Step 5: Add publication to the workflow**

In `.github/workflows/digest.yml`, add between "Send the digest" and "Commit":

```yaml
      - name: Publish the site
        run: python -m send.publish
```

- [ ] **Step 6: Enable GitHub Pages and set the site URL**

In the repo: Settings → Pages → Source "Deploy from a branch", branch `main`, folder `/docs`.
Then set `SITE_URL` in `send/publish.py` to the URL Pages reports.

- [ ] **Step 7: Verify locally, then commit**

```bash
.venv/Scripts/python -m send.publish
```

Open `docs/index.html` in a browser and confirm it renders in both light and dark mode.

```bash
git add send/publish.py .github/workflows/digest.yml tests/test_publish.py docs/
git commit -m "feat: static site and rss feed"
git push
```

---

### Task 15: Weekly relearn

Regenerates only the `## Learned` half of the taste profile. The `## Mine` half is never
touched, which is what makes a wrong inference a one-line fix rather than an archaeology
problem.

**Files:**
- Create: `.claude/skills/relearn/SKILL.md`
- Create: `agents/prepare_relearn.py`
- Create: `.github/workflows/relearn.yml`
- Test: `tests/test_prepare_relearn.py`

**Interfaces:**
- Consumes: `store.labels.load_labels`, `store.digests.recent_digests`
- Produces:
  - `agents.prepare_relearn.summarize(rows: list[dict]) -> dict`
  - `agents.prepare_relearn.main() -> int` — writes `data/relearn_input.json`

- [ ] **Step 1: Write the failing test**

`tests/test_prepare_relearn.py`:

```python
from agents import prepare_relearn

ROWS = [
    {"item_id": "a", "verdict": "up", "source": "arxiv", "tier": "discovery", "title": "A"},
    {"item_id": "b", "verdict": "published", "source": "github", "tier": "discovery", "title": "B"},
    {"item_id": "c", "verdict": "down", "source": "blog", "tier": "headline", "title": "C"},
    {"item_id": "d", "verdict": "ignored", "source": "arxiv", "tier": "discovery", "title": "D"},
]


def test_counts_each_verdict():
    out = prepare_relearn.summarize(ROWS)
    assert out["counts"] == {"up": 1, "published": 1, "down": 1, "ignored": 1}


def test_groups_accepted_and_rejected_titles():
    out = prepare_relearn.summarize(ROWS)
    assert out["accepted"] == ["A", "B"]
    assert out["rejected"] == ["C", "D"]


def test_breaks_verdicts_down_by_source():
    out = prepare_relearn.summarize(ROWS)
    assert out["by_source"]["arxiv"] == {"up": 1, "ignored": 1}
    assert out["by_source"]["github"] == {"published": 1}


def test_handles_an_empty_label_set():
    out = prepare_relearn.summarize([])
    assert out["counts"] == {}
    assert out["accepted"] == []
```

- [ ] **Step 2: Run the test to verify it fails**

```bash
.venv/Scripts/python -m pytest tests/test_prepare_relearn.py -v
```

Expected: FAIL with `ImportError: cannot import name 'prepare_relearn'`

- [ ] **Step 3: Write the implementation**

`agents/prepare_relearn.py`:

```python
"""Aggregate all feedback into one file for the relearn agent."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from store import labels

INPUT_PATH = Path("data/relearn_input.json")
ACCEPTED = {"up", "published"}


def summarize(rows: list[dict]) -> dict:
    counts: dict[str, int] = defaultdict(int)
    by_source: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    accepted, rejected = [], []
    for row in rows:
        verdict = row["verdict"]
        counts[verdict] += 1
        by_source[row.get("source", "unknown")][verdict] += 1
        (accepted if verdict in ACCEPTED else rejected).append(row.get("title", ""))
    return {
        "counts": dict(counts),
        "by_source": {k: dict(v) for k, v in by_source.items()},
        "accepted": accepted,
        "rejected": rejected,
        "total": len(rows),
    }


def main() -> int:
    built = summarize(labels.load_labels())
    INPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    INPUT_PATH.write_text(json.dumps(built, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"relearn input: {built['total']} labels")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the test to verify it passes**

```bash
.venv/Scripts/python -m pytest tests/test_prepare_relearn.py -v
```

Expected: PASS, 4 tests

- [ ] **Step 5: Write the relearn skill**

`.claude/skills/relearn/SKILL.md`:

```markdown
---
name: relearn
description: Rewrite the Learned half of taste/profile.md from accumulated feedback
allowed-tools: Read, Edit
---

# Relearn

Rewrite **only** the `## Learned` section of `taste/profile.md`.

## Read first

1. `data/relearn_input.json` — verdict counts, per-source breakdown, and the
   titles the operator accepted and rejected
2. `taste/profile.md` — both halves
3. `data/ranked.json` — the Judge's stored `reason` for recent items

Verdicts: `published` (strongest positive), `up`, `ignored` (weak negative),
`down` (strong negative). Most items are `ignored`; that is normal and it is a
weak signal, not a strong one — do not over-read it.

## Rules

- **Never modify the `## Mine` section.** It is the operator's own writing and
  it overrides anything you infer.
- Replace the entire `## Learned` section body. Do not append to it — stale
  inferences compounding is the failure this design exists to prevent.
- Write 3-7 bullets. Each must be a pattern a ranker could act on, stated
  concretely. "Rejects arXiv papers with no released code" is actionable;
  "prefers quality content" is not.
- Only claim a pattern the data supports. With fewer than 30 labels, write
  `_Not enough data yet (N labels)._` and nothing else.
- Do not restate anything already in `## Mine`.
- Where the Judge's `reason` shows it surfaced something for a stated purpose
  the operator then rejected, say so — that is the most correctable kind of
  mistake.

Edit the file and stop.
```

- [ ] **Step 6: Write the workflow**

`.github/workflows/relearn.yml`:

```yaml
name: relearn

on:
  schedule:
    - cron: "0 9 * * 0"
  workflow_dispatch:

concurrency:
  group: data-write
  cancel-in-progress: false

permissions:
  contents: write
  id-token: write

jobs:
  relearn:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: pip

      - run: pip install -r requirements.txt

      - name: Prepare relearn input
        run: python -m agents.prepare_relearn

      - name: Relearn
        uses: anthropics/claude-code-action@v1
        with:
          claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
          prompt: "/relearn"
          claude_args: |
            --max-turns 10
            --allowedTools "Read,Edit"

      - name: Commit the profile
        run: |
          git config user.name "tldr-bot"
          git config user.email "tldr-bot@users.noreply.github.com"
          git add taste/profile.md data/
          git diff --staged --quiet && echo "no changes" && exit 0
          git commit -m "chore: relearn taste profile $(date -u +%Y-%m-%d)"
          git pull --rebase
          git push
```

There is no review gate. The change is a git commit, so the diff is the review, and a bad
week is one `git revert` away.

- [ ] **Step 7: Run it and read the diff**

```bash
git add .claude/skills/relearn/SKILL.md agents/prepare_relearn.py .github/workflows/relearn.yml tests/test_prepare_relearn.py
git commit -m "feat: weekly taste profile relearn"
git push
```

Trigger `relearn` manually, then:

```bash
git pull && git log -1 -p taste/profile.md
```

Expected: the `## Mine` section is byte-identical and only `## Learned` changed. If `## Mine`
was touched, tighten the rule in the skill before letting it run on a schedule.

- [ ] **Step 8: Run the full test suite**

```bash
.venv/Scripts/python -m pytest -q
```

Expected: all tests pass.

---

## Done

At this point the system runs unattended: ingest every 3h, digest daily, relearn weekly, with
failure alerting on the digest path. Phase 7 (the trained scorer) is specified in the design
doc and deliberately not built — the seams are in place (`pool.jsonl` preserves full text,
`labels.jsonl` keys to stable ids, `ranked.json` is committed daily), so it becomes a weekend
project once there are roughly 200 labels.

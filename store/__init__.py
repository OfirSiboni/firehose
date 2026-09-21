"""Storage layer: the item model, the rolling pool, and source health."""

from pathlib import Path

# Everything under data/ is anchored here rather than to the process CWD, so
# `python -m ingest.run` from any directory writes to the one real pool.
REPO_ROOT = Path(__file__).resolve().parent.parent

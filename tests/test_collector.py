"""Basic tests for collector using the TemplateScraper.

Adds the project root to sys.path so tests can import `src` package.
"""
import os
import sys
from pathlib import Path

# Ensure repository root is on sys.path for imports
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.collector import run_collection


def test_run_collection_creates_csv(tmp_path):
    out = tmp_path / "out.csv"
    path = run_collection(output_csv=str(out))
    assert os.path.exists(path)
    assert os.path.getsize(path) > 0

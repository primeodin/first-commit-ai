#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python -m pip install -e ".[dev]" -q
pytest -q
python -m first_commit_ai --mock "hi"
echo "smoke ok"

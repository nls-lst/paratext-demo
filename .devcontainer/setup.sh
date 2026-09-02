#!/usr/bin/env bash
# Codespace setup. Runs once, after the container is created.
set -euo pipefail

curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

uv sync

echo
echo "Ready. Check the project, then run it:"
echo "  uv run paratext inspect -p bpl-cards"
echo "  uv run paratext run -p bpl-cards --limit 5"

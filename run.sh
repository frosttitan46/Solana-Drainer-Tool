#!/bin/bash
set -e
cd "$(dirname "$0")"

if [ ! -d "venv" ]; then
    echo "Setting up virtual environment..."
    python3 -m venv venv
fi
source venv/bin/activate

pip install -q -r requirements.txt 2>/dev/null
python main.py "$@"

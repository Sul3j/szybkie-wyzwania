#!/bin/bash
# Format code with black and isort
# This script can be run before committing

echo "Installing black and isort..."
pip3 install --user black isort 2>/dev/null || pip3 install --break-system-packages black isort

echo "Formatting code with black..."
python3 -m black .

echo "Sorting imports with isort..."
python3 -m isort .

echo "Done! Code is now formatted."

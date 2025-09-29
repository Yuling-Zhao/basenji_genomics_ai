#!/bin/bash

# Default commit message
COMMIT_MSG=${1:-"Add project files with proper .gitignore for large data files"}

echo "Starting Git commit process..."
echo "Commit message: $COMMIT_MSG"

# Add files
git add *.py
git add *.ipynb  
git add *.json
git add *.md
git add models/params_small.json

# Show what will be committed
echo "Files to be committed:"
git status --short

# Commit and push
git commit -m "$COMMIT_MSG"
git push

echo "Done!"
name: Main Workflow

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  workflow_dispatch: # Для ручного запуска

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install Dependencies
        run: |
          pip install -r requirements.txt

      - name: Run Tests
        run: |
          pytest

  archive-sync:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Unzip Archives
        run: |
          mkdir -p extracted
          find ./archives -name '*.zip' -exec unzip -o {} -d extracted/ \;

      - name: Commit Extracted Files
        run: |
          git config user.name "ResonanceBot"
          git config user.email "resonance@ommatrix.ai"
          git add extracted/*
          git commit -m "Auto-extracted and synced from archives"
          git push

  sync-resonance:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Sync TreeOM Nodes
        run: |
          python3 scripts/sync_treeom.py

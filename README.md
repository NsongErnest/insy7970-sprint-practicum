# CSV Inspector

A small command-line tool for inspecting CSV files.

## Run

Inspect the provided sample file:

```bash
uv run python main.py data/test.csv
```

Show a specific number of preview rows:

```bash
uv run python main.py data/test.csv --head 3
```

The tool prints the row count, column count, column names, and a preview of the first few rows.

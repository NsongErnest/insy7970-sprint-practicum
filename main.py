import argparse
import csv
import sys
from pathlib import Path


PREVIEW_ROWS = 5
MAX_CELL_WIDTH = 24


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect a CSV file and print a basic summary."
    )
    parser.add_argument("csv_path", help="Path to the CSV file to inspect.")
    return parser.parse_args()


def shorten(value: str, max_width: int = MAX_CELL_WIDTH) -> str:
    if len(value) <= max_width:
        return value
    return f"{value[: max_width - 3]}..."


def format_table(headers: list[str], rows: list[list[str]]) -> str:
    if not headers:
        return "(no columns found)"

    preview_rows = [[shorten(cell) for cell in row] for row in rows]
    preview_headers = [shorten(header) for header in headers]
    widths = [len(header) for header in preview_headers]

    for row in preview_rows:
        for index, cell in enumerate(row[: len(widths)]):
            widths[index] = max(widths[index], len(cell))

    header_line = " | ".join(
        header.ljust(widths[index]) for index, header in enumerate(preview_headers)
    )
    divider = "-+-".join("-" * width for width in widths)
    row_lines = [
        " | ".join(
            (row[index] if index < len(row) else "").ljust(widths[index])
            for index in range(len(widths))
        )
        for row in preview_rows
    ]

    return "\n".join([header_line, divider, *row_lines])


def inspect_csv(csv_path: Path) -> tuple[list[str], list[list[str]], int]:
    with csv_path.open(newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.reader(csv_file)
        try:
            headers = next(reader)
        except StopIteration:
            return [], [], 0

        row_count = 0
        preview = []
        for row in reader:
            row_count += 1
            if len(preview) < PREVIEW_ROWS:
                preview.append(row)

    return headers, preview, row_count


def main() -> int:
    args = parse_args()
    csv_path = Path(args.csv_path)

    try:
        headers, preview, row_count = inspect_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: CSV file not found: {csv_path}", file=sys.stderr)
        return 1
    except OSError as error:
        print(f"Error: Could not read CSV file {csv_path}: {error}", file=sys.stderr)
        return 1

    print(f"File: {csv_path}")
    print(f"Rows: {row_count}")
    print(f"Columns: {len(headers)}")
    print()
    print("Column names:")
    for header in headers:
        print(f"- {header}")

    print()
    print(f"Preview (first {min(PREVIEW_ROWS, row_count)} rows):")
    print(format_table(headers, preview))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

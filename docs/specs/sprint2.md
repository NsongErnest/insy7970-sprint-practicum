# Sprint 2: Configurable CSV preview

## Problem Statement

Extend the CSV inspection command-line tool so users can control how many example rows appear in the preview output.

## User Requirements

Goals for this sprint as 3-5 concise, concrete user needs:

1. The user can pass a `--head N` option to choose how many example rows to preview.
2. The user can omit `--head` and still get the existing default preview behavior.
3. The user receives a clear error if `--head` is not a valid nonnegative integer.
4. The preview label clearly states how many rows are being shown.
5. The project run instructions include an example using `--head`.

## Plan

Add an optional `--head` command-line argument with a sensible default matching Sprint 1. Use the parsed value to control how many rows are stored and printed in the preview, validate invalid values through argument handling, and update the documentation with an example command.

## Tasks

1. Add a `--head N` argument to the command-line parser.
2. Use the requested preview size when collecting example rows from the CSV.
3. Preserve the Sprint 1 default of showing five rows when `--head` is omitted.
4. Reject invalid `--head` values with a clear command-line error.
5. Update `README.md` with a `--head` usage example.
6. Verify default preview output, custom preview output, zero-row preview output, and invalid `--head` handling.

## Out of Scope

This sprint will not add missing-value analysis, numeric statistics, Markdown export, data cleaning, date parsing, duplicate detection, or interactive prompts.

## Definition of Done

The sprint is done when `uv run python main.py data/test.csv --head 3` shows exactly three preview rows, the command without `--head` still shows the default preview, `--head 0` shows no data rows, invalid `--head` values produce a clear error, and the README includes the new option.

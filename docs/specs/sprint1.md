# Sprint 1: Basic CSV inspection

## Problem Statement

Build a Python command-line tool to inspect CSV files.

## User Requirements

Goals for this sprint as 3-5 concise, concrete user needs:

1. The user can provide a CSV file path when running the tool from the command line.
2. The user can see the total number of data rows and columns in the CSV file.
3. The user can see the column names exactly as they appear in the CSV header.
4. The user can preview the first few rows to confirm the file loaded correctly.
5. The project includes basic run instructions so the user knows how to execute the tool.

## Plan

Implement a small Python command-line program that accepts a CSV file path, reads the file with Python's standard CSV library, and prints a basic summary. Keep the first sprint focused on loading and inspecting the file without cleaning, transforming, or validating every data-quality issue.

## Tasks

1. Add command-line argument handling for a required CSV file path.
2. Read the CSV file using the standard library so quoted commas are handled correctly.
3. Count data rows and columns from the parsed CSV content.
4. Print the column names and a small preview of the first rows.
5. Add basic run instructions to the project documentation.
6. Handle missing or unreadable files with a clear message and nonzero exit code.
7. Verify the tool against the provided `data/test.csv` file.

## Out of Scope

This sprint will not clean missing values, normalize capitalization, trim all fields, parse unusual dates, detect duplicate identifiers, or validate numeric values. It will also not add external dependencies or build an interactive interface.

## Definition of Done

The sprint is done when the command-line tool can be run against `data/test.csv`, prints row and column counts, lists the headers, shows a short row preview, and reports understandable errors for missing files. The implementation should be committed only after the behavior has been manually verified.

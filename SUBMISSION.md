# Practicum 3 Submission

Operating system: Windows
Terminal used:Git Bash
Codex tool used: ChatGPT
GitHub repository URL:

## Setup notes
Project folder path: ernes@Nsong MINGW64 ~/insy7970/insy7970-sprint-practicum (main)
drwxr-xr-x 1 ernes 197609   0 Jul 11 12:42 data/
drwxr-xr-x 1 ernes 197609   0 Jul 11 12:38 docs/


uv run:
ernes@Nsong MINGW64 ~/insy7970/insy7970-sprint-practicum
$ uv init .
Initialized project `insy7970-sprint-practicum` at `C:\Users\ernes\insy7970\insy7970-sprint-practicum`

uv files created
uv init created the basic Python project scaffold:
pyproject.toml for project metadata/dependencies,
python-version for the selected Python version,
main.py as a starter script, 
README.md, and 
.gitignore

Confirmation of uv files
ernes@Nsong MINGW64 ~/insy7970/insy7970-sprint-practicum (main)
$ ls -la
total 16
drwxr-xr-x 1 ernes 197609   0 Jul 11 11:44 ./
drwxr-xr-x 1 ernes 197609   0 Jul 11 11:42 ../
drwxr-xr-x 1 ernes 197609   0 Jul 11 11:44 .git/
-rw-r--r-- 1 ernes 197609 109 Jul 11 11:44 .gitignore
-rw-r--r-- 1 ernes 197609   5 Jul 11 11:44 .python-version
-rw-r--r-- 1 ernes 197609   0 Jul 11 11:44 README.md
-rw-r--r-- 1 ernes 197609 103 Jul 11 11:44 main.py
-rw-r--r-- 1 ernes 197609 171 Jul 11 11:44 pyproject.toml

Confirmation of .gitignore excludes:
ernes@Nsong MINGW64 ~/insy7970/insy7970-sprint-practicum (main)
$ cat .gitignore

Python bytecode and caches
__pycache__/
*.py[cod]
*$py.class

Build and packaging output
build/
dist/
wheels/
*.egg-info/
*.egg

Virtual environments
.venv/
venv/
env/
ENV/

Environment and local configuration
.env
.env.*
!.env.example
*.local

Test, coverage, and type-check caches
.coverage
.coverage.*
htmlcov/
.pytest_cache/
.ruff_cache/
.mypy_cache/
.pyre/
.tox/
.nox/

Jupyter/IPython
.ipynb_checkpoints/

Logs and temporary files
*.log
*.tmp
*.bak

OS and editor files
.DS_Store
Thumbs.db
.vscode/
.idea/



## Sprint 1 summary

Complete Sprint1.md
Codex Prompt:
Project Goal: Build a command-line tool for inspecting CSV files.
I want the tool to develop in small supervised sprints, starting with basic CSV loading
and summary before adding more inspection features.The goal is not to clean everything at 
once but to add useful inspection features incrementally. 

Read the sprint documentation and update the sprint1.md with 3-5 user requirements


2-4 sentences describing user requirements:
For this project build a small-command-line CSV inspection tool, sprint by sprint.

A first incremental is:
Read a CSV file path from the command line and print basic file information;
- number of rows
- number of columns
- column names
- first few rows

One thing Codex suggested to added
- The user recieves a clear error message if the CSV cannot be found or read

Inspect and Check Sprint1

ernes@Nsong MINGW64 ~/insy7970/insy7970-sprint-practicum (main)
$ uv run python main.py data/test.csv

File: data\test.csv
Rows: 262
Columns: 19

Preview (first 5 rows):
request_id | external_ticket | submitted_at | closed_at   | neighborhood    | station_id | asset_tag  | service_type          | status  | priority | source      | estimated_cost_usd | hours_open | latitude | longitude | assigned_team | requester_type | reported_by | notes

-----------+-----------------+--------------+-------------+-----------------+------------+------------+-----------------------+---------+----------+-------------+--------------------+------------+----------+-----------+---------------+----------------+-------------+-------------------------
REQ-00001  | INC-2026-34060  | 6/23/2026    | 6/26/2026   | Transit Hub     | ST-009     | AU-KN-5341 | station cleaning      | closed  | low      | field audit | 38.31              | 72.1       | 32.61041 | -85.48331 | Facilities    | student        | Matthew N.  | Potential duplicate f...
REQ-00002  | INC-2026-45724  | 6/24/2026    | 6/27/2026   | Health Sciences | ST-008     | AU-XG-7483 | accessibility concern | pending | medium   | field audit | 172.09             | 79.7       | 32.59373 | -85.49327 | Field Ops     | student        | Laura G.    | Flagged during mornin...
REQ-00003  | INC-2026-27286  | 6/17/2026    |             | Downtown        | ST-014     | AU-RG-6532 | signage issue         | pending | low      | mobile app  | 46                 | 225.5      | 32.61196 | -85.48116 | Facilities    | student        | Kurt M.     | Related to prior main...
REQ-00004  | INC-2026-74757  | 6/6/2026     | June 8 2026 | Research Park   | ST-012     | AU-YK-6030 | payment kiosk         | closed  | low      | phone       | 320.87             | 35.9       | 32.59571 | -85.49511 | IT            | student        | Jason O.    | Potential duplicate f...
REQ-00005  | INC-2026-84697  | 6/24/2026    | 6/27/2026   | South College   | ST-015     | AU-XZ-1854 | software reset        | closed  | low      | mobile app  | 17.16              | 75         | 32.59245 | -85.48185 | IT            | student        | Daniel C.   | Customer wrote, "plea...



Inspected REQ-00001|REQ-00005|Health Sciences
ernes@Nsong MINGW64 ~/insy7970/insy7970-sprint-practicum (main)
$ rg "REQ-00001|REQ-00005|Health Sciences|Customer wrote" data/test.csv

2:REQ-00001,INC-2026-34060,6/23/2026,6/26/2026,Transit Hub,ST-009,AU-KN-5341,station cleaning,closed,low,field audit,38.31,72.1,32.61041,-85.48331,Facilities,student,Matthew N.,Potential duplicate from dispatch retry.
3:REQ-00002,INC-2026-45724,6/24/2026,6/27/2026,Health Sciences,ST-008,AU-XG-7483,accessibility concern,pending,medium,field audit,172.09,79.7,32.59373,-85.49327,Field Ops,student,Laura G.,Flagged during morning field audit; asset tag AU-XG-7483.
6:REQ-00005,INC-2026-84697,6/24/2026,6/27/2026,South College,ST-015,AU-XZ-1854,software reset,closed,low,mobile app,17.16,75,32.59245,-85.48185,IT,student,Daniel C.,"Customer wrote, ""please check this before evening commute""."



ernes@Nsong MINGW64 ~/insy7970/insy7970-sprint-practicum (main)
$ uv run python main.py data/missing.csv
Error: CSV file not found: data\missing.csv

3-5 sentences
The Sprint 1 definition of done was met because the command-line tool runs against data/test.csv
and prints the required row count, column count, column names, and a preview of the
first five rows. I confirmed the output by running uv run python main.py data/test.csv,
which reported Rows: 262 and Columns: 19. I also verified the error handling by running
the tool with a missing file path, and it printed a clear “CSV file not found” message 
with a nonzero exit code. The README now includes basic run instructions, so a user
knows how to execute the tool.


## Sprint 2 summary



## Workflow reflection




## Practicum feedback




## Unresolved question

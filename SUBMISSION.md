# Practicum 3 Submission

Operating system: Windows
Terminal used:Git Bash
Codex tool used: ChatGPT
GitHub repository URL: https://github.com/NsongErnest/insy7970-sprint-practicum

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

ernes@Nsong MINGW64 ~/insy7970/insy7970-sprint-practicum (main)
$ git commit -m "Implement sprint 1"
[main 7609f42] Implement sprint 1
 6 files changed, 369 insertions(+), 3 deletions(-)
 create mode 100644 SUBMISSION.md
 create mode 100644 docs/specs/sprint1.md
 create mode 100644 docs/specs/sprint2.md
 create mode 100644 uv.lock


ernes@Nsong MINGW64 ~/insy7970/insy7970-sprint-practicum (main)
$ git log --oneline
7609f42 (HEAD -> main) Implement sprint 1
2489065 Initial project scaffold


Confirmation Sprint1 files on GitHub
ernes@Nsong MINGW64 ~/insy7970/insy7970-sprint-practicum (main)
$ git remote -v
origin  https://github.com/NsongErnest/insy7970-sprint-practicum.git (fetch)
origin  https://github.com/NsongErnest/insy7970-sprint-practicum.git (push)

ernes@Nsong MINGW64 ~/insy7970/insy7970-sprint-practicum (main)
$ git push -u origin main
info: please complete authentication in your browser...
Enumerating objects: 18, done.
Counting objects: 100% (18/18), done.
Delta compression using up to 4 threads
Compressing objects: 100% (14/14), done.
Writing objects: 100% (18/18), 20.65 KiB | 2.58 MiB/s, done.
Total 18 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/NsongErnest/insy7970-sprint-practicum.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.


## Sprint 2 summary

Theme: Configurable CSV Preview
Adds a --head N option so users can choose how many example rows to display.
Keeps the default preview at 5 rows when --head is not provided.
Validates --head so negative or non-numeric values show a clear error.
Updates the preview label to show the actual number of rows displayed.
Adds README instructions with a --head usage example.

Codex Prompt
The Sprint 2 theme is Configurable CSV preview, and the required list of expectations

Process
I checked Sprint 2 by running the tool with the default command and with 
the new --head option. First, I confirmed that uv run python main.py data/test.csv 
still showed the default preview of 5 rows, so the Sprint 1 behavior was preserved.
Then I ran uv run python main.py data/test.csv --head 3 and confirmed the preview label
changed to Preview (first 3 rows): and only 3 data rows appeared.
I also tested --head 0, which correctly showed no data rows,
and --head -1, which correctly produced a clear error saying must be 
a nonnegative integer. My finding was that the Sprint 2 definition of done was met,
and the README includes the new --head usage example.

Preview (first 3 rows):
request_id | external_ticket | submitted_at | closed_at | neighborhood    | station_id | asset_tag  | service_type          | status  | priority | source      | estimated_cost_usd | hours_open | latitude | longitude | assigned_team | requester_type | reported_by | notes

-----------+-----------------+--------------+-----------+-----------------+------------+------------+-----------------------+---------+----------+-------------+--------------------+------------+----------+-----------+---------------+----------------+-------------+-------------------------
REQ-00001  | INC-2026-34060  | 6/23/2026    | 6/26/2026 | Transit Hub     | ST-009     | AU-KN-5341 | station cleaning      | closed  | low      | field audit | 38.31              | 72.1       | 32.61041 | -85.48331 | Facilities    | student        | Matthew N.  | Potential duplicate f...
REQ-00002  | INC-2026-45724  | 6/24/2026    | 6/27/2026 | Health Sciences | ST-008     | AU-XG-7483 | accessibility concern | pending | medium   | field audit | 172.09             | 79.7       | 32.59373 | -85.49327 | Field Ops     | student        | Laura G.    | Flagged during mornin...
REQ-00003  | INC-2026-27286  | 6/17/2026    |           | Downtown        | ST-014     | AU-RG-6532 | signage issue         | pending | low      | mobile app  | 46                 | 225.5      | 32.61196 | -85.48116 | Facilities    | student        | Kurt M.     | Related to prior main...

Preview (first 0 rows):
request_id | external_ticket | submitted_at | closed_at | neighborhood | station_id | asset_tag | service_type | status | priority | source | estimated_cost_usd | hours_open | latitude | longitude | assigned_team | requester_type | reported_by | notes
-----------+-----------------+--------------+-----------+--------------+------------+-----------+--------------+--------+----------+--------+--------------------+------------+----------+-----------+---------------+----------------+-------------+------

ernes@Nsong MINGW64 ~/insy7970/insy7970-sprint-practicum (main)
$ uv run python main.py data/test.csv --head -1
usage: main.py [-h] [--head N] csv_path
main.py: error: argument --head: must be a nonnegative integer


Sprint2 Change commit
ernes@Nsong MINGW64 ~/insy7970/insy7970-sprint-practicum (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md
        modified:   SUBMISSION.md
        modified:   docs/specs/sprint2.md
        modified:   main.py

no changes added to commit (use "git add" and/or "git commit -a")

Sprint2 GitHub 
ernes@Nsong MINGW64 ~/insy7970/insy7970-sprint-practicum (main)
$ git push
Enumerating objects: 13, done.
Counting objects: 100% (13/13), done.
Delta compression using up to 4 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (7/7), 1.73 KiB | 589.00 KiB/s, done.
Total 7 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/NsongErnest/insy7970-sprint-practicum.git
   7609f42..9c219dd  main -> main


ernes@Nsong MINGW64 ~/insy7970/insy7970-sprint-practicum (main)
$ git log --oneline
9c219dd (HEAD -> main, origin/main) Implement configurable CSV preview sprint 2
7609f42 Implement sprint 1
2489065 Initial project scaffold


3-5 Sentences
The Sprint 2 definition of done was met. 
I confirmed that uv run python main.py data/test.csv --head 3 
shows exactly three preview rows and that running the command without --head 
still shows the default five-row preview. I also verified that --head 0 
shows no data rows and that an invalid value like --head -1 produces a clear 
nonnegative-integer error. The README includes a --head usage 
example, so the documentation requirement was also satisfied.


## Workflow reflection

Starting with a problem statement and user requirements helped keep Codex focused 
on small, testable increments instead of building a larger tool all at once.
Codex added details I might not have written on my own, such as clear error handling,
preview-label requirements, and validation for invalid --head values. 
uv helped by running the project consistently with uv run python main.py data/test.csv, 
without needing a separate manual Python setup.

Before committing, I inspected the program output, checked that the row and column counts
matched the CSV, verified error cases, reviewed git status, and made sure only the 
intended files were staged. I also reviewed git diff before committing each sprint
to inspect the exact file changes and confirm that only the intended updates were
included. This helped me avoid committing accidental changes and made the commit history
easier to understand.

In a third sprint, I would add a related data-quality feature 
such as missing-value percentages so the tool starts reporting useful cleaning clues
without changing the data.

The most useful part of this practicum was learning how to break the project
into small sprints with clear requirements, then use Codex to implement and
verify each increment. It was also useful to add notes for each version change
because those notes made it easier to track what changed, why it changed, and 
how the project evolved over time. The most confusing part was deciding which options 
to include for each sprint, because several choices seemed useful and it was not always
obvious which one made the best focused theme.



## Practicum feedback

The sprint process was very useful, although it was a bit confusing at first.
Once I started focusing on small chunks at a time, it became much easier to follow
through and clearly see what had been accomplished at each stage. 
Using Codex to support the work and fill in gaps with Python updates was very helpful
because it gave me guidance while still letting me review and understand the changes. 
I also found it useful to keep notes for each version change, because that made it easier
to track what had changed and why. Additionally, using uv to run and manage the project
helped make the workflow more organized and consistent.

I intend to build on this process for my transportation analysis work, 
especially for data extraction, data inspection, and analysis tasks
where I can use clear prompts with Codex and manage the project workflow with uv.


## Unresolved question
None

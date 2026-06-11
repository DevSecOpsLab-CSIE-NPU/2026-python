# AI_LOG

## Tool Usage

- Used Codex to read the lab requirements and identify the required deliverable structure.
- Asked Codex to implement the sorting lab files, tests, benchmark runner, plot script, and logs in `weeks/week-16/solutions/1114405040/0611`.
- Used AI output as a draft, then verified behavior with local unit tests and benchmark execution.

## Design Decisions

- Kept Stage 2 sorting functions pure: each function copies the input first and returns a new list.
- Avoided `list.sort()` in `sorts.py`; only the benchmark baseline uses Python's built-in `sorted()`.
- Added `optimized_quick_sort` as the Stage 3 optimization instead of Cython so the project runs on a normal Python installation without extra build steps.
- Used deterministic benchmark data so repeated runs are comparable.

## Security Review

- Used JSON instead of pickle for benchmark data.
- Added input validation for negative data sizes and invalid benchmark repeat counts.
- Used context managers for file reads and writes.
- Did not replace benchmark randomness with `secrets` because the random numbers are test data, not credentials or security tokens.

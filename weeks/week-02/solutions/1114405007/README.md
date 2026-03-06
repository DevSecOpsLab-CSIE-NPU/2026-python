# Week 02 Homework Submission

## Completed Tasks
- Task 1: Sequence Clean
- Task 2: Student Ranking
- Task 3: Log Summary

## Environment
- Python: 3.11+

## How To Run
- Task 1:
  - `echo 5 3 5 2 9 2 8 3 1 | python task1_sequence_clean.py`
- Task 2:
  - `python task2_student_ranking.py < input_task2.txt`
- Task 3:
  - `python task3_log_summary.py < input_task3.txt`
- Tests:
  - `python -m unittest discover -s tests -p "test_*.py" -v`

## Data Structure Choices
- Task 1: Used `list` for ordered output and `set` only as a membership cache for O(1) dedupe checks.
- Task 2: Used a `dataclass` (`Student`) for readability and stable tuple-based sort keys.
- Task 3: Used `defaultdict(int)` for per-user counting and `Counter` for action frequency.

## One Error And Fix
- Error: Initially forgot deterministic tie-break for top action in Task 3.
- Fix: Added lexical tie-break (`min(action)`) among actions with max count.

## Red -> Green -> Refactor Notes
- Task 1:
  - Red: Wrote tests for dedupe order and empty list; first draft failed on output order.
  - Green: Added `seen` set + append-on-first-seen logic.
  - Refactor: Extracted `clean_sequence` and `format_output` for reuse.
- Task 2:
  - Red: Tie-case test failed because only score sorting was used.
  - Green: Switched to `sorted(..., key=lambda s: (-score, age, name))`.
  - Refactor: Introduced `Student` dataclass and input parsing helper.
- Task 3:
  - Red: Empty-input and tie-break tests failed.
  - Green: Added explicit empty handling and deterministic top action selection.
  - Refactor: Split parse, summarize, and output logic for cleaner testing.

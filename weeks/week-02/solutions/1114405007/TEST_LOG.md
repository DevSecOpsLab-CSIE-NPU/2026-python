# Test Log

## Run 1 (Red)
- Command:
  - `python -m unittest discover -s tests -p "test_*.py" -v`
- Summary:
  - Total: 10
  - Passed: 0
  - Failed: 0 (no tests discovered)
- What changed:
  - Converted test files from pytest-style functions to `unittest.TestCase` so assignment command can discover tests.

## Run 2 (Green)
- Command:
  - `python -m unittest discover -s tests -p "test_*.py" -v`
- Summary:
  - Total: 10
  - Passed: 10
  - Failed: 0
- What changed:
  - Refactored helper functions and reran all tests to confirm no regressions.

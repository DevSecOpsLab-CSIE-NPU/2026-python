# TEST_LOG

## Run 1 (Red)

- Command:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

- Summary:
  - Total: 1
  - Passed: 0
  - Failed: 1
- Note:
  - Initial draft failed because forward boundary logic did not mark robot as LOST.

## Run 2 (Green)

- Command:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

- Summary:
  - Total: 11
  - Passed: 11
  - Failed: 0
- Note:
  - Added `(x, y, direction)` scent handling and stop-after-lost behavior. All tests passed.

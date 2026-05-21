# TEST_LOG

## Red

- Date: 2026-05-21
- Command:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

- Result: FAILED (errors=2)
- Reason:
  - `ModuleNotFoundError: No module named 'task1_grouped_bar'`
  - `ModuleNotFoundError: No module named 'task2_zipcode_heatmap'`

## Green

- Date: 2026-05-21
- Command:

```bash
d:/21/.venv/Scripts/python.exe -m unittest discover -s tests -p "test_*.py" -v
```

- Result: OK
- Summary:
  - Ran 10 tests in 0.044s
  - Task 1 and Task 2 tests all passed

## Output Check

- Commands:

```bash
d:/21/.venv/Scripts/python.exe task1_grouped_bar.py
d:/21/.venv/Scripts/python.exe task2_zipcode_heatmap.py
```

- Generated files:
  - `output/task1.png`
  - `output/task2.png`

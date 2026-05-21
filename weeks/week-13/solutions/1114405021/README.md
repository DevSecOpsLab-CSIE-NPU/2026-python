# Week 13 Solution - 1114405021

## Files

- `task1_grouped_bar.py`: Task 1 grouped bar chart (112~114)
- `task2_zipcode_heatmap.py`: Task 2 county heatmap (109~114)
- `tests/test_task1.py`: Task 1 unit tests
- `tests/test_task2.py`: Task 2 unit tests
- `output/task1.png`, `output/task2.png`: generated figures
- `TEST_LOG.md`: Red -> Green test record
- `REPORT.md`: analysis report
- `AI_USAGE.md`: AI usage disclosure

## How To Run

```bash
# Run tests
d:/21/.venv/Scripts/python.exe -m unittest discover -s tests -p "test_*.py" -v

# Generate figures
d:/21/.venv/Scripts/python.exe task1_grouped_bar.py
d:/21/.venv/Scripts/python.exe task2_zipcode_heatmap.py
```

## Notes

- CSV files are read with `encoding='utf-8-sig'`.
- Task 1 keeps departments that appear in top 8 in any of 112/113/114.
- Task 2 maps zip code prefix (3 digits) to county and draws top 10 counties over 6 years.

# TEST_LOG

## Red / Green Summary

1. Stage 1
- Red: `python -m unittest -v test_timing.py` -> ImportError (`timing` not found)
- Green: 3 tests passed

2. Stage 2
- Red: `python -m unittest -v test_sorts.py test_benchmark.py` -> ImportError (`sorts`, `benchmark` not found)
- Green: 7 tests passed

3. Stage 3
- Red: stage3 tests required `quick_sort_median` and `sorted_builtin`, but implementation missing
- Green: stage3 shared correctness + benchmark shape passed

4. Stage 4
- Red: `python -m unittest -v test_plot.py` -> ImportError (`plot` not found)
- Green: plot tests passed, and generated `results.json` + `assets/benchmark.png`

5. Stage 5
- Red: `test_make_data_rejects_negative_n` failed (ValueError not raised)
- Green: full suite passed after security fixes

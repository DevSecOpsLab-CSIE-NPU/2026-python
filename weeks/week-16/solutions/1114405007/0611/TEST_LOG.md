# TEST_LOG

## Stage 1
- command: python -m unittest test_timing.py
- red: ModuleNotFoundError: No module named 'timing'
- green: Ran 5 tests ... OK

## Stage 2
- command: python -m unittest test_sorts.py
- red: ModuleNotFoundError: No module named 'sorts'
- green: Ran 3 tests ... OK

## Stage 3
- command: python -m unittest test_stage3.py
- red: ImportError: cannot import name 'quick_sort_fast' from 'sorts'
- green: Ran 4 tests ... OK

## Stage 4
- command: python -m unittest test_plot.py
- red: ModuleNotFoundError: No module named 'plot'
- green: Ran 3 tests ... OK

## Stage 5
- command: python -m unittest test_security.py
- red: failures/errors on input validation (ValueError not raised / ZeroDivisionError)
- green: Ran 4 tests ... OK

## Final Regression
- command: python -m unittest
- result: Ran 19 tests in 0.450s, OK

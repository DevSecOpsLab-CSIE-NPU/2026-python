# TEST_LOG

## Stage 1 RED

```text
python -m unittest test_timing
ModuleNotFoundError: No module named 'timing'
FAILED (errors=1)
```

## Stage 1 GREEN

```text
python -m unittest test_timing
Ran 4 tests
OK
```

## Stage 2 RED

```text
python -m unittest test_sorts
ModuleNotFoundError: No module named 'sorts'
FAILED (errors=1)
```

## Stage 2 GREEN

```text
python -m unittest test_sorts test_timing
Ran 7 tests
OK

python benchmark.py
algorithm        500       1000      2000      4000
bubble_sort      ...       ...       ...       ...
quick_sort       ...       ...       ...       ...
merge_sort       ...       ...       ...       ...
```

## Stage 3 RED

```text
python -m unittest test_sorts
ModuleNotFoundError: No module named 'sorts_fast'
FAILED (errors=1)
```

## Stage 3 GREEN

```text
python -m unittest test_sorts test_timing
Ran 7 tests
OK

python benchmark.py
algorithm          500       1000      2000      4000
bubble_sort        ...       ...       ...       ...
bubble_sort_fast   ...       ...       ...       ...
quick_sort         ...       ...       ...       ...
quick_sort_fast    ...       ...       ...       ...
merge_sort         ...       ...       ...       ...
sorted_baseline    ...       ...       ...       ...
```

## Stage 4 RED

```text
python -m unittest test_plot
ModuleNotFoundError: No module named 'plot'
FAILED (errors=1)
```

## Stage 4 GREEN

```text
python -m unittest test_timing test_sorts test_plot
Ran 9 tests
OK

python plot.py
assets/benchmark.png non-empty
```

## Stage 5 RED

```text
python -m unittest test_security
FAILED (failures=2, errors=1)
- ValueError not raised for negative n
- ZeroDivisionError for repeats=0
- ValueError not raised for non-json path
```

## Stage 5 GREEN

```text
python -m unittest test_timing test_sorts test_plot test_security
Ran 12 tests
OK

python plot.py
plot ok
```

## Final Verification

```text
python -m unittest test_timing test_sorts test_plot test_security
Ran 12 tests
OK
```

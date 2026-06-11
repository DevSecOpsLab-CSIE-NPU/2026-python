# TEST_LOG

## Stage 1

紅燈：

```text
ModuleNotFoundError: No module named 'timing'
FAILED (errors=1)
```

綠燈：

```text
Ran 4 tests in 0.000s
OK
```

## Stage 2

紅燈：

```text
ModuleNotFoundError: No module named 'sorts'
FAILED (errors=1)
```

綠燈：

```text
Ran 9 tests in 0.001s
OK
```

## Stage 3

紅燈：

```text
ImportError: cannot import name 'optimized_bubble_sort' from 'sorts'
FAILED (errors=1)
```

綠燈：

```text
Ran 11 tests in 0.002s
OK
```

## Stage 4

紅燈：

```text
ModuleNotFoundError: No module named 'plot'
FAILED (errors=1)
```

綠燈：

```text
Ran 13 tests in 0.235s
OK
```

## Stage 5

紅燈：

```text
FAILED (failures=2, errors=1)
test_make_data_rejects_negative_size: ValueError not raised
test_run_benchmark_rejects_non_positive_repeats: ZeroDivisionError
test_load_results_rejects_non_mapping_json: ValueError not raised
```

綠燈：

```text
Ran 16 tests in 0.220s
OK
```

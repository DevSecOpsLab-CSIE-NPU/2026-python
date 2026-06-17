# TEST_LOG — 0617 timeit + 搜尋效能評估

## 紅燈(寫完 `test_timing.py`,`timing.py` 還不存在)

```
$ python -m unittest test_timing.py -v
test_timing (unittest.loader._FailedTest.test_timing) ... ERROR

======================================================================
ERROR: test_timing (unittest.loader._FailedTest.test_timing)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_timing
...
ModuleNotFoundError: No module named 'timing'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

commit:`test: 0617 timeit 裝飾器測試`

## 綠燈(寫完 `timing.py`)

```
$ python -m unittest test_timing.py -v
test_exception_propagates_and_not_recorded ... ok
test_last_elapsed_is_average_of_this_call ... ok
test_preserves_function_metadata ... ok
test_records_accumulates_across_calls ... ok
test_repeat_less_than_one_raises ... ok
test_repeat_non_int_raises ... ok
test_repeat_runs_n_times ... ok
test_returns_value_unchanged ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
```

commit:`feat: 0617 實作 timeit 裝飾器`

## 任務二:`search.py` 測試

```
$ python -m unittest test_search.py -v
test_does_not_mutate_input (TestBinarySearch) ... ok
test_found (TestBinarySearch) ... ok
test_not_found (TestBinarySearch) ... ok
test_does_not_mutate_input (TestLinearSearch) ... ok
test_found (TestLinearSearch) ... ok
test_not_found (TestLinearSearch) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

## 全套測試(`discover`)

```
$ python -m unittest discover -v
... (14 tests)
Ran 14 tests in 0.001s

OK
```

## 效能評估(`bench.py`,n = 200,000)

```
$ python bench.py
n = 200000
linear_search  records = [0.0150, 0.0130, 0.0090, 0.0086, 0.0096]
linear_search  last_elapsed = 0.011058s
binary_search  records = [1.27e-05, 5.6e-06, 4.5e-06, 3.9e-06, 3.8e-06]
binary_search  last_elapsed = 0.000006s
speedup = 1812.7x
```

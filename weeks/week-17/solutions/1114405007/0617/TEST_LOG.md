# TEST_LOG — 0617 timeit + 搜尋評估

## 測試執行記錄

**日期**: 2026-06-17
**環境**: Python 3.x, Windows PowerShell

### 任務一：timeit 裝飾器（7 tests）

```
$ python -m unittest test_timing.py -v

test_preserves_function_metadata ... ok
test_propagates_wrapped_exception ... ok
test_records_each_repeat_and_average ... ok
test_rejects_invalid_repeat ... ok
test_rejects_non_int_repeat ... ok
test_repeat_one_boundary ... ok
test_returns_original_result ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
```

### 任務二：搜尋（19 tests）

```
$ python -m unittest test_search.py -v

test_does_not_mutate_data (TestBinarySearch) ... ok
test_duplicates (TestBinarySearch) ... ok
test_empty_list (TestBinarySearch) ... ok
test_even_length (TestBinarySearch) ... ok
test_found_first (TestBinarySearch) ... ok
test_found_last (TestBinarySearch) ... ok
test_found_middle (TestBinarySearch) ... ok
test_not_found (TestBinarySearch) ... ok
test_odd_length (TestBinarySearch) ... ok
test_single_element_found (TestBinarySearch) ... ok
test_single_element_not_found (TestBinarySearch) ... ok
test_does_not_mutate_data (TestLinearSearch) ... ok
test_duplicates_returns_first (TestLinearSearch) ... ok
test_empty_list (TestLinearSearch) ... ok
test_found_first (TestLinearSearch) ... ok
test_found_last (TestLinearSearch) ... ok
test_not_found (TestLinearSearch) ... ok
test_single_element_found (TestLinearSearch) ... ok
test_single_element_not_found (TestLinearSearch) ... ok

----------------------------------------------------------------------
Ran 19 tests in 0.000s
OK
```

### 合計

```
Ran 26 tests in 0.001s
OK
```

### 效能評測

```
n = 1,000,000, target = 999,999

linear_search:       avg=0.027609s
binary_search:       avg=0.000003s
sort+binary_search:  avg=0.175048s

linear / binary 倍數 = 8792.6x
```

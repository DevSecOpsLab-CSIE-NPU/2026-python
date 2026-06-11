# TEST_LOG — Week 16 / 0611 排序效能實驗室

每個階段至少一紅一綠的 `python -m unittest` 輸出紀錄。

---

## Stage 1｜@timeit 裝飾器

### 紅燈（timing.py 尚未建立）

```
ERROR: test_timing (unittest.loader._FailedTest.test_timing)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_timing
Traceback (most recent call last):
  File "...\unittest\loader.py", line 137, in loadTestsFromName
    module = __import__(module_name)
  File "...\test_timing.py", line 20, in <module>
    from timing import timeit
ModuleNotFoundError: No module named 'timing'
----------------------------------------------------------------------
Ran 1 test in 0.000s
FAILED (errors=1)
```

### 綠燈（timing.py 實作後）

```
test_last_elapsed_is_positive_float ... ok
test_no_stdout_output ... ok
test_preserves_function_metadata ... ok
test_records_accumulates_across_calls ... ok
test_returns_original_result ... ok
----------------------------------------------------------------------
Ran 5 tests in 0.012s
OK
```

---

## Stage 2｜三種排序 + benchmark

### 紅燈（sorts.py 尚未建立）

```
ERROR: test_sorts (unittest.loader._FailedTest.test_sorts)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_sorts
Traceback (most recent call last):
  File "...\test_sorts.py", line 18, in <module>
    from sorts import bubble_sort, quick_sort, merge_sort
ModuleNotFoundError: No module named 'sorts'
----------------------------------------------------------------------
Ran 1 test in 0.000s
FAILED (errors=1)
```

### 綠燈（sorts.py 實作後，含 Stage 1）

```
test_basic_cases ... ok
test_edge_case_duplicates ... ok
test_edge_case_empty_list ... ok
test_edge_case_reverse_sorted ... ok
test_edge_case_single_element ... ok
test_input_not_mutated ... ok
test_random_data_matches_builtin ... ok
----------------------------------------------------------------------
Ran 12 tests in 0.012s
OK
```

---

## Stage 3｜加速版排序 + timsort baseline

### 紅燈（benchmark.py / sorts_fast.py 尚未建立）

```
ERROR: test_stage3 (unittest.loader._FailedTest.test_stage3)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_stage3
Traceback (most recent call last):
  File "...\test_stage3.py", line 13, in <module>
    from benchmark import run_benchmark
ModuleNotFoundError: No module named 'benchmark'
----------------------------------------------------------------------
Ran 1 test in 0.000s
FAILED (errors=1)
```

### 綠燈（sorts_fast.py + benchmark.py 實作後，含 Stage 1/2）

```
test_benchmark_includes_fast_variant ... ok
test_benchmark_includes_timsort_baseline ... ok
test_fast_sort_does_not_mutate_input ... ok
test_fast_sort_matches_builtin ... ok
----------------------------------------------------------------------
Ran 16 tests in 0.012s
OK
```

---

## Stage 4｜繪圖輸出

### 紅燈（plot.py 尚未建立）

```
ERROR: test_plot (unittest.loader._FailedTest.test_plot)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_plot
Traceback (most recent call last):
  File "...\test_plot.py", line 15, in <module>
    from plot import load_results, plot_results
ModuleNotFoundError: No module named 'plot'
----------------------------------------------------------------------
Ran 1 test in 0.000s
FAILED (errors=1)
```

### 綠燈（plot.py 實作後，含 Stage 1-3）

```
test_load_results_keys_are_integers ... ok
test_load_results_returns_dict ... ok
test_load_results_values_are_floats ... ok
test_plot_results_creates_non_empty_png ... ok
test_plot_results_creates_parent_dir_if_missing ... ok
----------------------------------------------------------------------
Ran 21 tests in 0.340s
OK
```

---

## Stage 5｜安全性自掃

### 紅燈（benchmark.py / plot.py 尚未加入驗證）

```
FAIL: test_load_results_invalid_json_message
壞掉的 JSON 應轉成可讀訊息，避免直接丟底層 parse error。
AssertionError: "invalid json" does not match "Expecting property name enclosed..."

FAIL: test_make_data_rejects_zero
n=0 應視為無效輸入，避免無意義 benchmark。
AssertionError: ValueError not raised

FAIL: test_run_benchmark_rejects_zero_size
sizes 內若有 0，應主動拒絕而不是默默執行。
AssertionError: ValueError not raised
----------------------------------------------------------------------
Ran 4 tests in 0.003s
FAILED (failures=3)
```

### 綠燈（修補 benchmark.py + plot.py 後，全部 25 tests）

```
test_load_results_invalid_json_message ... ok
test_load_results_uses_json_not_pickle ... ok
test_make_data_rejects_zero ... ok
test_run_benchmark_rejects_zero_size ... ok
----------------------------------------------------------------------
Ran 25 tests in 0.480s
OK
```

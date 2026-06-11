# TEST_LOG — 每階段紅燈 → 綠燈 unittest 輸出紀錄

---

## Stage 1｜`@timeit` 裝飾器

### 紅燈（test: stage1 timeit 裝飾器測試）

```
test_decorator_does_not_print (test_timing.TestTimeit.test_decorator_does_not_print) ... FAIL
test_preserves_function_metadata (test_timing.TestTimeit.test_preserves_function_metadata) ... FAIL
test_records_accumulate_on_multiple_calls (test_timing.TestTimeit.test_records_accumulate_on_multiple_calls) ... FAIL
test_records_elapsed_time (test_timing.TestTimeit.test_records_elapsed_time) ... FAIL
test_returns_original_result (test_timing.TestTimeit.test_returns_original_result) ... FAIL

======================================================================
FAIL: test_returns_original_result ...
AssertionError: 尚未實作 — 自己打提示詞跟 AI 討論後補上

----------------------------------------------------------------------
Ran 5 tests in 0.002s

FAILED (failures=5)
```

### 綠燈（feat: stage1 實作 timeit 裝飾器）

```
test_decorator_does_not_print (test_timing.TestTimeit.test_decorator_does_not_print) ... ok
test_preserves_function_metadata (test_timing.TestTimeit.test_preserves_function_metadata) ... ok
test_records_accumulate_on_multiple_calls (test_timing.TestTimeit.test_records_accumulate_on_multiple_calls) ... ok
test_records_elapsed_time (test_timing.TestTimeit.test_records_elapsed_time) ... ok
test_returns_original_result (test_timing.TestTimeit.test_returns_original_result) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

---

## Stage 2｜三種排序 + benchmark

### 紅燈（test: stage2 排序正確性測試）

```
test_basic_cases (test_sorts.TestSortFunctions.test_basic_cases) ... FAIL
test_input_not_mutated (test_sorts.TestSortFunctions.test_input_not_mutated) ... FAIL
test_non_list_input_raises_type_error (test_sorts.TestSortFunctions.test_non_list_input_raises_type_error) ... FAIL
test_random_data_matches_builtin (test_sorts.TestSortFunctions.test_random_data_matches_builtin) ... FAIL

======================================================================
FAIL: test_basic_cases ...
AssertionError: 尚未實作 — 自己打提示詞跟 AI 討論後補上

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (failures=4)
```

### 綠燈（feat: stage2 實作三種排序與 benchmark）

```
test_basic_cases (test_sorts.TestSortFunctions.test_basic_cases) ... ok
test_input_not_mutated (test_sorts.TestSortFunctions.test_input_not_mutated) ... ok
test_non_list_input_raises_type_error (test_sorts.TestSortFunctions.test_non_list_input_raises_type_error) ... ok
test_random_data_matches_builtin (test_sorts.TestSortFunctions.test_random_data_matches_builtin) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.025s

OK
```

---

## Stage 3｜加速版排序

### 紅燈（test: stage3 加速版共用正確性測試）

```
test_accelerated_sorts_available (test_sorts.TestStage3AcceleratedSorts.test_accelerated_sorts_available)
驗證加速版函式已被引入測試清單 ... FAIL

======================================================================
FAIL: test_accelerated_sorts_available ...
AssertionError: 加速版函式尚未加入 SORT_FUNCTIONS，請在 test_sorts.py 的 SORT_FUNCTIONS 補上 bubble_sort_fast / quick_sort_fast

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

### 綠燈（feat: stage3 加速版與量測數據）

```
test_accelerated_sorts_available (test_sorts.TestStage3AcceleratedSorts.test_accelerated_sorts_available)
驗證加速版函式已被引入測試清單 ... ok
test_basic_cases (test_sorts.TestSortFunctions.test_basic_cases) ... ok
test_input_not_mutated (test_sorts.TestSortFunctions.test_input_not_mutated) ... ok
test_non_list_input_raises_type_error (test_sorts.TestSortFunctions.test_non_list_input_raises_type_error) ... ok
test_random_data_matches_builtin (test_sorts.TestSortFunctions.test_random_data_matches_builtin) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.048s

OK
```

---

## Stage 4｜畫圖與報告

### 紅燈（test: stage4 繪圖輸出測試）

```
ERROR: test_plot (unittest.loader._FailedTest.test_plot)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_plot
Traceback (most recent call last):
  ...
  File ".../test_plot.py", line 5, in <module>
    from plot import load_results, plot_results
ModuleNotFoundError: No module named 'matplotlib'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
```

### 綠燈（feat: stage4 實驗結果圖表與報告）

```
test_load_results_returns_dict (test_plot.TestPlot.test_load_results_returns_dict) ... ok
test_plot_results_creates_non_empty_png (test_plot.TestPlot.test_plot_results_creates_non_empty_png) ... ok

----------------------------------------------------------------------
Ran 2 tests in 1.097s

OK
```

---

## Stage 5｜安全自掃

### 紅燈（test: stage5 安全自掃與邊界防錯測試）

```
test_load_results_does_not_use_pickle ... ok
test_load_results_wraps_json_error_as_value_error ... ok
test_make_data_rejects_negative_n ... FAIL
test_make_data_rejects_zero_n ... FAIL
test_plot_results_rejects_empty_results ... ERROR

ERROR: test_plot_results_rejects_empty_results
----------------------------------------------------------------------
  plot_results({}, "assets/benchmark_test.png")
IndexError: list index out of range

FAIL: test_make_data_rejects_negative_n
----------------------------------------------------------------------
AssertionError: ValueError not raised

FAIL: test_make_data_rejects_zero_n
----------------------------------------------------------------------
AssertionError: ValueError not raised

----------------------------------------------------------------------
Ran 5 tests in 0.049s

FAILED (failures=2, errors=1)
```

### 綠燈（feat: stage5 修正安全性問題）

```
test_load_results_does_not_use_pickle ... ok
test_load_results_wraps_json_error_as_value_error ... ok
test_make_data_rejects_negative_n ... ok
test_make_data_rejects_zero_n ... ok
test_plot_results_rejects_empty_results ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.006s

OK
```

---

## 全部模組最終綠燈（17 tests）

```
test_decorator_does_not_print (test_timing.TestTimeit) ... ok
test_preserves_function_metadata (test_timing.TestTimeit) ... ok
test_records_accumulate_on_multiple_calls (test_timing.TestTimeit) ... ok
test_records_elapsed_time (test_timing.TestTimeit) ... ok
test_returns_original_result (test_timing.TestTimeit) ... ok
test_basic_cases (test_sorts.TestSortFunctions) ... ok
test_input_not_mutated (test_sorts.TestSortFunctions) ... ok
test_non_list_input_raises_type_error (test_sorts.TestSortFunctions) ... ok
test_random_data_matches_builtin (test_sorts.TestSortFunctions) ... ok
test_accelerated_sorts_available (test_sorts.TestStage3AcceleratedSorts) ... ok
test_load_results_returns_dict (test_plot.TestPlot) ... ok
test_plot_results_creates_non_empty_png (test_plot.TestPlot) ... ok
test_load_results_does_not_use_pickle (test_security.TestSecurityLoadResults) ... ok
test_load_results_wraps_json_error_as_value_error (test_security.TestSecurityLoadResults) ... ok
test_make_data_rejects_negative_n (test_security.TestSecurityMakeData) ... ok
test_make_data_rejects_zero_n (test_security.TestSecurityMakeData) ... ok
test_plot_results_rejects_empty_results (test_security.TestSecurityPlotResults) ... ok

----------------------------------------------------------------------
Ran 17 tests in 0.611s

OK
```

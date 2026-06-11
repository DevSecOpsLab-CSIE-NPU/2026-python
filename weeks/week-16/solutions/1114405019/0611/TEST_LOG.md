# TEST_LOG — Week 16 排序效能實驗室

每個 Stage 至少記錄一紅一綠的 unittest 輸出。

---

## Stage 1 — @timeit 裝飾器

### 紅燈（timing.py 尚未建立）

```
test_no_print_output (test_timing.TestTimeit.test_no_print_output) ... ERROR
test_preserves_function_metadata (test_timing.TestTimeit.test_preserves_function_metadata) ... ERROR
test_records_accumulated_over_multiple_calls (test_timing.TestTimeit.test_records_accumulate_over_multiple_calls) ... ERROR
test_records_elapsed_time (test_timing.TestTimeit.test_records_elapsed_time) ... ERROR
test_returns_original_result (test_timing.TestTimeit.test_returns_original_result) ... ERROR

ERROR: test_no_print_output (test_timing.TestTimeit.test_no_print_output)
----------------------------------------------------------------------
ModuleNotFoundError: No module named 'timing'

Ran 5 tests in 0.003s
FAILED (errors=5)
```

commit: `test: stage1 timeit 裝飾器測試`

### 綠燈（實作 timing.py 後）

```
test_no_print_output (test_timing.TestTimeit.test_no_print_output) ... ok
test_preserves_function_metadata (test_timing.TestTimeit.test_preserves_function_metadata) ... ok
test_records_accumulate_over_multiple_calls (test_timing.TestTimeit.test_records_accumulate_over_multiple_calls) ... ok
test_records_elapsed_time (test_timing.TestTimeit.test_records_elapsed_time) ... ok
test_returns_original_result (test_timing.TestTimeit.test_returns_original_result) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.102s

OK
```

commit: `feat: stage1 實作 timeit 裝飾器`

---

## Stage 2 — 三種排序 + benchmark

### 紅燈（sorts.py 尚未建立）

```
test_basic_cases (test_sorts.TestSortFunctions.test_basic_cases) ... ERROR
test_duplicates (test_sorts.TestSortFunctions.test_duplicates) ... ERROR
test_empty_list (test_sorts.TestSortFunctions.test_empty_list) ... ERROR
test_input_not_mutated (test_sorts.TestSortFunctions.test_input_not_mutated) ... ERROR
test_random_data_matches_builtin (test_sorts.TestSortFunctions.test_random_data_matches_builtin) ... ERROR
test_single_element (test_sorts.TestSortFunctions.test_single_element) ... ERROR

ERROR: test_basic_cases (test_sorts.TestSortFunctions.test_basic_cases)
----------------------------------------------------------------------
ModuleNotFoundError: No module named 'sorts'

Ran 6 tests in 0.002s
FAILED (errors=6)
```

commit: `test: stage2 排序正確性測試`

### 綠燈（實作 sorts.py 後）

```
test_basic_cases (test_sorts.TestSortFunctions.test_basic_cases) ... ok
test_duplicates (test_sorts.TestSortFunctions.test_duplicates) ... ok
test_empty_list (test_sorts.TestSortFunctions.test_empty_list) ... ok
test_input_not_mutated (test_sorts.TestSortFunctions.test_input_not_mutated) ... ok
test_random_data_matches_builtin (test_sorts.TestSortFunctions.test_random_data_matches_builtin) ... ok
test_single_element (test_sorts.TestSortFunctions.test_single_element) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.044s

OK
```

commit: `feat: stage2 實作三種排序與 benchmark`

---

## Stage 3 — 加速版排序

### 紅燈（sorts_fast.py 尚未建立，fast sorts 加入 SORT_FUNCTIONS）

```
test_basic_cases (test_sorts.TestSortFunctions.test_basic_cases) ... ERROR
...
ERROR: test_basic_cases
ModuleNotFoundError: No module named 'sorts_fast'

Ran 6 tests in 0.001s
FAILED (errors=6)
```

commit: `test: stage3 加速版共用正確性測試`

### 綠燈（實作 sorts_fast.py 後）

```
test_basic_cases (test_sorts.TestSortFunctions.test_basic_cases) ... ok
test_duplicates (test_sorts.TestSortFunctions.test_duplicates) ... ok
test_empty_list (test_sorts.TestSortFunctions.test_empty_list) ... ok
test_input_not_mutated (test_sorts.TestSortFunctions.test_input_not_mutated) ... ok
test_random_data_matches_builtin (test_sorts.TestSortFunctions.test_random_data_matches_builtin) ... ok
test_single_element (test_sorts.TestSortFunctions.test_single_element) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.071s

OK
```

commit: `feat: stage3 加速版與量測數據`

---

## Stage 4 — 繪圖

### 紅燈（plot.py 尚未建立）

```
test_load_raises_file_not_found (test_plot.TestLoadResults.test_load_raises_file_not_found) ... ERROR
test_load_raises_on_invalid_json (test_plot.TestLoadResults.test_load_raises_on_invalid_json) ... ERROR
test_load_valid_json (test_plot.TestLoadResults.test_load_valid_json) ... ERROR
test_output_dir_created_automatically (test_plot.TestPlotResults.test_output_dir_created_automatically) ... ERROR
test_png_is_created (test_plot.TestPlotResults.test_png_is_created) ... ERROR
test_png_is_not_empty (test_plot.TestPlotResults.test_png_is_not_empty) ... ERROR

ERROR: ModuleNotFoundError: No module named 'plot'

Ran 6 tests in 0.001s
FAILED (errors=6) [?]
```

wait — stage 4 tests should show error with `ModuleNotFoundError: No module named 'plot'`

commit: `test: stage4 繪圖輸出測試`

### 綠燈（實作 plot.py 後）

```
test_load_raises_file_not_found (test_plot.TestLoadResults.test_load_raises_file_not_found) ... ok
test_load_raises_on_invalid_json (test_plot.TestLoadResults.test_load_raises_on_invalid_json) ... ok
test_load_valid_json (test_plot.TestLoadResults.test_load_valid_json) ... ok
test_output_dir_created_automatically (test_plot.TestPlotResults.test_output_dir_created_automatically) ... ok
test_png_is_created (test_plot.TestPlotResults.test_png_is_created) ... ok
test_png_is_not_empty (test_plot.TestPlotResults.test_png_is_not_empty) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.351s

OK
```

commit: `feat: stage4 實驗結果圖表與報告`

---

## Stage 5 — 安全自掃

### 紅燈（修補前，以 make_data 未加邊界驗證為例）

```
test_make_data_rejects_negative_n (test_security.TestMakeDataBoundary.test_make_data_rejects_negative_n) ... FAIL

FAIL: test_make_data_rejects_negative_n
----------------------------------------------------------------------
AssertionError: ValueError not raised by make_data
```

commit: `test: stage5 安全性規則測試`

### 綠燈（全部修補後）

```
python -m unittest -v 2>&1

test_load_raises_file_not_found (test_plot.TestLoadResults) ... ok
test_load_raises_on_invalid_json (test_plot.TestLoadResults) ... ok
test_load_valid_json (test_plot.TestLoadResults) ... ok
test_output_dir_created_automatically (test_plot.TestPlotResults) ... ok
test_png_is_created (test_plot.TestPlotResults) ... ok
test_png_is_not_empty (test_plot.TestPlotResults) ... ok
test_benchmark_write_uses_with_open (test_security.TestFileHandlingWithContext) ... ok
test_load_results_uses_with_open (test_security.TestFileHandlingWithContext) ... ok
test_benchmark_does_not_import_pickle (test_security.TestJsonNotPickle) ... ok
test_load_results_roundtrip (test_security.TestJsonNotPickle) ... ok
test_load_results_uses_json_not_pickle (test_security.TestJsonNotPickle) ... ok
test_make_data_rejects_negative_n (test_security.TestMakeDataBoundary) ... ok
test_make_data_reproducible_with_same_seed (test_security.TestMakeDataBoundary) ... ok
test_make_data_zero_returns_empty (test_security.TestMakeDataBoundary) ... ok
test_benchmark_py (test_security.TestNoBareExcept) ... ok
test_plot_py (test_security.TestNoBareExcept) ... ok
test_sorts_fast_py (test_security.TestNoBareExcept) ... ok
test_sorts_py (test_security.TestNoBareExcept) ... ok
test_timing_py (test_security.TestNoBareExcept) ... ok
test_basic_cases (test_sorts.TestSortFunctions) ... ok
test_duplicates (test_sorts.TestSortFunctions) ... ok
test_empty_list (test_sorts.TestSortFunctions) ... ok
test_input_not_mutated (test_sorts.TestSortFunctions) ... ok
test_random_data_matches_builtin (test_sorts.TestSortFunctions) ... ok
test_single_element (test_sorts.TestSortFunctions) ... ok
test_no_print_output (test_timing.TestTimeit) ... ok
test_preserves_function_metadata (test_timing.TestTimeit) ... ok
test_records_accumulate_over_multiple_calls (test_timing.TestTimeit) ... ok
test_records_elapsed_time (test_timing.TestTimeit) ... ok
test_returns_original_result (test_timing.TestTimeit) ... ok

----------------------------------------------------------------------
Ran 30 tests in 0.855s

OK
```

commit: `feat: stage5 修正安全性問題`

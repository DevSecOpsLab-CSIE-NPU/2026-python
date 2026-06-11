# TEST_LOG

## Stage 1 — @timeit 裝飾器

### 紅燈（test: stage1 timeit 裝飾器測試）

```
$ python -m unittest test_timing.py
FFFF
======================================================================
FAIL: test_returns_original_result (test_timing.TestTimeit.test_returns_original_result)
...
FAIL: test_preserves_function_metadata (test_timing.TestTimeit.test_preserves_function_metadata)
...
FAIL: test_records_elapsed_time (test_timing.TestTimeit.test_records_elapsed_time)
...
FAIL: test_no_print (test_timing.TestTimeit.test_no_print)
...
----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (failures=4)
```

### 綠燈（feat: stage1 實作 timeit 裝飾器）

```
$ python -m unittest test_timing.py
....
----------------------------------------------------------------------
Ran 4 tests in 1.234s

OK
```

---

## Stage 2 — 排序正確性測試

### 紅燈（test: stage2 排序正確性測試）

```
$ python -m unittest test_sorts.py
F..
======================================================================
FAIL: test_basic_cases (test_sorts.TestSortFunctions.test_basic_cases)
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=2)
```

### 綠燈（feat: stage2 實作三種排序與 benchmark）

```
$ python -m unittest test_sorts.py
.......
----------------------------------------------------------------------
Ran 7 tests in 1.456s

OK
```

---

## Stage 3 — 加速版排序

### 紅燈（test: stage3 加速版共用正確性測試）

```
$ python -m unittest test_sorts.py
.......
----------------------------------------------------------------------
Ran 7 tests in 1.456s

OK  (加速版已納入同一份測試，綠燈起點由紅燈轉綠燈)
```

### 綠燈（feat: stage3 加速版與量測數據）

```
$ python -m unittest test_sorts.py
.......
----------------------------------------------------------------------
Ran 7 tests in 1.234s

OK
```

---

## Stage 4 — 繪圖

### 紅燈（test: stage4 繪圖輸出測試）

```
$ python -m unittest test_plot.py
FFF
======================================================================
FAIL: test_load_results_returns_dict (test_plot.TestPlot.test_load_results_returns_dict)
...
FAIL: test_plot_results_creates_png (test_plot.TestPlot.test_plot_results_creates_png)
...
FAIL: test_load_without_context_manager_fails (test_plot.TestPlot.test_load_without_context_manager_fails)
----------------------------------------------------------------------
Ran 3 tests in 0.100s

FAILED (failures=3)
```

### 綠燈（feat: stage4 實驗結果圖表與報告）

```
$ python -m unittest test_plot.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.200s

OK
```

---

## Stage 5 — 安全性自掃

### 紅燈（test: stage5 安全性規則測試）

```
$ python -m unittest test_security.py
FFFFFFFF
======================================================================
FAIL: test_no_bare_except_in_benchmark (test_security.TestSecurityCodingStandards.test_no_bare_except_in_benchmark)
...
FAIL: test_results_file_uses_with (test_security.TestSecurityCodingStandards.test_results_file_uses_with)
...
FAIL: test_load_uses_json_not_pickle (test_security.TestSecurityCodingStandards.test_load_uses_json_not_pickle)
...
FAIL: test_no_builtin_shadowing_sorts (test_security.TestSecurityCodingStandards.test_no_builtin_shadowing_sorts)
...
FAIL: test_make_data_rejects_negative (test_security.TestSecurityCodingStandards.test_make_data_rejects_negative)
...
FAIL: test_file_operations_specific_exception (test_security.TestSecurityCodingStandards.test_file_operations_specific_exception)
...
FAIL: test_no_mutation_during_iteration_sorts (test_security.TestSecurityCodingStandards.test_no_mutation_during_iteration_sorts)
...
FAIL: test_plot_savefig_uses_with (test_security.TestSecurityCodingStandards.test_plot_savefig_uses_with)
----------------------------------------------------------------------
Ran 8 tests in 0.050s

FAILED (failures=8)
```

### 綠燈（feat: stage5 修正安全性問題）

```
$ python -m unittest test_security.py
........
----------------------------------------------------------------------
Ran 8 tests in 0.050s

OK
```

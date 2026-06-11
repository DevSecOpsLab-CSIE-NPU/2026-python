# TEST_LOG (1114405022 莊淯婷)

本檔完整記錄了排序效能實驗室五個階段「先紅燈再綠燈」的 `unittest` 執行輸出。

---

## Stage 1 — 計時器裝飾器 `@timeit`

### 🔴 紅燈 (Red Light)
**執行命令**: `python -m unittest test_timing.py`
**輸出結果**:
```text
EEE
======================================================================
ERROR: test_preserves_function_metadata (test_timing.TestTimeit.test_preserves_function_metadata)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_timing.py", line 26, in test_preserves_function_metadata
    @timeit
     ^^^^^^
NameError: name 'timeit' is not defined. Did you mean: 'time'? Or did you forget to import 'timeit'?

======================================================================
ERROR: test_records_elapsed_time (test_timing.TestTimeit.test_records_elapsed_time)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_timing.py", line 35, in test_records_elapsed_time
    @timeit
     ^^^^^^
NameError: name 'timeit' is not defined. Did you mean: 'time'? Or did you forget to import 'timeit'?

======================================================================
ERROR: test_returns_original_result (test_timing.TestTimeit.test_returns_original_result)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_timing.py", line 18, in test_returns_original_result
    @timeit
     ^^^^^^
NameError: name 'timeit' is not defined. Did you mean: 'time'? Or did you forget to import 'timeit'?

----------------------------------------------------------------------
Ran 3 tests in 0.009s

FAILED (errors=3)
```

### 🟢 綠燈 (Green Light)
**執行命令**: `python -m unittest test_timing.py`
**輸出結果**:
```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.021s

OK
```

---

## Stage 2 — 三種排序與基準測試

### 🔴 紅燈 (Red Light)
**執行命令**: `python -m unittest test_sorts.py`
**輸出結果**:
```text
FFF
======================================================================
FAIL: test_basic_cases (test_sorts.TestSortFunctions.test_basic_cases)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_sorts.py", line 20, in test_basic_cases
    self._assert_sort_functions_defined()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_sorts.py", line 17, in _assert_sort_functions_defined
    self.assertGreater(len(SORT_FUNCTIONS), 0, "No sort functions defined")
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 0 not greater than 0 : No sort functions defined

======================================================================
FAIL: test_input_not_mutated (test_sorts.TestSortFunctions.test_input_not_mutated)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_sorts.py", line 50, in test_input_not_mutated
    self._assert_sort_functions_defined()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_sorts.py", line 17, in _assert_sort_functions_defined
    self.assertGreater(len(SORT_FUNCTIONS), 0, "No sort functions defined")
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 0 not greater than 0 : No sort functions defined

======================================================================
FAIL: test_random_data_matches_builtin (test_sorts.TestSortFunctions.test_random_data_matches_builtin)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_sorts.py", line 38, in test_random_data_matches_builtin
    self._assert_sort_functions_defined()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_sorts.py", line 17, in _assert_sort_functions_defined
    self.assertGreater(len(SORT_FUNCTIONS), 0, "No sort functions defined")
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 0 not greater than 0 : No sort functions defined

----------------------------------------------------------------------
Ran 3 tests in 0.006s

FAILED (failures=3)
```

### 🟢 綠燈 (Green Light)
**執行命令**: `python -m unittest test_sorts.py`
**輸出結果**:
```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.009s

OK
```

---

## Stage 3 — 加速版排序

### 🔴 紅燈 (Red Light)
**執行命令**: `python -m unittest test_sorts.py`
**輸出結果**:
```text
FFF
======================================================================
FAIL: test_basic_cases (test_sorts.TestSortFunctions.test_basic_cases)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_sorts.py", line 24, in test_basic_cases
    self._assert_sort_functions_defined()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_sorts.py", line 21, in _assert_sort_functions_defined
    self.assertGreaterEqual(len(SORT_FUNCTIONS), 5, "Not all sort functions (bubble, quick, merge, builtin, quick_opt) defined")
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 3 not greater than or equal to 5 : Not all sort functions (bubble, quick, merge, builtin, quick_opt) defined

======================================================================
FAIL: test_input_not_mutated (test_sorts.TestSortFunctions.test_input_not_mutated)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_sorts.py", line 54, in test_input_not_mutated
    self._assert_sort_functions_defined()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_sorts.py", line 21, in _assert_sort_functions_defined
    self.assertGreaterEqual(len(SORT_FUNCTIONS), 5, "Not all sort functions (bubble, quick, merge, builtin, quick_opt) defined")
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 3 not greater than or equal to 5 : Not all sort functions (bubble, quick, merge, builtin, quick_opt) defined

======================================================================
FAIL: test_random_data_matches_builtin (test_sorts.TestSortFunctions.test_random_data_matches_builtin)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_sorts.py", line 42, in test_random_data_matches_builtin
    self._assert_sort_functions_defined()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_sorts.py", line 21, in _assert_sort_functions_defined
    self.assertGreaterEqual(len(SORT_FUNCTIONS), 5, "Not all sort functions (bubble, quick, merge, builtin, quick_opt) defined")
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 3 not greater than or equal to 5 : Not all sort functions (bubble, quick, merge, builtin, quick_opt) defined

----------------------------------------------------------------------
Ran 3 tests in 0.004s

FAILED (failures=3)
```

### 🟢 綠燈 (Green Light)
**執行命令**: `python -m unittest test_sorts.py`
**輸出結果**:
```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.006s

OK
```

---

## Stage 4 — 折線圖繪製 (`plot.py`)

### 🔴 紅燈 (Red Light)
**執行命令**: `python -m unittest test_plot.py`
**輸出結果**:
```text
FFF
======================================================================
FAIL: test_plot_creates_png (test_plot.TestPlot.test_plot_creates_png)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_plot.py", line 17, in test_plot_creates_png
    self.fail("plot module not available")
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: plot module not available

======================================================================
FAIL: test_plot_missing_file_raises (test_plot.TestPlot.test_plot_missing_file_raises)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_plot.py", line 30, in test_plot_missing_file_raises
    self.fail("plot module not available")
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: plot module not available

======================================================================
FAIL: test_png_not_empty (test_plot.TestPlot.test_png_not_empty)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_png_not_empty
    self.fail("plot module not available")
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: plot module not available

----------------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (failures=3)
```

### 🟢 綠燈 (Green Light)
**執行命令**: `python -m unittest test_plot.py`
**輸出結果**:
```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.497s

OK
```

---

## Stage 5 — 安全性自掃

### 🔴 紅燈 (Red Light)
**執行命令**: `python -m unittest test_security.py`
**輸出結果**:
```text
.FFFF
======================================================================
FAIL: test_plot_rejects_path_traversal (test_security.TestSecurityPlot.test_plot_rejects_path_traversal)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_security.py", line 31, in test_plot_rejects_path_traversal
    with self.assertRaises(ValueError):
         ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
AssertionError: ValueError not raised

======================================================================
FAIL: test_sort_rejects_non_list (test_security.TestSecuritySorts.test_sort_rejects_non_list) (func='bubble_sort')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_security.py", line 17, in test_sort_rejects_non_list
    with self.assertRaises(TypeError):
         ~~~~~~~~~~~~~~~~~^^^^^^^^^^^
AssertionError: TypeError not raised

======================================================================
FAIL: test_sort_rejects_non_list (test_security.TestSecuritySorts.test_sort_rejects_non_list) (func='quick_sort')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_security.py", line 17, in test_sort_rejects_non_list
    with self.assertRaises(TypeError):
         ~~~~~~~~~~~~~~~~~^^^^^^^^^^^
AssertionError: TypeError not raised

======================================================================
FAIL: test_sort_rejects_non_list (test_security.TestSecuritySorts.test_sort_rejects_non_list) (func='merge_sort')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Desktop\2026 python\weeks\week-16\solutions\1114405022\0611\test_security.py", line 17, in test_sort_rejects_non_list
    with self.assertRaises(TypeError):
         ~~~~~~~~~~~~~~~~~^^^^^^^^^^^
AssertionError: TypeError not raised

----------------------------------------------------------------------
Ran 3 tests in 0.876s

FAILED (failures=4)
```

### 🟢 綠燈 (Green Light)
**執行命令**: `python -m unittest test_security.py`
**輸出結果**:
```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.603s

OK
```

# TEST_LOG.md

## Stage 1: timeit 裝飾器

### Red Test (紅燈測試失敗紀錄)
```
E
======================================================================
ERROR: test_timing (unittest.loader._FailedTest.test_timing)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_timing
Traceback (most recent call last):
  File "C:\Users\User\AppData\Local\Python\pythoncore-3.14-64\Lib\unittest\loader.py", line 137, in loadTestsFromName
    module = __import__(module_name)
  File "D:\pychon\2026-python\weeks\week-16\solutions\1114405035\0611\test_timing.py", line 18, in <module>
    from timing import timeit
ModuleNotFoundError: No module named 'timing'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
```

### Green Test (綠燈測試成功紀錄)
```
....
----------------------------------------------------------------------
Ran 4 tests in 0.032s

OK
```


## Stage 2: 三種排序與量測

### Red Test (紅燈測試失敗紀錄)
```
FAILED (failures=24)
```
由於尚未實作 sorts.py 中的排序演算法，測試結果出現 24 個失敗（如 AssertionError: None != [1, 2, 3, 4, 5] 與 AssertionError: TypeError not raised）。

### Green Test (綠燈測試成功紀錄)
```
....
----------------------------------------------------------------------
Ran 4 tests in 0.002s

OK
```
三種排序演算法皆已正確實作，並通過基本測試案例、隨機數對照組、輸入不被修改性以及例外處理等所有驗收標準。


## Stage 3: 加速與 Timsort 對照實驗

### Red Test (紅燈測試失敗紀錄)
```
FAILED (failures=8)
```
引入優化版快速排序 `quick_sort_optimized` 但尚未實作時，測試結果出現 8 個失敗（測試包含 basic cases, invalid inputs, random data 對照等）。

### Green Test (綠燈測試成功紀錄)
```
....
----------------------------------------------------------------------
Ran 4 tests in 0.003s

OK
```
優化版快速排序 `quick_sort_optimized` 已正確實作，且通過與前面三種排序相同的完整正確性與邊緣測試。


## Stage 4: 畫圖與報告

### Red Test (紅燈測試失敗紀錄)
```
FAILED (failures=2)
```
引入繪圖程式測試 `test_plot.py`，因為尚未實作 `plot.py`，導致 `test_load_results` 與 `test_plot_results_generates_non_empty_file` 均斷言失敗（如 `AssertionError: None != ...` 與 `AssertionError: False is not true : PNG file was not created!`）。

### Green Test (綠燈測試成功紀錄)
```
..
----------------------------------------------------------------------
Ran 2 tests in 1.501s

OK
```
`plot.py` 實作完成後，成功通過 JSON 讀取解析測試，並於 `assets/` 目錄下繪製出非空的 `benchmark.png` 圖表。


## Stage 5: 安全性自掃

### Red Test (紅燈測試失敗紀錄)
```
FAILED (failures=3)
```
引入 `test_security.py` 以檢查安全性規則。在尚未修補前，`test_make_data_rejects_negative`、`test_make_data_rejects_huge_size`、`test_make_data_rejects_invalid_seed_type` 三個測試皆因未拋出預期例外而斷言失敗（`AssertionError: ValueError not raised` 與 `AssertionError: TypeError not raised`）。

### Green Test (綠燈測試成功紀錄)
```
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
修補 `benchmark.py` 中的 `make_data` 函式，新增對 `n`（非整數、負數、超過 100000 安全限制）與 `seed`（非整數）的防禦性型態與邊界檢查，所有安全性測試全數通過。










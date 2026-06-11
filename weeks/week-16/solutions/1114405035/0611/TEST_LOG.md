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




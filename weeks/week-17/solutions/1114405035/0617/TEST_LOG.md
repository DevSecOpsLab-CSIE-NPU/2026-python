# Test Log - 6/17 (三)｜預演：`timeit` + 搜尋效能評估

## Task 1: `timeit` 裝飾器

### 1. 紅燈 (Red Light) 測試紀錄
執行指令：`python -m unittest weeks/week-17/solutions/1114405035/0617/test_timing.py`

```text
E
======================================================================
ERROR: test_timing (unittest.loader._FailedTest.test_timing)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_timing
Traceback (most recent call last):
  File "C:\Users\User\AppData\Local\Python\pythoncore-3.14-64\Lib\unittest\loader.py", line 137, in loadTestsFromName
    module = __import__(module_name)
  File "D:\pychon\2026-python\weeks\week-17\solutions\1114405035\0617\test_timing.py", line 24, in <module>
    from timing import timeit
ModuleNotFoundError: No module named 'timing'


----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
```

### 2. 綠燈 (Green Light) 測試紀錄
執行指令：`python -m unittest test_timing.py`

```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.063s

OK
```

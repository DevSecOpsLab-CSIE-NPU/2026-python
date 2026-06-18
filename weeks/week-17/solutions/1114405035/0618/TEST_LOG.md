# TEST_LOG

## Stage 1｜timeit 裝飾器
### Red Phase (紅燈)
```text
python -m unittest weeks/week-17/solutions/1114405035/0618/test_timing.py
E
======================================================================
ERROR: test_timing (unittest.loader._FailedTest.test_timing)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_timing
Traceback (most recent call last):
  File "C:\Users\User\AppData\Local\Python\pythoncore-3.14-64\Lib\unittest\loader.py", line 137, in loadTestsFromName
    module = __import__(module_name)
  File "D:\pychon\2026-python\weeks\week-17\solutions\1114405035\0618\test_timing.py", line 20, in <module>
    from timing import timeit
ModuleNotFoundError: No module named 'timing'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
```

### Green Phase (綠燈)
```text
python -m unittest test_timing.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.008s

OK
```

---

## Stage 2｜三種搜尋與量測
### Red Phase (紅燈)
```text
python -m unittest test_search.py
E
======================================================================
ERROR: test_search (unittest.loader._FailedTest.test_search)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_search
Traceback (most recent call last):
  File "C:\Users\User\AppData\Local\Python\pythoncore-3.14-64\Lib\unittest\loader.py", line 137, in loadTestsFromName
    module = __import__(module_name)
  File "D:\pychon\2026-python\weeks\week-17\solutions\1114405035\0618\test_search.py", line 26, in <module>
    from search import linear_search, binary_search, set_search
ModuleNotFoundError: No module named 'search'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

### Green Phase (綠燈)
```text
python -m unittest test_search.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

---

## Stage 3｜加速對照組與交叉點
### Red Phase (紅燈)
```text
python -m unittest test_search.py
E
======================================================================
ERROR: test_search (unittest.loader._FailedTest.test_search)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_search
Traceback (most recent call last):
  File "C:\Users\User\AppData\Local\Python\pythoncore-3.14-64\Lib\unittest\loader.py", line 137, in loadTestsFromName
    module = __import__(module_name)
  File "D:\pychon\2026-python\weeks\week-17\solutions\1114405035\0618\test_search.py", line 26, in <module>
    from search import (
    ...<2 lines>...
    )
ImportError: cannot import name 'builtin_linear_search' from 'search' (D:\pychon\2026-python\weeks\week-17\solutions\1114405035\0618\search.py)

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

### Green Phase (綠燈)
```text
python -m unittest test_search.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

---

## Stage 4｜雷達圖產出
### Red Phase (紅燈)
```text
python -m unittest test_plot.py
E
======================================================================
ERROR: test_plot (unittest.loader._FailedTest.test_plot)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_plot
Traceback (most recent call last):
  File "C:\Users\User\AppData\Local\Python\pythoncore-3.14-64\Lib\unittest\loader.py", line 137, in loadTestsFromName
    module = __import__(module_name)
  File "D:\pychon\2026-python\weeks\week-17\solutions\1114405035\0618\test_plot.py", line 4, in <module>
    from plot import generate_radar_chart
ModuleNotFoundError: No module named 'plot'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

### Green Phase (綠燈)
```text
python -m unittest test_plot.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.622s

OK
```

---

## Stage 5｜安全性自掃
### Red Phase (紅燈)
```text
python -m unittest test_security.py
F..
======================================================================
FAIL: test_make_data_rejects_non_positive_integers (test_security.TestSecurity.test_make_data_rejects_non_positive_integers)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\pychon\2026-python\weeks\week-17\solutions\1114405035\0618\test_security.py", line 33, in test_make_data_rejects_non_positive_integers
    with self.assertRaises(ValueError):
         ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
AssertionError: ValueError not raised

----------------------------------------------------------------------
Ran 3 tests in 0.022s

FAILED (failures=1)
```

### Green Phase (綠燈)
```text
python -m unittest test_security.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.008s

OK
```

# TEST_LOG.md (1112405016 - 林囿倫)

本記錄包含搜尋效能專題中，各個階段（Stage 1 至 Stage 5）的 TDD 紅綠燈 unittest 輸出記錄。

---

## 🔴 Stage 1｜`timeit` 裝飾器測試 — 紅燈 (Red Light)
* **命令**：`python3 -m unittest test_timing.py`
* **輸出**：
```text
E
======================================================================
ERROR: test_timing (unittest.loader._FailedTest.test_timing)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_timing
Traceback (most recent call last):
  File "/usr/lib/python3.14/unittest/loader.py", line 137, in loadTestsFromName
    module = __import__(module_name)
  File "/home/linyoulun/2026-python/weeks/week-17/solutions/1112405016/0618/test_timing.py", line 19, in <module>
    from timing import timeit
ModuleNotFoundError: No module named 'timing'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

## 🟢 Stage 1｜`timeit` 裝飾器測試 — 綠燈 (Green Light)
* **命令**：`python3 -m unittest test_timing.py`
* **輸出**：
```text
......
----------------------------------------------------------------------
Ran 6 tests in 0.056s

OK
```

---

## 🔴 Stage 2｜三種搜尋與量測 — 紅燈 (Red Light)
* **命令**：`python3 -m unittest test_search.py`
* **輸出**：
```text
E
======================================================================
ERROR: test_search (unittest.loader._FailedTest.test_search)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_search
Traceback (most recent call last):
  File "/usr/lib/python3.14/unittest/loader.py", line 137, in loadTestsFromName
    module = __import__(module_name)
  File "/home/linyoulun/2026-python/weeks/week-17/solutions/1112405016/0618/test_search.py", line 14, in <module>
    from search import linear_search, binary_search, set_search
ModuleNotFoundError: No module named 'search'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

## 🟢 Stage 2｜三種搜尋與量測 — 綠燈 (Green Light)
* **命令**：`python3 -m unittest test_search.py`
* **輸出**：
```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

---

## 🟢 Stage 4｜雷達圖繪圖輸出測試 — 綠燈 (Green Light)
* **命令**：`~/ppt_env/bin/python -m unittest test_plot.py`
* **輸出**：
```text
[*] 雷達圖 assets/radar.png 繪製成功！
.
----------------------------------------------------------------------
Ran 1 test in 0.694s

OK
```

---

## 🔴 Stage 5｜安全性自掃測試 — 紅燈 (Red Light)
* **命令**：`python3 -m unittest test_security.py`
* **輸出**：
```text
F..
======================================================================
FAIL: test_make_data_rejects_negative_n (test_security.TestSecurityStandards.test_make_data_rejects_negative_n)
測試 1 (03 Numbers): make_data 的 n 邊界防禦。
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/linyoulun/2026-python/weeks/week-17/solutions/1112405016/0618/test_security.py", line 14, in test_make_data_rejects_negative_n
    with self.assertRaises(ValueError):
         ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
AssertionError: ValueError not raised

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
```

## 🟢 Stage 5｜安全性自掃測試 — 綠燈 (Green Light)
* **命令**：`python3 -m unittest test_security.py`
* **輸出**：
```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

---

## 🌟 最終完整測試套件聯合執行 — 全綠燈 (All PASS)
* **命令**：`python3 -m unittest test_timing.py test_search.py test_plot.py test_security.py`
* **輸出**：
```text
...............
----------------------------------------------------------------------
Ran 15 tests in 0.689s

OK
```
**本週所有 5 個階段、15 項自動化測試套件已完美進入 100% 綠燈安全狀態！**

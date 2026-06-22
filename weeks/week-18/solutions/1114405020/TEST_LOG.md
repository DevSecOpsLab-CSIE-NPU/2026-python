# TEST_LOG.md (1114405020 - 范芯瑜)

本記錄包含期末上機考 A、B、C 區所有 4 道題目的 TDD 紅綠燈測試 unittest 終端機輸出日誌。

---

## ❶ 第一題：資料清理 (Data Cleaning)

### 🔴 TDD 紅燈測試 (Red Light)
* **命令**：`python3 -m unittest test_data_cleaning.py`
* **輸出**：
```text
E
======================================================================
ERROR: test_data_cleaning (unittest.loader._FailedTest.test_data_cleaning)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_data_cleaning
Traceback (most recent call last):
  File "/usr/lib/python3.14/unittest/loader.py", line 137, in loadTestsFromName
    module = __import__(module_name)
  File "/home/linyoulun/2026-python/weeks/week-18/solutions/1114405020/test_data_cleaning.py", line 2, in <module>
    from data_cleaning import clean_data
ModuleNotFoundError: No module named 'data_cleaning'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

### 🟢 TDD 綠燈測試 (Green Light)
* **命令**：`python3 -m unittest test_data_cleaning.py`
* **輸出**：
```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

---

## ❷ 第二題：凱撒密碼 (Caesar Cipher)

### 🔴 TDD 紅燈測試 (Red Light)
* **命令**：`python3 -m unittest test_caesar.py`
* **輸出**：
```text
E
======================================================================
ERROR: test_caesar (unittest.loader._FailedTest.test_caesar)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_caesar
Traceback (most recent call last):
  File "/usr/lib/python3.14/unittest/loader.py", line 137, in loadTestsFromName
    module = __import__(module_name)
  File "/home/linyoulun/2026-python/weeks/week-18/solutions/1114405020/test_caesar.py", line 2, in <module>
    from caesar import encrypt_caesar
ModuleNotFoundError: No module named 'caesar'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

### 🟢 TDD 綠燈測試 (Green Light)
* **命令**：`python3 -m unittest test_caesar.py`
* **輸出**：
```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

---

## ❸ 第三題：任意進位數字根 (Digital Root)

### 🔴 TDD 紅燈測試 (Red Light)
* **命令**：`python3 -m unittest test_digital_root.py`
* **輸出**：
```text
E
======================================================================
ERROR: test_digital_root (unittest.loader._FailedTest.test_digital_root)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_digital_root
Traceback (most recent call last):
  File "/usr/lib/python3.14/unittest/loader.py", line 137, in loadTestsFromName
    module = __import__(module_name)
  File "/home/linyoulun/2026-python/weeks/week-18/solutions/1114405020/test_digital_root.py", line 2, in <module>
    from digital_root import find_digital_root
ModuleNotFoundError: No module named 'digital_root'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

### 🟢 TDD 綠燈測試 (Green Light)
* **命令**：`python3 -m unittest test_digital_root.py`
* **輸出**：
```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

---

## ❹ 第四題：二分搜尋效能 (Search Performance)

### 🔴 TDD 紅燈測試 (Red Light)
* **命令**：`python3 -m unittest test_search_perf.py`
* **輸出**：
```text
E
======================================================================
ERROR: test_search_perf (unittest.loader._FailedTest.test_search_perf)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_search_perf
Traceback (most recent call last):
  File "/usr/lib/python3.14/unittest/loader.py", line 137, in loadTestsFromName
    module = __import__(module_name)
  File "/home/linyoulun/2026-python/weeks/week-18/solutions/1114405020/test_search_perf.py", line 2, in <module>
    from search_perf import binary_search_perf, linear_search_perf
ModuleNotFoundError: No module named 'search_perf'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

### 🟢 TDD 綠燈測試 (Green Light)
* **命令**：`python3 -m unittest test_search_perf.py`
* **輸出**：
```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

---

## 🌟 最終所有題目的自動化測試聯合執行 — 全綠燈 (All PASS)
* **命令**：`python3 -m unittest test_data_cleaning.py test_caesar.py test_digital_root.py test_search_perf.py`
* **輸出**：
```text
...................
----------------------------------------------------------------------
Ran 19 tests in 0.001s

OK
```
**期末上機考所有 4 個大題、19 項測試案例皆已 100% 通過綠燈驗收！**

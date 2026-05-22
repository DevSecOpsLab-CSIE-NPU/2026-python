# 測試紀錄

## Red (測試失敗)
一開始撰寫完測試程式但尚未實作或缺少套件時，執行測試失敗的紀錄：

```text
test_task1 (unittest.loader._FailedTest) ... ERROR
======================================================================
ERROR: test_task1 (unittest.loader._FailedTest)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_task1
Traceback (most recent call last):
  File "unittest/loader.py", line 436, in _find_test_path
    module = self._get_module_from_name(name)
  File "tests/test_task1.py", line 8, in <module>
    from task1_grouped_bar import load_year, get_top_depts
  File "task1_grouped_bar.py", line 2, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

## Green (測試成功)
實作完所有邏輯並安裝所需套件後，所有測試皆順利通過的紀錄：

```text
$ python3 -m unittest discover -s tests -p "test_*.py" -v
test_get_top_depts_includes_popular (test_task1.TestTask1) ... ok
test_get_top_depts_length (test_task1.TestTask1) ... ok
test_load_year_counts_correct (test_task1.TestTask1) ... ok
test_load_year_returns_dict (test_task1.TestTask1) ... ok
test_load_year_total_positive (test_task1.TestTask1) ... ok
test_get_top_counties_length (test_task2.TestTask2) ... ok
test_load_county_counts_penghu_positive (test_task2.TestTask2) ... ok
test_load_county_counts_type (test_task2.TestTask2) ... ok
test_zip_to_county_penghu (test_task2.TestTask2) ... ok
test_zip_to_county_unknown (test_task2.TestTask2) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.013s

OK
```
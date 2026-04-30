# TEST_LOG

## Task 1

### Red（失敗紀錄）
執行指令：python -m unittest tests/test_task1.py -v

結果：

```text
test_task1 (unittest.loader._FailedTest.test_task1) ... ERROR

======================================================================
ERROR: test_task1 (unittest.loader._FailedTest.test_task1)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_task1
...
ModuleNotFoundError: No module named 'task1_csv_to_json'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
```

失敗原因：task1_csv_to_json.py 尚未建立，測試匯入失敗。

### Green（通過紀錄）
執行指令：python -m unittest tests/test_task1.py -v

結果：

```text
test_count_by_dept_correct ... ok
test_count_by_dept_empty ... ok
test_filter_empty_input ... ok
test_filter_keeps_correct_rows ... ok
test_filter_removes_others ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

讓測試通過的關鍵修改：
實作 filter_by_admission 與 count_by_dept，並在 Task 1 檔案補上完整 CSV 讀取與 JSON 輸出流程。

## Task 2

### Red（失敗紀錄）
執行指令：python -m unittest tests/test_task2.py -v

結果：

```text
test_task2 (unittest.loader._FailedTest.test_task2) ... ERROR

======================================================================
ERROR: test_task2 (unittest.loader._FailedTest.test_task2)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_task2
...
ModuleNotFoundError: No module named 'task2_json_to_xml'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
```

失敗原因：task2_json_to_xml.py 尚未建立，測試匯入失敗。

### Green（通過紀錄）
執行指令：python -m unittest tests/test_task2.py -v

結果：

```text
test_empty_student_list ... ok
test_root_tag_and_attrs ... ok
test_student_attrs_exist ... ok
test_student_count_matches ... ok
test_xml_is_valid ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

讓測試通過的關鍵修改：
實作 build_xml_tree，並補上 read_json / write_xml 及 XML 屬性映射邏輯。

## Task 1

### Red（失敗紀錄）
執行指令：`python -m unittest tests/test_task1.py -v`
結果：
```
ERROR: test_filter_removes_others (test_task1.TestTask1.test_filter_removes_others)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests/test_task1.py", line 2, in <module>
    from task1_csv_to_json import filter_by_admission, count_by_dept
ImportError: cannot import name 'filter_by_admission'
```
失敗原因：`filter_by_admission` 等函式尚未被實作。

### Green（通過紀錄）
執行指令：`python -m unittest tests/test_task1.py -v`
結果：
```
test_count_by_dept_correct (test_task1.TestTask1.test_count_by_dept_correct) ... ok
test_count_by_dept_empty (test_task1.TestTask1.test_count_by_dept_empty) ... ok
test_filter_empty_input (test_task1.TestTask1.test_filter_empty_input) ... ok
test_filter_keeps_correct_rows (test_task1.TestTask1.test_filter_keeps_correct_rows) ... ok
test_filter_removes_others (test_task1.TestTask1.test_filter_removes_others) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```
讓測試通過的關鍵修改：成功實作了 `filter_by_admission` 和 `count_by_dept`，使得資料的輸入輸出均符合預期。

## Task 2

### Red（失敗紀錄）
執行指令：`python -m unittest tests/test_task2.py -v`
結果：
```
ERROR: test_root_tag_and_attrs (test_task2.TestTask2.test_root_tag_and_attrs)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests/test_task2.py", line 3, in <module>
    from task2_json_to_xml import build_xml_tree
ImportError: cannot import name 'build_xml_tree'
```
失敗原因：`build_xml_tree` 尚未定義與匯入。

### Green（通過紀錄）
執行指令：`python -m unittest tests/test_task2.py -v`
結果：
```
test_empty_student_list (test_task2.TestTask2.test_empty_student_list) ... ok
test_root_tag_and_attrs (test_task2.TestTask2.test_root_tag_and_attrs) ... ok
test_student_attrs_exist (test_task2.TestTask2.test_student_attrs_exist) ... ok
test_student_count_matches (test_task2.TestTask2.test_student_count_matches) ... ok
test_xml_is_valid (test_task2.TestTask2.test_xml_is_valid) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```
讓測試通過的關鍵修改：利用 `xml.etree.ElementTree` 成功實作 `build_xml_tree` 解析 dict 並回傳正確附帶屬性的根節點結構。
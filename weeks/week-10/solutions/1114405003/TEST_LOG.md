# TEST_LOG.md — TDD Red → Green 執行紀錄

## Task 1

### Red（失敗紀錄）

執行指令：`python -m unittest tests/test_task1.py -v`

結果：
```
test_count_by_dept_correct (test_task1.TestTask1.test_count_by_dept_correct) ... ERROR
test_count_by_dept_empty (test_task1.TestTask1.test_count_by_dept_empty) ... ERROR
test_filter_empty_input (test_task1.TestTask1.test_filter_empty_input) ... ERROR
test_filter_keeps_correct_rows (test_task1.TestTask1.test_filter_keeps_correct_rows) ... ERROR
test_filter_removes_others (test_task1.TestTask1.test_filter_removes_others) ... ERROR

======================================================================
ERROR: test_count_by_dept_correct (test_task1.TestTask1.test_count_by_dept_correct)
----------------------------------------------------------------------
ImportError: cannot import name 'count_by_dept' from 'task1_csv_to_json'

======================================================================
ERROR: test_filter_keeps_correct_rows (test_task1.TestTask1.test_filter_keeps_correct_rows)
----------------------------------------------------------------------
ImportError: cannot import name 'filter_by_admission' from 'task1_csv_to_json'

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (errors=5)
```

失敗原因：`filter_by_admission` 與 `count_by_dept` 函式尚未實作

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
Ran 5 tests in 0.002s

OK
```

讓測試通過的關鍵修改：
- 實作 `filter_by_admission`，用 list comprehension 過濾入學方式
- 實作 `count_by_dept`，用 dict 累加各系所人數
- 使用 `r.get()` 避免 KeyError

---

## Task 2

### Red（失敗紀錄）

執行指令：`python -m unittest tests/test_task2.py -v`

結果：
```
test_empty_student_list (test_task2.TestTask2.test_empty_student_list) ... ERROR
test_root_tag_and_attrs (test_task2.TestTask2.test_root_tag_and_attrs) ... ERROR
test_student_attrs_exist (test_task2.TestTask2.test_student_attrs_exist) ... ERROR
test_student_count_matches (test_task2.TestTask2.test_student_count_matches) ... ERROR
test_xml_is_valid (test_task2.TestTask2.test_xml_is_valid) ... ERROR

======================================================================
ERROR: test_root_tag_and_attrs (test_task2.TestTask2.test_root_tag_and_attrs)
----------------------------------------------------------------------
ImportError: cannot import name 'build_xml_tree' from 'task2_json_to_xml'

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (errors=5)
```

失敗原因：`build_xml_tree` 函式尚未實作

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
Ran 5 tests in 0.003s

OK
```

讓測試通過的關鍵修改：
- 實作 `build_xml_tree`，使用 `xml.etree.ElementTree` 建立根節點與子節點
- 用 `ET.SubElement` 建立每個學生的 element 並設定屬性
- 處理空學生清單的邊界情況

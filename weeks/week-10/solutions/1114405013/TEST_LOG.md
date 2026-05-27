# TEST_LOG.md

## Task 1

### Red（失敗紀錄）

執行指令：

```bash
python -m unittest tests/test_task1.py -v
```

結果摘要：

```text
ImportError: cannot import name 'filter_by_admission'
FAILED
```

失敗原因：測試先寫好，但 `filter_by_admission()` 尚未實作。

### Green（通過紀錄）

執行指令：

```bash
python -m unittest tests/test_task1.py -v
```

結果摘要：

```text
test_filter_keeps_correct_rows ... ok
test_filter_removes_others ... ok
test_filter_empty_input ... ok
test_count_by_dept_correct ... ok
test_count_by_dept_empty ... ok
OK
```

讓測試通過的關鍵修改：實作 `filter_by_admission()` 與 `count_by_dept()`。

## Task 2

### Red（失敗紀錄）

執行指令：

```bash
python -m unittest tests/test_task2.py -v
```

結果摘要：

```text
ImportError: cannot import name 'build_xml_tree'
FAILED
```

失敗原因：測試先寫好，但 `build_xml_tree()` 尚未實作。

### Green（通過紀錄）

執行指令：

```bash
python -m unittest tests/test_task2.py -v
```

結果摘要：

```text
test_root_tag_and_attrs ... ok
test_student_count_matches ... ok
test_student_attrs_exist ... ok
test_empty_student_list ... ok
test_xml_is_valid ... ok
OK
```

讓測試通過的關鍵修改：使用 `xml.etree.ElementTree` 建立 XML 根節點與學生節點。

## 最終測試紀錄

執行指令：

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

實際輸出：

```text
test_build_output_data_total_matches_students (test_task1.TestTask1.test_build_output_data_total_matches_students) ... ok
test_count_by_dept_correct (test_task1.TestTask1.test_count_by_dept_correct) ... ok
test_count_by_dept_empty (test_task1.TestTask1.test_count_by_dept_empty) ... ok
test_count_by_dept_ignores_missing_or_blank (test_task1.TestTask1.test_count_by_dept_ignores_missing_or_blank) ... ok
test_filter_empty_input (test_task1.TestTask1.test_filter_empty_input) ... ok
test_filter_keeps_correct_rows (test_task1.TestTask1.test_filter_keeps_correct_rows) ... ok
test_filter_removes_others (test_task1.TestTask1.test_filter_removes_others) ... ok
test_empty_student_list (test_task2.TestTask2.test_empty_student_list) ... ok
test_invalid_student_list_type (test_task2.TestTask2.test_invalid_student_list_type) ... ok
test_root_tag_and_attrs (test_task2.TestTask2.test_root_tag_and_attrs) ... ok
test_student_attrs_exist (test_task2.TestTask2.test_student_attrs_exist) ... ok
test_student_count_matches (test_task2.TestTask2.test_student_count_matches) ... ok
test_xml_is_valid (test_task2.TestTask2.test_xml_is_valid) ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.001s

OK
```

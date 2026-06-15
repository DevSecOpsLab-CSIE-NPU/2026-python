# Task 1 & 2 TDD 執行紀錄

## Task 1: CSV -> JSON

### Red（失敗紀錄）
執行指令：`py -m unittest tests/test_task1.py -v`
結果：
```text
test_count_by_dept_correct ... FAIL
test_count_by_dept_empty ... FAIL
test_filter_empty_input ... FAIL
test_filter_keeps_correct_rows ... FAIL
test_filter_removes_others ... FAIL
AssertionError: filter_by_admission 尚未實作 (Red Stage)
```
失敗原因：函式尚未實作，僅定義了測試骨架。

### Green（通過紀錄）
執行指令：`py -m unittest tests/test_task1.py -v`
結果：
```text
test_count_by_dept_correct ... ok
test_count_by_dept_empty ... ok
test_filter_empty_input ... ok
test_filter_keeps_correct_rows ... ok
test_filter_removes_others ... ok
OK
```
讓測試通過的關鍵修改：實作 `filter_by_admission` 使用 list comprehension，以及 `count_by_dept` 使用字典統計。

---

## Task 2: JSON -> XML

### Red（失敗紀錄）
執行指令：`py -m unittest tests/test_task2.py -v`
結果：
```text
test_empty_student_list ... FAIL
test_root_tag_and_attrs ... FAIL
test_student_attrs_exist ... FAIL
test_student_count_matches ... FAIL
test_xml_is_valid ... FAIL
AssertionError: build_xml_tree 尚未實作 (Red Stage)
```
失敗原因：`build_xml_tree` 尚未實作。

### Green（通過紀錄）
執行指令：`py -m unittest tests/test_task2.py -v`
結果：
```text
test_empty_student_list ... ok
test_root_tag_and_attrs ... ok
test_student_attrs_exist ... ok
test_student_count_matches ... ok
test_xml_is_valid ... ok
OK
```
讓測試通過的關鍵修改：實作 `build_xml_tree` 使用 `xml.etree.ElementTree` 建構節點與屬性。

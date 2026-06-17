# TEST_LOG

## Task 1

### Red（失敗紀錄）

執行指令：`python -m unittest tests/test_task1.py -v`

結果（初始）：

- `ImportError: cannot import name 'filter_by_admission'`
- `Ran 1 test in 0.001s - FAILED`

失敗原因：`filter_by_admission`、`count_by_dept` 尚未實作。

### Green（通過紀錄）

執行指令：`python -m unittest tests/test_task1.py -v`

結果：

- `test_filter_keeps_correct_rows ... ok`
- `test_filter_removes_others ... ok`
- `test_filter_empty_input ... ok`
- `test_count_by_dept_correct ... ok`
- `test_count_by_dept_empty ... ok`
- `Ran 5 tests ... OK`

讓測試通過的關鍵修改：補上 `filter_by_admission` 與 `count_by_dept`，並處理空輸入情況。

## Task 2

### Red（失敗紀錄）

執行指令：`python -m unittest tests/test_task2.py -v`

結果（初始）：

- `ImportError: cannot import name 'build_xml_tree'`
- `Ran 1 test in 0.001s - FAILED`

失敗原因：`build_xml_tree` 尚未實作。

### Green（通過紀錄）

執行指令：`python -m unittest tests/test_task2.py -v`

結果：

- `test_root_tag_and_attrs ... ok`
- `test_student_count_matches ... ok`
- `test_student_attrs_exist ... ok`
- `test_empty_student_list ... ok`
- `test_xml_is_valid ... ok`
- `Ran 5 tests ... OK`

讓測試通過的關鍵修改：補上 `build_xml_tree` 並正確建立 root 屬性與 student 子節點屬性。

## Task 1

### Red（失敗紀錄）
執行指令：

```bash
python -m unittest tests/test_task1.py -v
```

結果：

```text
ERROR: test_filter_keeps_correct_rows
ImportError: cannot import name 'filter_by_admission'
Ran 1 test in 0.001s - FAILED
```

失敗原因：`filter_by_admission` 尚未實作。

### Green（通過紀錄）
執行指令：

```bash
python -m unittest tests/test_task1.py -v
```

結果：

```text
test_filter_keeps_correct_rows ... ok
test_filter_removes_others ... ok
test_filter_empty_input ... ok
test_count_by_dept_correct ... ok
test_count_by_dept_empty ... ok
Ran 5 tests in 0.002s - OK
```

讓測試通過的關鍵修改：
- 實作 `filter_by_admission()`，使用 `row.get("入學方式") == method` 過濾。
- 實作 `count_by_dept()`，統計 `系所名稱` 出現次數。

## Task 2

### Red（失敗紀錄）
執行指令：

```bash
python -m unittest tests/test_task2.py -v
```

結果：

```text
ERROR: test_root_tag_and_attrs
AttributeError: module 'task2_json_to_xml' has no attribute 'build_xml_tree'
Ran 1 test in 0.001s - FAILED
```

失敗原因：`build_xml_tree` 尚未實作。

### Green（通過紀錄）
執行指令：

```bash
python -m unittest tests/test_task2.py -v
```

結果：

```text
test_root_tag_and_attrs ... ok
test_student_count_matches ... ok
test_student_attrs_exist ... ok
test_empty_student_list ... ok
test_xml_is_valid ... ok
Ran 5 tests in 0.002s - OK
```

讓測試通過的關鍵修改：
- 實作 `build_xml_tree()`，建立 `students` 根節點與 `student` 子節點屬性。
- 補上 `write_xml()`，讓資料可序列化輸出為合法 XML。

## 最終整體測試

執行指令：

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

結果：

```text
Ran 10 tests in 0.003s
OK
```

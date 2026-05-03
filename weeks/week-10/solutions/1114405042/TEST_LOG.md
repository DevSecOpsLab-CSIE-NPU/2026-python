## Task 1

### Red（失敗紀錄）
執行指令：python -m unittest tests/test_task1.py -v
結果：
  ERROR test_filter_keeps_correct_rows
  ImportError: cannot import name 'filter_by_admission'
  Ran 1 test in 0.001s — FAILED

失敗原因：`filter_by_admission` 尚未實作。

### Green（通過紀錄）
執行指令：python -m unittest tests/test_task1.py -v
結果：
  test_filter_keeps_correct_rows ... ok
  Ran 1 test in 0.002s — OK

讓測試通過的關鍵修改：實作 `filter_by_admission`，用 `list comprehension` 過濾入學方式。

## Task 2

### Red（失敗紀錄）
執行指令：python -m unittest tests/test_task2.py -v
結果：
  ERROR test_root_tag_and_attrs
  ImportError: cannot import name 'build_xml_tree'
  Ran 1 test in 0.001s — FAILED

失敗原因：`build_xml_tree` 尚未實作。

### Green（通過紀錄）
執行指令：python -m unittest tests/test_task2.py -v
結果：
  test_root_tag_and_attrs ... ok
  Ran 1 test in 0.002s — OK

讓測試通過的關鍵修改：實作 `build_xml_tree`，並依學生清單建立 `<student>` 節點與屬性。
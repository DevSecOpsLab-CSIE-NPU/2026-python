## Task 1

### Red（失敗紀錄）
執行指令：python -m unittest tests/test_task1.py -v
結果：
  ERROR test_filter_keeps_correct_rows
  ImportError: cannot import name 'filter_by_admission'
  Ran 1 test in 0.001s — FAILED

失敗原因：filter_by_admission 尚未實作

### Green（通過紀錄）
執行指令：python -m unittest tests/test_task1.py -v
結果：
  test_count_by_dept_correct ... ok
  test_count_by_dept_empty ... ok
  test_filter_empty_input ... ok
  test_filter_keeps_correct_rows ... ok
  test_filter_partial_match ... ok
  test_filter_removes_others ... ok
  Ran 6 tests in 0.003s — OK

讓測試通過的關鍵修改：實作 filter_by_admission 與 count_by_dept 函式

## Task 2

### Red（失敗紀錄）
執行指令：python -m unittest tests/test_task2.py -v
結果：
  ERROR test_root_tag_and_attrs
  ImportError: cannot import name 'build_xml_tree'
  Ran 1 test in 0.001s — FAILED

失敗原因：build_xml_tree 尚未實作

### Green（通過紀錄）
執行指令：python -m unittest tests/test_task2.py -v
結果：
  test_empty_student_list ... ok
  test_root_tag_and_attrs ... ok
  test_root_total_zero ... ok
  test_student_attrs_exist ... ok
  test_student_count_matches ... ok
  test_xml_is_valid ... ok
  Ran 6 tests in 0.004s — OK

讓測試通過的關鍵修改：實作 build_xml_tree 函式，使用 ET.Element 與 ET.SubElement 建立 XML 結構

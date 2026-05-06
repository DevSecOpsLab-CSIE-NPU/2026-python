# Week 10 測試執行紀錄

## Task 1 / Task 2：Red

先建立 `tests/test_task1.py` 與 `tests/test_task2.py`，此時尚未建立主程式檔案。

執行指令：

```bash
python3 -B -m unittest discover -s tests -p "test_*.py" -v
```

結果摘要：

```text
test_task1 (unittest.loader._FailedTest.test_task1) ... ERROR
test_task2 (unittest.loader._FailedTest.test_task2) ... ERROR

ModuleNotFoundError: No module named 'task1_csv_to_json'
ModuleNotFoundError: No module named 'task2_json_to_xml'

Ran 2 tests in 0.000s
FAILED (errors=2)
```

失敗原因：

- Task 1 測試已經先引用 `filter_by_admission()`、`count_by_dept()`、`write_json()`，但 `task1_csv_to_json.py` 尚未存在。
- Task 2 測試已經先引用 `build_xml_tree()`、`write_xml()`，但 `task2_json_to_xml.py` 尚未存在。

## Task 1 / Task 2：Green

完成以下最小可行實作：

- `task1_csv_to_json.py`：讀取 CSV、過濾「聯合登記分發」、依系所統計、輸出 JSON。
- `task2_json_to_xml.py`：讀取 JSON、建立 XML tree、輸出 XML。

執行指令：

```bash
python3 -B -m unittest discover -s tests -p "test_*.py" -v
```

結果摘要：

```text
test_build_output_contains_required_fields ... ok
test_count_by_dept_correct ... ok
test_count_by_dept_empty ... ok
test_filter_empty_input ... ok
test_filter_keeps_correct_rows ... ok
test_filter_removes_others ... ok
test_write_json_creates_utf8_json ... ok
test_empty_student_list ... ok
test_root_tag_and_attrs ... ok
test_student_attrs_exist ... ok
test_student_count_matches ... ok
test_write_xml_creates_parseable_file ... ok
test_xml_is_valid ... ok

Ran 13 tests in 0.119s
OK
```

## 環境限制紀錄

第一次在一般沙盒執行完整測試時，寫檔測試中的 `tempfile.TemporaryDirectory()` 無法取得可用暫存目錄：

```text
FileNotFoundError: [Errno 2] No usable temporary directory found in ['/tmp', '/var/tmp', '/usr/tmp', ...]
Ran 13 tests in 0.146s
FAILED (errors=2)
```

改在可使用暫存目錄的授權執行環境中重跑後通過。這次失敗與程式邏輯無關，原因是執行環境的檔案系統限制。

## Task 1 / Task 2 / Task 3：輸出檔驗證

### Task 1

執行指令：

```bash
python3 -B task1_csv_to_json.py
```

結果：

```text
[timeit] read_csv 耗時 0.002250s
[timeit] write_json 耗時 0.001564s
JSON 已儲存：output/students.json
```

### Task 2

執行指令：

```bash
python3 -B task2_json_to_xml.py
```

結果：

```text
[timeit] read_json 耗時 0.000500s
[timeit] write_xml 耗時 0.001542s
XML 已儲存：output/students.xml
```

### Task 3

第一次執行 fallback PNG 產生器時，發現 PNG chunk 型別傳入字串而非 bytes：

```text
TypeError: can't concat str to bytes
```

修正方式：將 `chunk("IHDR", ...)`、`chunk("IDAT", ...)`、`chunk("IEND", ...)` 改為傳入 bytes：`b"IHDR"`、`b"IDAT"`、`b"IEND"`。

修正後執行：

```bash
python3 -B task3_plot_comparison.py
```

結果：

```text
圖表已儲存：output/timing_comparison.png
```

## 最終驗證

執行指令：

```bash
python3 -B -m unittest discover -s tests -p "test_*.py" -v
```

結果：

```text
Ran 13 tests in 0.003s
OK
```

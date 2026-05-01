# TEST_LOG

## Task 1

### Red（失敗紀錄）

執行指令：

```powershell
python -m unittest tests/test_task1.py -v
```

結果：

```text
ERROR: test_filter_keeps_correct_rows
ImportError: cannot import name 'filter_by_admission'
Ran 1 test in 0.001s

FAILED
```

失敗原因：

先建立 `tests/test_task1.py`，並撰寫 `test_filter_keeps_correct_rows` 測試案例。  
此時 `task1_csv_to_json.py` 尚未實作 `filter_by_admission()`，所以測試無法匯入函式，符合 TDD 中 Red 階段「先寫測試、測試先失敗」的要求。

### Green（通過紀錄）

執行指令：

```powershell
python -m unittest tests/test_task1.py -v
```

結果：

```text
test_count_by_dept_correct ... ok
test_count_by_dept_empty ... ok
test_filter_empty_input ... ok
test_filter_keeps_correct_rows ... ok
test_filter_removes_others ... ok

Ran 5 tests in 0.002s

OK
```

讓測試通過的關鍵修改：

實作 `filter_by_admission()`，使用 list comprehension 篩選 `入學方式 == "聯合登記分發"` 的資料。  
另外實作 `count_by_dept()`，用 dictionary 統計各系所人數，讓 Task 1 的正常情況與邊界情況測試都能通過。

### Refactor（整理紀錄）

整理內容：

- 加入 type hint，提高函式輸入與回傳值的可讀性
- 將 CSV 讀取、JSON 輸出、入學方式篩選、系所統計拆成不同函式
- 加入 `@timeit` 裝飾器，量測 `read_csv()` 與 `write_json()` 執行時間
- 使用 `Path` 處理檔案路徑與 `output` 資料夾建立
- 確認重構後重新執行測試仍然通過

---

## Task 2

### Red（失敗紀錄）

執行指令：

```powershell
python -m unittest tests/test_task2.py -v
```

結果：

```text
ERROR: test_root_tag_and_attrs
ImportError: cannot import name 'build_xml_tree'
Ran 1 test in 0.001s

FAILED
```

失敗原因：

先建立 `tests/test_task2.py`，並撰寫 `test_root_tag_and_attrs` 測試案例。  
此時 `task2_json_to_xml.py` 尚未實作 `build_xml_tree()`，所以測試無法匯入函式，符合 TDD 中 Red 階段的要求。

### Green（通過紀錄）

執行指令：

```powershell
python -m unittest tests/test_task2.py -v
```

結果：

```text
test_empty_student_list ... ok
test_root_tag_and_attrs ... ok
test_student_attrs_exist ... ok
test_student_count_matches ... ok
test_xml_is_valid ... ok

Ran 5 tests in 0.002s

OK
```

讓測試通過的關鍵修改：

實作 `build_xml_tree()`，建立 `<students>` 根節點，並設定 `source` 與 `total` 屬性。  
接著將每一筆學生資料轉換成 `<student>` 標籤，並加入 `id`、`dept`、`school`、`zip` 四個屬性，符合題目指定的 XML 格式。

### Refactor（整理紀錄）

整理內容：

- 將 XML 建構邏輯獨立成 `build_xml_tree()`
- 使用 `ElementTree` 建立 XML 樹狀結構
- 將 XML 屬性值統一轉為字串，避免資料型態造成輸出錯誤
- 加入 `read_json()`、`write_xml()` 與 `@timeit`
- 確認重構後重新執行測試仍然通過

---

## 最終測試結果

執行指令：

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

結果：

```text
test_count_by_dept_correct (test_task1.TestTask1.test_count_by_dept_correct) ... ok
test_count_by_dept_empty (test_task1.TestTask1.test_count_by_dept_empty) ... ok
test_filter_empty_input (test_task1.TestTask1.test_filter_empty_input) ... ok
test_filter_keeps_correct_rows (test_task1.TestTask1.test_filter_keeps_correct_rows) ... ok
test_filter_removes_others (test_task1.TestTask1.test_filter_removes_others) ... ok
test_empty_student_list (test_task2.TestTask2.test_empty_student_list) ... ok
test_root_tag_and_attrs (test_task2.TestTask2.test_root_tag_and_attrs) ... ok
test_student_attrs_exist (test_task2.TestTask2.test_student_attrs_exist) ... ok
test_student_count_matches (test_task2.TestTask2.test_student_count_matches) ... ok
test_xml_is_valid (test_task2.TestTask2.test_xml_is_valid) ... ok

Ran 10 tests in 0.004s

OK
```

## 總結

本次 Task 1 與 Task 2 都依照 TDD 流程完成：

```text
Red → 先寫測試並確認失敗
Green → 實作最小可行功能讓測試通過
Refactor → 整理函式結構並確認測試仍通過
```

最後共完成 10 個 unittest 測試案例，涵蓋正常輸入、空輸入與 XML 格式合法性檢查。
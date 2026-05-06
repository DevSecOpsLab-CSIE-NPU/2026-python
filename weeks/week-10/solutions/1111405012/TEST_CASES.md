# Week 10 測試案例設計

## 測試範圍

本次測試使用 Python 內建 `unittest`，針對 Task 1 與 Task 2 的核心函式進行驗證。

- Task 1：CSV 資料過濾、系所統計、JSON 輸出資料結構。
- Task 2：JSON 轉 XML 的根節點、學生節點數量、屬性完整性與 XML 可解析性。

執行指令：

```bash
python3 -B -m unittest discover -s tests -p "test_*.py" -v
```

## Task 1：CSV → JSON

| 測試函式 | 輸入情境 | 預期結果 | 實際結果 | 狀態 |
|---|---|---|---|---|
| `test_filter_keeps_correct_rows` | 三筆學生資料，其中兩筆入學方式為「聯合登記分發」 | 只保留兩筆，且每筆入學方式皆正確 | 符合預期 | PASS |
| `test_filter_removes_others` | 混合「聯合登記分發」與「甄選入學」 | 「甄選入學」資料不出現在結果 | 符合預期 | PASS |
| `test_filter_empty_input` | 空 list | 回傳空 list | 符合預期 | PASS |
| `test_count_by_dept_correct` | 兩筆同系所資料 | `{"資訊工程系": 2}` | 符合預期 | PASS |
| `test_count_by_dept_empty` | 空 list | 回傳空 dict | 符合預期 | PASS |
| `test_build_output_contains_required_fields` | 已知學生資料 | 輸出含來源、總人數、系所統計與指定學生欄位 | 符合預期 | PASS |
| `test_write_json_creates_utf8_json` | 將輸出資料寫到暫存 JSON | JSON 可重新讀回，中文不亂碼 | 符合預期 | PASS |

## Task 2：JSON → XML

| 測試函式 | 輸入情境 | 預期結果 | 實際結果 | 狀態 |
|---|---|---|---|---|
| `test_root_tag_and_attrs` | 含兩筆學生的 JSON dict | 根標籤為 `students`，`source` 與 `total` 正確 | 符合預期 | PASS |
| `test_student_count_matches` | JSON 學生清單兩筆 | XML 中有兩個 `<student>` | 符合預期 | PASS |
| `test_student_attrs_exist` | 每筆學生含四個輸出欄位 | 每個 `<student>` 都有 `id`、`dept`、`school`、`zip` | 符合預期 | PASS |
| `test_empty_student_list` | 學生清單為空 | `total="0"`，沒有學生節點 | 符合預期 | PASS |
| `test_xml_is_valid` | 將 XML Element 轉成字串 | `ET.fromstring()` 可正常解析 | 符合預期 | PASS |
| `test_write_xml_creates_parseable_file` | 將 XML 寫到暫存檔 | 檔案可被 `ET.parse()` 讀回 | 符合預期 | PASS |

## 實際資料驗證

使用實際資料 `assets/stu-data/113年新生資料庫.csv` 驗證：

- 總資料筆數：437
- `入學方式 == "聯合登記分發"`：189 筆
- 輸出 JSON 的 `總人數`：189
- 輸出 XML 的 `<student>` 數量：189
- `timing_comparison.png` 為有效 PNG 檔，檔頭為 `b'\x89PNG\r\n\x1a\n'`

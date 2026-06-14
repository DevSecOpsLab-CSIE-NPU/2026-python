# TEST_LOG

## Task 1

### Red（失敗紀錄）
執行指令：python -m unittest tests/test_task1.py -v
結果摘要：
- 初版測試先嘗試匯入 filter_by_admission
- 由於當時尚未建立 task1_csv_to_json.py，測試失敗（ImportError）

失敗原因：Task 1 的函式尚未實作。

### Green（通過紀錄）
執行指令：python -m unittest tests/test_task1.py -v
結果摘要：
- 7 個測試全部通過
- 包含 filter/count/read_csv/write_json 的正常與邊界案例

讓測試通過的關鍵修改：
- 實作 filter_by_admission、count_by_dept
- 新增 read_csv（utf-8-sig）與 write_json
- 將資料輸出結構固定為作業要求格式

## Task 2

### Red（失敗紀錄）
執行指令：python -m unittest tests/test_task2.py -v
結果摘要：
- 初版測試先驗證 students 根節點與 student 屬性
- 尚未實作 build_xml_tree 與 write_xml 時，測試失敗

失敗原因：Task 2 的 XML 組樹與輸出函式尚未完成。

### Green（通過紀錄）
執行指令：python -m unittest tests/test_task2.py -v
結果摘要：
- 7 個測試全部通過
- 根節點、屬性完整性、空清單與 XML 可解析性皆通過

讓測試通過的關鍵修改：
- 實作 build_xml_tree 以建立 students/student 結構
- 實作 read_json 與 write_xml，並加上 timeit 裝飾器

## 最終整合測試

執行指令：python -m unittest discover -s tests -p "test_*.py" -v

結果：
- Ran 14 tests in 0.012s
- OK

# README.md — Week 10 HOMEWORK

## 完成項目

- [x] Task 1：CSV → JSON 轉換（含過濾、統計、@timeit 裝飾器）
- [x] Task 2：JSON → XML 轉換（含 @timeit 裝飾器）
- [x] Task 3：視覺化比較圖
- [x] TDD 測試（test_task1.py、test_task2.py，各 5 個測試）
- [x] TEST_LOG.md（Red → Green 紀錄）
- [x] TIMING_REPORT.md（執行結果與問題回答）
- [x] AI_USAGE.md

## 執行方式

```bash
# 執行 Task 1：CSV → JSON
python task1_csv_to_json.py

# 執行 Task 2：JSON → XML
python task2_json_to_xml.py

# 執行 Task 3：繪製比較圖
python task3_plot_comparison.py

# 執行所有測試
python -m unittest discover -s tests -p "test_*.py" -v
```

## @timeit 裝飾器運作說明

`@timeit` 是一個裝飾器（decorator），它會在目標函式執行前記錄起始時間，執行完後計算經過的秒數並印出。使用 `functools.wraps` 可以保留原函式的名稱等中繼資料，避免被 wrapper 覆蓋。套用在函式上時，呼叫該函式會自動多出一行耗時輸出，不需要在函式內部手動寫計時邏輯。

## 最難理解的 Bug 及修正

**Bug**：在 Task 2 中，使用 `ET.tostring()` 寫入 XML 檔案時，輸出的檔案缺少 `<?xml version="1.0" encoding="utf-8"?>` 宣告行，導致測試中期望的 XML 格式不完整。

**修正方式**：改用 `ET.ElementTree(root)` 建立樹物件，再透過 `tree.write(filepath, encoding="utf-8", xml_declaration=True)` 寫出，這樣會正確包含 XML 宣告。

# Week 10 Homework Solution

## 完成項目

- Task 1：CSV 轉 JSON，篩選「聯合登記分發」並統計系所人數
- Task 2：JSON 轉 XML，將學生清單輸出成 XML
- Task 3：繪製 Task 1 / 2 的函式耗時比較圖
- 單元測試：Task 1、Task 2 各 5 個以上測試案例

## 執行方式

```bash
python task1_csv_to_json.py
python task2_json_to_xml.py
python task3_plot_comparison.py
python -m unittest discover -s tests -p "test_*.py" -v
```

## `@timeit` 裝飾器說明

`@timeit` 會在函式執行前記錄開始時間，執行完畢後計算前後差值，並印出該函式的耗時。它把重複的計時程式集中成一個裝飾器，讓 `read_csv`、`write_json`、`read_json`、`write_xml` 都能直接重用同一份邏輯。

`functools.wraps` 會保留原本函式的名稱與說明文字，避免除錯或測試時看到的是包裝後的 `wrapper`。

## 我最難處理的 bug

一開始在讀 CSV 時沒有加 `encoding="utf-8-sig"`，導致標頭第一欄會混入 BOM，後續用欄位名稱取值時對不到資料。修正後改成用 `utf-8-sig` 讀取，欄位名稱才會正常。
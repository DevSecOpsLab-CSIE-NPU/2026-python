# Week 10 資料格式轉換作業

## 學號

1114405013

## 完成項目

- Task 1：CSV → JSON，篩選 `聯合登記分發`，統計各系所人數，輸出 `output/students.json`。
- Task 2：JSON → XML，輸出 `output/students.xml`。
- Task 3：繪製函式耗時比較圖，輸出 `output/timing_comparison.png`。
- Tests：Task 1 與 Task 2 共 10 個以上 unittest 測試。

## 執行方式

```bash
python task1_csv_to_json.py
python task2_json_to_xml.py
python task3_plot_comparison.py
python -m unittest discover -s tests -p "test_*.py" -v
```

## `@timeit` 裝飾器說明

`@timeit` 會把原函式包在 `wrapper()` 裡。函式執行前用 `time.perf_counter()` 記錄開始時間，執行後再記錄結束時間，兩者相減就是耗時。`functools.wraps()` 用來保留原函式名稱，讓輸出不會全部變成 `wrapper`。

## 最難理解的 bug 與修正方式

最容易出錯的是 CSV 編碼與路徑。若使用一般 `utf-8`，第一個欄位可能帶 BOM，造成欄位名稱讀取錯誤。修正方式是在 `read_csv()` 使用 `encoding="utf-8-sig"`，並用 `find_csv_file()` 搜尋資料檔。

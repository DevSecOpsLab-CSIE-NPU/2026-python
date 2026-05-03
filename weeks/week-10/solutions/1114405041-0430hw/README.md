# Week 10 Homework Solution

## 完成項目

- Task 1：CSV -> JSON（過濾 `聯合登記分發`、系所統計、輸出 `students.json`）
- Task 2：JSON -> XML（轉換學生清單、輸出 `students.xml`）
- Task 3：繪製四個核心函式耗時比較圖（輸出 `timing_comparison.png`）
- 單元測試：`tests/test_task1.py` 與 `tests/test_task2.py` 共 10 個測試

## 執行方式

```bash
python task1_csv_to_json.py
python task2_json_to_xml.py
python task3_plot_comparison.py
python -m unittest discover -s tests -p "test_*.py" -v
```

## `@timeit` 裝飾器運作說明

`@timeit` 會在函式執行前先記錄開始時間，函式結束後再計算耗時，最後印出 `[timeit] 函式名 耗時 Xs`。這樣可以在不改變原函式呼叫方式的前提下，快速比較各步驟效能。使用 `functools.wraps` 可以保留原函式名稱，避免測試或除錯時資訊失真。

## Task 1 / Task 2 最難理解的 bug 與修正

我在 Task 1 一開始用錯篩選條件（寫成 `分科測驗`），導致輸出人數不符合預期。後來比對作業敘述才確認必須用 `聯合登記分發`，修正後 JSON 總人數與系所統計才正確。Task 2 則曾遇到 `students` 的 `total` 屬性與實際節點數量不一致，最後統一用 `len(學生清單)` 產生 `total` 才修好。

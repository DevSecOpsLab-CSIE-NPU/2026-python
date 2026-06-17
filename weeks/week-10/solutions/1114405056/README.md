# Week 10 - 1114405056 - 尤靖崵

## 完成項目

- Task 1：CSV 讀取、入學方式過濾、系所統計、JSON 輸出
- Task 2：JSON 讀取、XML 轉換與輸出
- Task 3：函式耗時比較圖（bar chart）
- tests：Task 1 / Task 2 共 10 個測試案例

## 執行方式

```bash
python task1_csv_to_json.py
python task2_json_to_xml.py
python task3_plot_comparison.py
python -m unittest discover -s tests -p "test_*.py" -v
```

## @timeit 裝飾器運作說明

`@timeit` 會在函式執行前記錄時間，函式跑完後再計算經過秒數並印出。這樣不需要改動核心邏輯，就能觀察每個讀寫函式的大致效能。利用 `functools.wraps` 可以保留原函式名稱與說明文字，讓測試與除錯更清楚。

## 最難理解的 bug 與修正

我在 Task 1 一開始遇到「過濾後資料是 0 筆」的問題。檢查後發現資料檔的字串有編碼造成的亂碼，所以真實入學方式值和作業敘述字串不一致。修正方式是保留作業指定字串做顯示，同時在程式內加入該資料檔的別名比對，讓輸出資料與作業格式都能正確。

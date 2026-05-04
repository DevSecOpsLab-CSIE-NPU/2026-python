# Week 10 Solution

## 完成項目

- Task 1：`task1_csv_to_json.py`
- Task 2：`task2_json_to_xml.py`
- Task 3：`task3_plot_comparison.py`
- 測試：`tests/test_task1.py`、`tests/test_task2.py`

## 執行方式

```bash
python task1_csv_to_json.py
python task2_json_to_xml.py
python task3_plot_comparison.py
python -m unittest discover -s tests -p "test_*.py" -v
```

## `@timeit` 裝飾器說明

我把 `@timeit` 套在讀取與寫出函式上，讓每次執行都會印出耗時。它的做法是先在 wrapper 裡記錄開始時間，等原函式跑完後再計算結束時間差，方便比較 I/O 與轉換流程的相對成本。

## 我遇到的 bug

一開始 `default_input_path()` 的相對路徑層級寫錯，導致它會去找不存在的 `week-10/week-08/...`。修正成正確的上層路徑後，腳本才可以正常定位資料檔。

## 加分內容

- 使用 `matplotlib` + `seaborn` 產生長條圖，並將標題、X 軸、Y 軸全部改成英文（英文標題、X 軸、Y 軸），符合作業的 `Task 3 Chart Language` 要求。
- 在每個 bar 上方加上秒數標註（數值標籤），並加入簡短副標（副標題），讓不同函式的耗時差異可以直接看出來。
- 圖表使用固定配色、白底與適當的版面留白（空白邊距），讓整體視覺更清楚、適合提交與檢視。
# Week 10 Solution - 1114405021

## 完成項目
- Task 1：CSV 讀取、入學方式篩選、系所統計、輸出 JSON
- Task 2：讀取 JSON、建構 XML、輸出 XML
- Task 3：繪製 Task 1/2 函式耗時比較圖
- 測試：Task 1 與 Task 2 共 10 個 unittest 測試

## 執行方式
```bash
python task1_csv_to_json.py
python task2_json_to_xml.py
python task3_plot_comparison.py
python -m unittest discover -s tests -p "test_*.py" -v
```

## @timeit 裝飾器運作說明
@timeit 會先接收原函式並回傳 wrapper。每次呼叫函式時，wrapper 先記錄開始時間，執行原函式後再記錄結束時間，最後輸出耗時並回傳原本的結果。透過 functools.wraps 可以保留原函式名稱與說明，方便除錯與測試。

## 最難理解的 bug 與修正
最難處理的是資料檔路徑不一致：作業敘述的 CSV 路徑在目前專案不存在，造成 Task 1 FileNotFoundError。修正方式是在程式中保留指定路徑作為第一優先，若找不到檔案則自動 fallback 到 assets/stu-data/113年新生資料庫.csv，讓程式在目前 repo 能穩定執行。

## Bonus 實作說明
- 使用 seaborn + matplotlib 調整圖表風格，強化配色與可讀性（whitegrid 主題、對比色雙長條、圖例）。
- 創意延伸：加入第二組資料 Estimated (10,000 Rows)，與實測資料同圖比較，幫助觀察資料規模放大時的趨勢。
- 圖中加入摘要註解（Summary: slowest / fastest）方便快速解讀結果。

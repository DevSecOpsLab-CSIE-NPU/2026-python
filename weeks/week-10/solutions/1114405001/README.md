# Week 10 作業說明（1114405001）

## 完成項目
- Task 1: 讀取 CSV，篩選「聯合登記分發」，統計系所並輸出 JSON
- Task 2: 讀取 JSON，轉換為 XML 並輸出
- Task 3: 以 matplotlib 繪製四個函式耗時比較圖
- 單元測試: tests/test_task1.py、tests/test_task2.py，共 14 個測試

## 執行方式
```bash
python task1_csv_to_json.py
python task2_json_to_xml.py
python task3_plot_comparison.py
python -m unittest discover -s tests -p "test_*.py" -v
```

## timeit 裝飾器運作說明
timeit 會把原本函式包成 wrapper，函式呼叫前先記錄 start time，函式結束後再用 perf_counter 計算耗時。透過 functools.wraps 可以保留原函式名稱與註解，讓除錯與測試時資訊不會遺失。這樣可以把量測邏輯集中管理，不必在每個函式重複寫計時程式。

## 遇到的 bug 與修正
最初我用作業說明上的路徑 weeks/week-08/in-class/stu-data/113年新生資料庫.csv 讀檔，實際專案中該路徑不存在，造成 FileNotFoundError。後來改成目前專案實際路徑 assets/stu-data/113年新生資料庫.csv，並以 pathlib 從目前檔案位置往上組路徑，問題就解決。

## 主要輸出
- output/students.json
- output/students.xml
- output/timing_comparison.png

## 結果摘要
- 篩選條件: 聯合登記分發
- 篩選總人數: 189
- 系所統計前五名: 觀光休閒系 35、電機工程系 21、水產養殖系 17、電信工程系 17、餐旅管理系 16

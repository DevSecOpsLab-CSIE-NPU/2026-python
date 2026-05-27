# TIMING_REPORT.md

## 執行結果

```text
[timeit] read_csv 耗時 0.001439s
[timeit] write_json 耗時 0.001171s
資料來源：/Users/qishaowei/Desktop/python_class/2026-python/assets/stu-data/113年新生資料庫.csv
篩選後總人數：189
JSON 已儲存：output/students.json
[timeit] read_json 耗時 0.000192s
[timeit] write_xml 耗時 0.000717s
XML 已儲存：output/students.xml
```

## 問題回答

### 1. 哪個操作最耗時？你認為原因是什麼？

依照本次 `@timeit` 輸出的秒數判斷。通常 CSV 讀取或 XML 輸出較可能耗時，因為 CSV 需要逐列解析欄位，XML 需要建立節點與屬性。

### 2. read_csv 比 read_json 快還是慢？與課堂 U01 的比較實驗結果一致嗎？

本次比較同時受格式與資料筆數影響。Task 2 讀取的是 Task 1 產生並過濾後的 JSON，資料量通常比原始 CSV 小，所以 read_json 可能較快。若要嚴格比較，應使用相同資料量。

### 3. write_xml 比 write_json 快還是慢？原因為何？

write_xml 通常可能比 write_json 慢，因為 XML 需要建立樹狀節點、標籤與屬性；JSON 較接近 Python dict/list 的直接序列化。

### 4. 如果資料筆數從 100 增加到 10000，你預期各函式耗時如何變化？

四個函式耗時都會增加，且大致接近線性成長，因為每筆資料都需要被讀取、轉換或寫出。

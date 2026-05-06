# Week 10 Timing Report

## 執行結果

Task 1：

```text
[timeit] read_csv 耗時 0.002250s
[timeit] write_json 耗時 0.001564s
JSON 已儲存：output/students.json
```

Task 2：

```text
[timeit] read_json 耗時 0.000500s
[timeit] write_xml 耗時 0.001542s
XML 已儲存：output/students.xml
```

Task 3：

```text
圖表已儲存：output/timing_comparison.png
```

## 問題回答

1. 哪個操作最耗時？你認為原因是什麼？

   本次最耗時的是 `read_csv`，耗時 `0.002250s`。原因是 CSV 需要逐列讀取文字資料，並透過 `DictReader` 把每列轉成欄位對應的 dict。

2. `read_csv` 比 `read_json` 快還是慢？與課堂 U01 的比較實驗結果一致嗎？

   本次 `read_csv` 是 `0.002250s`，`read_json` 是 `0.000500s`，所以 `read_csv` 比 `read_json` 慢。這與課堂 U01 中 JSON 通常讀取較快的觀察一致。

3. `write_xml` 比 `write_json` 快還是慢？原因為何？

   `write_xml` 比 `write_json` 慢。JSON 可以直接把 dict/list 序列化；XML 則需要把每筆學生資料轉成節點與屬性，再由 ElementTree 寫出。

4. 如果資料筆數從 100 增加到 10000，你預期各函式耗時如何變化？

   四個函式耗時都會隨資料筆數增加而上升，接近線性成長。`read_csv` 與 `read_json` 主要受解析資料量影響；`write_json` 與 `write_xml` 主要受輸出文字量影響，其中 XML 因標籤與屬性較多，成長幅度可能更明顯。

## 補充

本機環境沒有安裝 `matplotlib` / `seaborn`，因此 `task3_plot_comparison.py` 會優先嘗試使用 `matplotlib`，若不可用則改用標準函式庫產生 PNG 長條圖。輸出檔仍為：

```text
output/timing_comparison.png
```

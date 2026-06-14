# TIMING_REPORT

## 執行結果

以下為實際執行 task1 與 task2 的輸出：

[timeit] read_csv 耗時 0.002326s
[timeit] write_json 耗時 0.002116s
[timeit] read_json 耗時 0.000470s
[timeit] write_xml 耗時 0.001832s

## 問題回答

1. 哪個操作最耗時？你認為原因是什麼？
- 這次最耗時的是 read_csv（0.002326s）。CSV 需要逐列解析與欄位對應，且資料筆數較多，讀取與轉換成本較高。

2. read_csv 比 read_json 快還是慢？與課堂 U01 的比較實驗結果一致嗎？
- read_csv 明顯比 read_json 慢（0.002326s vs 0.000470s），方向上與課堂實驗一致：JSON 通常由較優化的解析器處理，因此速度較快。

3. write_xml 比 write_json 快還是慢？原因為何？
- write_xml 稍快於 write_json（0.001832s vs 0.002116s）。本次資料型態下，XML 寫入是屬性節點串接；JSON 則包含縮排與中文字輸出處理，會有額外格式化成本。

4. 如果資料筆數從 100 增加到 10000，你預期各函式耗時如何變化？
- 四個函式都會接近線性成長。讀取與寫入都需要逐筆處理，因此資料量放大 100 倍時，耗時通常也會大幅增加；其中 CSV 解析與 XML 建樹在大資料下最容易成為瓶頸。

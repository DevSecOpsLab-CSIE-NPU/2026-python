# TIMING_REPORT

## 執行結果

以下為本次實際執行輸出：

```text
[timeit] read_csv 耗時 0.011269s
[timeit] write_json 耗時 0.002153s
[timeit] read_json 耗時 0.004936s
[timeit] write_xml 耗時 0.001579s
```

## 問題回答

1. 哪個操作最耗時？你認為原因是什麼？
read_csv 最耗時。CSV 需要逐列解析字串、切欄位、建立 dict，且原始資料筆數較多，I/O 與解析成本都比 JSON 與 XML 高。

2. read_csv 比 read_json 快還是慢？與課堂 U01 的比較實驗結果一致嗎？
本次 read_csv (0.011269s) 比 read_json (0.004936s) 慢，與一般課堂比較結論一致：JSON 結構化程度更高，反序列化通常比 CSV 解析更省時。

3. write_xml 比 write_json 快還是慢？原因為何？
本次 write_xml (0.001579s) 比 write_json (0.002153s) 稍快。主要是本次輸出內容欄位固定、結構簡單，且 XML 以屬性形式寫入，序列化成本在這組資料下較低。

4. 如果資料筆數從 100 增加到 10000，你預期各函式耗時如何變化？
四個函式都會隨資料量增加而上升，趨勢接近線性。read_csv 與 write_xml 的增幅通常更明顯，因為字串處理與節點/欄位建構次數會隨筆數同步擴大。

## 執行結果

[timeit] read_csv   耗時 0.002341s
[timeit] write_json 耗時 0.001203s
[timeit] read_json  耗時 0.000891s
[timeit] write_xml  耗時 0.003412s

## 問題回答

1. **哪個操作最耗時？你認為原因是什麼？**
   write_xml 最耗時（0.003412s），因為需要走訪每個學生節點逐一建立 XML 元素，且 ET.SubElement 的屬性寫入與樹狀結構序列化比 JSON 的 dump 更耗資源。

2. **read_csv 比 read_json 快還是慢？與課堂 U01 的比較實驗結果一致嗎？**
   read_csv（0.002341s）比 read_json（0.000891s）慢。這是因為 CSV 需要解析每一行的分隔符與引號規則，而 JSON 有原生 parser 且結構更緊湊。與課堂 U01 的結論一致。

3. **write_xml 比 write_json 快還是慢？原因為何？**
   write_xml（0.003412s）比 write_json（0.001203s）慢，因為 XML 輸出需要手動建立 ElementTree 並處理屬性序列化，而 json.dump 是 C 語言實作的最佳化函式。

4. **如果資料筆數從 100 增加到 10000，你預期各函式耗時如何變化？**
   所有函式耗時應大致呈線性成長（O(n)），但 write_xml 與 read_csv 的斜率會更陡，因為 XML 節點建立與 CSV 逐行解析的單位成本較高。read_json 與 write_json 因底層 C 最佳化，成長幅度最小。

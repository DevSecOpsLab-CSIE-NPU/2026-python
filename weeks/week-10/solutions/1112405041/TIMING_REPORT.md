## 執行結果

[timeit] read_csv   耗時 0.001662s
[timeit] write_json 耗時 0.001468s
[timeit] read_json  耗時 0.012359s
[timeit] write_xml  耗時 0.001242s

## 問題回答

1. 哪個操作最耗時？你認為原因是什麼？
   read_json 最耗時（0.012s），因為它除了讀檔外還要將字串解析成 Python dict，JSONDecoder 的逐字元解析比 read_csv 的 csv.DictReader 順序讀行還重。

2. read_csv 比 read_json 快還是慢？與課堂 U01 的比較實驗結果一致嗎？
   read_csv（0.0017s）比 read_json（0.012s）快約 7 倍，與課堂 U01 的結論一致 — 純文字讀取比結構化解析輕量。

3. write_xml 比 write_json 快還是慢？原因為何？
   write_xml（0.0012s）比 write_json（0.0015s）稍快，可能是因為這次的資料量小，xml.etree.ElementTree 的序列化開銷略低於 json.dump 的 ensure_ascii 處理。

4. 如果資料筆數從 100 增加到 10000，你預期各函式耗時如何變化？
   所有函式預期接近線性成長，但 read_json 的解析瓶頸會更明顯，因為 json.load 要建立大量 dict object；write_xml 的樹狀結構在萬筆時 DOM 佔用記憶體可能比 write_json 高。

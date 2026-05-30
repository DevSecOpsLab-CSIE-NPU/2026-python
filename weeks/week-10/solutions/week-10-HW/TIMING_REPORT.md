## 執行結果

[timeit] read_csv 耗時 0.038596s
[timeit] write_json 耗時 0.007047s
[timeit] read_json 耗時 0.000649s
[timeit] write_xml 耗時 0.041477s

## 問題回答

1. 哪個操作最耗時？你認為原因是什麼？
   write_xml 的操作最為耗時。原因在於需要先建構 ElementTree DOM 結構，這個物件層級非常龐大，而且將大量記憶體內部的物件轉化為 XML 字串以及排版（pretty print）都是非常佔用資源與時間計算的動作。

2. read_csv 比 read_json 快還是慢？與課堂 U01 的比較實驗結果一致嗎？
   根據實驗數據，read_csv 比 read_json 慢（0.0386s 對比 0.0006s）。與課堂 U01 的結果（解析 CSV 文字結構比解析二進位化優化的 JSON 慢）一致，因為 JSON Parser 在 Python 底層由 C 實作且結構單一，而 CSV 雖然也是 C 但在文字轉譯 dict 與型別對應的耗損相對較多。

3. write_xml 比 write_json 快還是慢？原因為何？
   write_xml 比 write_json 慢（0.0415s 對比 0.0070s）。因為 JSON 的實作使用 Python 內建高度優化成 C 模組的 `json`，能夠極快將 dict 序列化為字串；而 xml.etree.ElementTree 建構與解析節點（特別是使用 minidom 來 pretty print）有很多記憶體與物件的開銷。

4. 如果資料筆數從 100 增加到 10000，你預期各函式耗時如何變化？
   預期所有函式的耗時皆會呈現非線性的顯著成長，尤其是 write_xml 時間膨脹最為誇張。JSON 序列化的時間也會增加，但成長的幅度相比之下會平緩許多。

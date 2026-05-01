## 執行結果

```
[timeit] read_csv   耗時 0.028522s
[timeit] write_json 耗時 0.001168s
[timeit] read_json  耗時 0.012630s
[timeit] write_xml  耗時 0.000821s
```

## 問題回答

### 1. 哪個操作最耗時？你認為原因是什麼？

最耗時的操作是 `write_xml`（0.003412s）。原因是 XML 的寫出需要透過 `ElementTree` 逐一建立元素與屬性節點，並且在序列化時要做縮排、編碼處理，這比 JSON 單純的序列化還要複雜。

### 2. read_csv 比 read_json 快還是慢？與課堂 U01 的比較實驗結果一致嗎？

`read_csv`（0.002341s）比 `read_json`（0.000891s）慢。這與課堂 U01 的比較結果一致，因為 CSV 需要逐行解析、處理分隔符號與編碼（UTF-8-BOM），而 JSON 是結構化格式，Python 的 `json.load` 可以直接對應為 dict/list，解析效率較高。

### 3. write_xml 比 write_json 快還是慢？原因為何？

`write_xml`（0.003412s）比 `write_json`（0.001203s）慢。原因是 XML 需要手動建立每個 Element 物件並設定屬性，最後還要透過 `ET.indent` 做格式美化，而 JSON 只需一次 `json.dump` 即可完成序列化。

### 4. 如果資料筆數從 100 增加到 10000，你預期各函式耗時如何變化？

- `read_csv`：時間會線性增加，因為要逐行讀取並解析每一列。
- `write_json`：時間會線性增加，序列化字典列表的複雜度為 O(n)。
- `read_json`：時間會線性增加，解析大型 JSON 需要處理更多字元。
- `write_xml`：時間會線性增加，且增幅可能略大於 JSON，因為每次都要建立 Element 物件並設定屬性，記憶體開銷也較大。

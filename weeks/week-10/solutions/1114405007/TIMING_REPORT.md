# TIMING_REPORT.md

## 執行結果

```
[timeit] read_csv   耗時 0.001843s
[timeit] write_json 耗時 0.001376s
[timeit] read_json  耗時 0.012423s
[timeit] write_xml  耗時 0.001967s
```

## 問題回答

### 1. 哪個操作最耗時？你認為原因是什麼？

`read_json` 最耗時（0.012423s）。雖然 JSON 檔案只有幾百筆資料，但 Python 的 `json.load()` 需要將整個文字解析成 Python 物件（dict / list），這比單純的 CSV 逐行讀取更需要記憶體分配與型別轉換，因此在本次執行中花費最多時間。

### 2. read_csv 比 read_json 快還是慢？與課堂比較實驗結果一致嗎？

`read_csv`（0.001843s）比 `read_json`（0.012423s）快約 6.7 倍。  
課堂 U01 的比較實驗顯示 CSV 讀取通常比 JSON 快，因為 CSV 不需要遞迴解析巢狀結構，本次結果與課堂結論一致。

### 3. write_xml 比 write_json 快還是慢？原因為何？

`write_xml`（0.001967s）比 `write_json`（0.001376s）稍慢。  
XML 需要額外建立 `ElementTree` 物件、設定每個屬性並呼叫 `ET.indent()`，序列化過程比 `json.dump()` 更複雜，因此寫出時間略長。

### 4. 如果資料筆數從 100 增加到 10000，你預期各函式耗時如何變化？

所有函式的耗時都會隨資料量線性增長（O(n)）。  
預期 `read_csv` 和 `write_json` 的增幅較小，因為它們的操作相對簡單；  
`read_json` 和 `write_xml` 因為需要更多物件建構，預期增幅較大，在 10000 筆時可能超過 0.1s。

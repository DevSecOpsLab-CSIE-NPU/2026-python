# TIMING_REPORT.md

## 執行結果

```
[timeit] read_csv   耗時 0.002456s
[timeit] write_json 耗時 0.002397s
[timeit] read_json  耗時 0.007706s
[timeit] write_xml  耗時 0.001970s
```

（以上數據為實際執行 task1、task2 所得；task3 中二次執行的數字相近）

## 問題回答

**1. 哪個操作最耗時？你認為原因是什麼？**

`read_json` 最耗時（約 0.0077s）。雖然 JSON 檔案比 CSV 小，但 Python 的 `json.load()` 需要將整個 JSON 字串解析成 Python dict／list 物件，涉及較多的記憶體配置；加上本機磁碟快取狀態不同，第一次讀取 JSON 時 OS 快取尚未預熱，所以比 `read_csv` 慢。

**2. read_csv 比 read_json 快還是慢？與課堂 U01 的比較實驗結果一致嗎？**

`read_csv`（0.0025s）比 `read_json`（0.0077s）快。這與課堂 U01 的觀察一致：CSV 為純文字逐行讀取，`csv.DictReader` 只做字串分割；`json.load` 則需完整解析巢狀結構，整體開銷較大。

**3. write_xml 比 write_json 快還是慢？原因為何？**

`write_xml`（0.0020s）比 `write_json`（0.0024s）略快。原因在於本作業的 XML 每筆學生只輸出四個屬性的單行自閉合標籤，輸出量較精簡；而 `json.dump` 加上 `indent=2` 會在每個欄位後加入換行與縮排字元，實際位元組數稍多，寫出時間也略長。

**4. 如果資料筆數從 100 增加到 10000，你預期各函式耗時如何變化？**

四個函式皆為 O(n) 操作（逐列讀寫），耗時應線性成長，約為現在的 53 倍（10000/189 ≈ 53）。`write_xml` 的成長幅度可能稍大，因為 ElementTree 在建構 Element 物件時有額外的 Python 物件分配開銷；`read_json` 的成長則取決於 JSON 字串長度，亦屬線性。

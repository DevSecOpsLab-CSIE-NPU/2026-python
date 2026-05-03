## 執行結果

```text
[timeit] read_csv 耗時 0.002918s
[timeit] write_json 耗時 0.002581s
[timeit] read_json 耗時 0.001129s
[timeit] write_xml 耗時 0.001662s
```

## 問題回答

1. 哪個操作最耗時？你認為原因是什麼？

`read_csv` 最耗時（0.002918s）。原因是 CSV 需要逐行解析字串並建立欄位對應，資料清理成本通常較高。

2. read_csv 比 read_json 快還是慢？與課堂 U01 的比較實驗結果一致嗎？

`read_csv` 比 `read_json` 慢。這與課堂上常見結論一致：JSON 載入通常較直接，CSV 解析與欄位映射會多一些處理。

3. write_xml 比 write_json 快還是慢？原因為何？

這次結果中 `write_xml`（0.001662s）比 `write_json`（0.002581s）快。原因可能是本次輸出欄位固定、XML 節點結構較簡單，加上資料量不大，序列化差異不明顯。

4. 如果資料筆數從 100 增加到 10000，你預期各函式耗時如何變化？

預期四個函式都會明顯增加，趨勢接近線性成長。`read_csv` 與 `write_json` 會因為逐筆解析與格式化輸出而增加更顯著，`write_xml` 也會因節點數暴增而變慢。

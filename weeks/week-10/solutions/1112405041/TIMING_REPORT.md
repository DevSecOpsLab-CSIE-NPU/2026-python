# Week 10 效能分析報告

## 執行結果

[timeit] read_csv    耗時 0.004025s
[timeit] write_json   耗時 1.724969s
[timeit] read_json    耗時 0.008864s
[timeit] write_xml    耗時 1.133040s

## 問題回答

1. **哪個操作最耗時？你認為原因是什麼？**
   `write_json` 最耗時。原因可能是檔案 I/O 操作本身較慢，且 Python 在處理大型字典轉 JSON 並進行 `indent=2` 的縮進格式化時，需要較多的 CPU 運算。

2. **read_csv 比 read_json 快還是慢？與課堂 U01 的比較實驗結果一致嗎？**
   `read_csv` (0.004s) 比 `read_json` (0.008s) 快。這與 U01 的實驗結果（JSON 通常最快）略有不一致，這可能是因為我們的 CSV 資料量較小，且 `DictReader` 在處理純文字時的開銷在小規模下不明顯，而 JSON 解析器的啟動開銷相對較大。

3. **write_xml 比 write_json 快還是慢？原因為何？**
   `write_xml` (1.133s) 比 `write_json` (1.724s) 快。通常 XML 解析較慢，但在「寫入」方面，`ElementTree` 的 `write` 方法經過高度優化，且我們在寫入 JSON 時使用了較大的 `indent` 格式化，這增加了寫入時間。

4. **如果資料筆數從 100 增加到 10000，你預期各函式耗時如何變化？**
   預期所有函式的耗時都會隨筆數呈線性增長 ($O(N)$)。其中 JSON 的解析與寫入時間增長可能會比 XML 慢一些，因為 JSON 的格式更簡單；而 CSV 讀取在超大規模下可能會因為需要逐行解析字串而變慢。

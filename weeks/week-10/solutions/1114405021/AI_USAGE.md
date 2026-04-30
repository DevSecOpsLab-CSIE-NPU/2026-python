# AI_USAGE

## 我問 AI 的問題（3-5 條）
- Python CSV 在 UTF-8-BOM 編碼下應該用什麼 encoding 讀取？
- 要怎麼設計 timeit decorator，保留原函式名稱與 docstring？
- JSON 轉 XML 時，學生資料用屬性還是子節點比較符合指定格式？
- unittest 如何覆蓋正常、邊界、反例三類情境？
- matplotlib 長條圖如何在每個 bar 上標示秒數？

## AI 建議有採用的部分
- CSV 讀取使用 encoding='utf-8-sig'。
- timeit 使用 functools.wraps 與 time.perf_counter()。
- 測試拆成 5 個明確情境，讓需求可追蹤。

## AI 建議我拒絕的部分與原因
- 建議把 timeit 寫在共用 util 檔後再 import。因作業要求 Task1 與 Task2 要在各自檔案自行實作 decorator，因此拒絕共用化。
- 建議直接依照 data['總人數'] 寫入 XML total。為避免資料不一致，改用實際學生清單長度計算 total。

## AI 輸出有誤案例與修正
- 錯誤建議：CSV 路徑固定使用 weeks/week-08/in-class/stu-data/113年新生資料庫.csv。
- 實際執行結果：本專案資料位於 assets/stu-data/113年新生資料庫.csv，導致 FileNotFoundError。
- 修正方式：程式先嘗試課程指定路徑，若不存在則 fallback 到 assets/stu-data，並重新執行成功。

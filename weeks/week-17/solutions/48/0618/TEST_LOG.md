# 測試執行紀錄 (TEST_LOG.md)

## 1. 測試環境
* **執行日期**：2026-06-18
* **測試框架**：pytest
* **計時器底層**：`time.perf_counter()`
* **圖形輸出**：matplotlib (使用 Agg backend)

## 2. 測試範疇與驗收標準
* **Stage 1 (裝飾器功能與例外)**
  * 驗證其不改變原函式簽名與回傳值（透過 `functools.wraps`）。
  * 邊界測試：`repeat=1` 可正常執行。
  * 異常/紅燈測試：驗證 `repeat=0`、`repeat=-1` 等小於 1 的不合法數值會精準拋出 `ValueError`。
* **Stage 2 (搜尋演算法邊界)**
  * 空陣列測試：`linear_search` 與 `binary_search` 傳入 `[]` 回傳 `-1`；`set_search` 回傳 `False`。
  * 防禦性測試：`data` 或 `target` 傳入 `None` 時，精準拋出 `TypeError`。
  * 唯讀測試：使用 `copy` 深度比對，確保演算法執行前後完全沒有修改原始 `data` 內容。
* **Stage 4 & 5 (效能視覺化與防禦性強化)**
  * 驗證 `assets/radar.png` 雷達圖正確產生且檔案非空。
  * 強健性測試：確保型態檢查使用 `type(repeat) is not int`，阻絕 `repeat=True` 等不合法型態輸入。

## 3. 測試結果
* **測試通過狀態**：PASSED
* 所有邊界條件、正常綠燈、異常紅燈斷言皆符合預期，成功串接基準測試與數據視覺化輸出。

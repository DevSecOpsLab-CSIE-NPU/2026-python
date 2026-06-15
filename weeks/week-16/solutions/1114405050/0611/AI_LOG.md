# AI 協作紀錄

## Stage 3 效能報告摘要
1. **加速百分比**：在 N=4000 時，`quick_sort_fast` 耗時從 0.00471s 降至 0.00231s，加速比約為 **2.04 倍**。
2. **演算法優化策略**：
   - **小陣列切換**：當子陣列小於等於 15 時切換為 Insertion Sort，降低遞迴開銷。
   - **Median-of-Three**：取頭、中、尾的中位數作為 pivot，避免在排序好的陣列退化成 $O(N^2)$。
   - **In-place 排序副本**：進入遞迴前先複製一份陣列，然後在副本上進行 in-place 排序以減少記憶體配置負擔。

## Stage 5 安全性自掃摘要
3. **修補程式問題**：總共依據 OpenSSF 修補/處理了 **3 項** 程式問題，並標示 1 項不適用：
   - **CWE-502**：確保使用 `json` 而不是不安全的 `pickle` 存取 benchmark 檔案。
   - **Chapter 3 (Numbers)**：在 `make_data` 新增負數檢查，防止產生不合理長度的陣列 (`ValueError`)。
   - **Chapter 5 (Exception Handling)**：在 `load_results` 中加上讀檔失敗的例外處理防護 (`FileNotFoundError`)。

---
> 註：本專題開發過程中，依據「開發訪談助教」的協作協議，每個階段皆落實「提問填滿檢查表 → 紅燈測試 → 綠燈實作」的 TDD 循環。

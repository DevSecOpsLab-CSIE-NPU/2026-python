# AI_LOG — 第四題：二分搜尋效能 (Binary Search Performance)

## 第四題：二分搜尋效能 (Binary Search Performance)

### 我問 AI 什麼
1. 告知 AI 開始第四題，並要求拆解 $\ge 3$ 個 test cases。
2. 要求 AI 依照 TDD 流程（寫測試 $\to$ 確認紅燈 $\to$ commit $\to$ 實作 $\to$ 綠燈 $\to$ commit）。

### AI 反問我什麼 / 我怎麼回答
*   **AI 反問**：函式簽名與回傳型別建議（Tuple 回傳 `(index, cmp)` vs 屬性記錄）。
    *   **我回答**：選擇建議 A，回傳 `(index, cmp_count)` 之 tuple。
*   **AI 反問**：空 list (n=0) 時的預期結果。
    *   **我回答**：回傳 `(-1, 0)`。
*   **AI 反問**：`binary_search` 收到未排序資料的處理方式。
    *   **我回答**：選擇「做法 B」，即在函式內部檢查排序，若未排序則拋出 `ValueError`。
*   **AI 反問**：如何驗證比較次數 (cmp) 的正確性。
    *   **我回答**：同意線性搜尋驗證 `cmp == index + 1`，二分搜尋驗證符合 $\log_2 n$ 量級。

### AI 給了什麼
1. 建立了 `test_search_performance.py`，包含 6 個測試（線性找/沒找、二分找/沒找、未排序拋錯、空 list 邊界）。
2. 實作了 `search_performance.py`（包含 `linear_search` 與 `binary_search`，並在二分搜尋前加入排序檢查）。

### 我改了什麼
1.  **明確化回傳介面**：在 AI 建議多種方式後，決定採用 Tuple 回傳，以確保每個呼叫都能獲取獨立的比較次數，避免在多執行緒或複雜呼叫中產生狀態污染。
2.  **強化安全性檢查**：堅持在 `binary_search` 內部加入排序檢查機制（raise ValueError），而非僅依賴外部輸入正確，確保實作符合嚴謹的工程標準。

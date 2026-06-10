## 我問 AI 什麼
- 請幫我為 `digit_root(n: int) -> int` 寫 `unittest` 測試，至少包含基本案例、edge case、與 `n < 1` 例外案例。
- 請幫我實作 `digit_root`，規格是反覆加總各位數直到剩一位數，且 `n < 1` 要 `raise ValueError("n must be >= 1")`。

## AI 給了什麼
- 提供了可執行的 `unittest` 測試範例與函式實作方向。
- 提醒可用迴圈重複做數字加總直到結果小於 10。

## 我改了什麼
- 我自行確認並保留例外訊息必須與題目完全一致：`n must be >= 1`。
- 我補了一個大數 edge case：`2_000_000_000`，確認在上限附近也能正確回傳。
- 我用 `assertRaisesRegex` 精確比對錯誤訊息，避免只檢查型別而漏掉訊息不符。

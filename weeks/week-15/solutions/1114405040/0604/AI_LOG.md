# AI_LOG

## 我問 AI 的問題

請幫我完成 `count_squares(a, b)` 的 unittest 測試與實作，至少包含基本案例、edge case，以及 `a > b` 時要丟出 `ValueError` 的測試。

## AI 的建議

AI 建議測試 `count_squares(1, 10) == 3`、沒有平方數的區間 `count_squares(5, 8) == 0`、單點平方數 `count_squares(100, 100) == 1`，並使用 `assertRaises` 測試錯誤輸入。

## 我自己的判斷

我確認題目要求 `[a, b]` 含端點，所以 `100` 到 `100` 要算 1 個平方數；另外我採用 `math.isqrt` 實作，避免用迴圈逐一檢查每個數。

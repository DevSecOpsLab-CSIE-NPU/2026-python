# AI_LOG

## 我問 AI 什麼

> 「請幫我用 unittest 寫 digit_root(n) 的測試，至少 3 個 case：1 個基本、1 個 edge case、1 個例外案例。edge case 包含一位數、10、極大值。例外案例要檢查 n<1 時 raise ValueError 且訊息為 "n must be >= 1"。」

## AI 給了什麼

> 給了 5 個測試案例（test_basic: 199→1, 24→6, 9999→9；test_edge_case: 5→5, 1→1, 9→9, 10→1, 2000000000→2；test_invalid_input_raises: 0 與 -1 都檢查 ValueError 及訊息）。

## 我改了什麼

> 測試案例齊全，無需修改。digit_root.py 用雙層 while 迴圈實作，符合規格。自己補了 AI_LOG.md。

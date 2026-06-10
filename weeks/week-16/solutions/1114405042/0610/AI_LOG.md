# AI_LOG — 6/10 計時演練：數字根

## 我問 AI 什麼

> 「請幫我用 unittest 寫 digit_root(n) 的測試，至少包含：基本多位數案例、一位數 edge case、大數 edge case、以及 n<1 時 raise ValueError 的例外案例。」

## AI 給了什麼

> 給出了 4 個測試案例：test_basic_multidigit（24→6, 199→1, 9999→9）、test_edge_single_digit（5→5, 1→1, 9→9）、test_edge_large_number（2000000000→2）、test_invalid_input_raises（n=0 與 n=-5 應 raise ValueError 並比對錯誤訊息）。但 AI 給的 import 語法有誤，且未確認 ValueError 訊息文字是否完全相符。

## 我改了什麼

> 修正 import 為 `from digit_root import digit_root`（AI 漏了 import 寫法），並自行補上 `self.assertEqual(str(ctx.exception), "n must be >= 1")` 確認錯誤訊息文字完全一致，因為題目要求訊息一字不差。另外自行實作 digit_root 函式：先檢查輸入是否 <1，再用 while 迴圈反覆加總各位數直到剩一位數。

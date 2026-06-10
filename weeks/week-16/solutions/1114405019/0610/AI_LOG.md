# AI_LOG — 6/10 數字根

## 我問 AI 什麼

「我要用 Python unittest 測試一個函式 digit_root(n: int) -> int，規格：反覆把 n 的各位數字相加直到剩一位數；n < 1 要 raise ValueError("n must be >= 1")。輸入範圍 1 ≤ n ≤ 2,000,000,000。請幫我列出至少 3 個 test case，包含 edge case 與例外案例。」

## AI 給了什麼

AI 給了 4 個測試：24→6、199→1、5→5（一位數）、n=0 應 raise ValueError。沒有負數輸入的測試，也沒有靠近上限 2,000,000,000 的大數測試。

## 我改了什麼

1. 補了 `test_invalid_negative_raises`：題目說 `n < 1`，負數也應該 raise，AI 只測了 0，我自己加了 n=-5 的案例。
2. 補了 `test_edge_large_number`：驗證 n=2000000000（數字根為 2），確保迴圈在大數下也能正確收斂。
3. 把 `test_basic_9999`（9999→36→9）加進去，測試需要兩步驟才能收斂的情況，AI 沒給這個 case。

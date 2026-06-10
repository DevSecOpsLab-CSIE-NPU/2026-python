# AI_LOG

## 我問 AI 什麼

1. 「請幫我針對數字根（digit root）題目拆解測試案例。輸入範圍為 1 <= n <= 2,000,000,000 的正整數。當 n < 1 時應拋出 ValueError("n must be >= 1")。請幫我設計至少三個測試案例（包含基本案例、邊界案例、例外案例）。」
2. 「請幫我用 Python 實作 digit_root(n) 函式，反覆把各位數字相加直到剩下一位數並回傳。如果有輸入 n < 1 則拋出 ValueError("n must be >= 1")。」

## AI 給了什麼

1. AI 給了測試案例的設計：基本案例（24 -> 6, 199 -> 1, 9999 -> 9）、邊界案例（5 -> 5, 1 -> 1, 2000000000 -> 2）、例外案例（0 與 -100 應拋出 ValueError）。
2. AI 給了使用 `while n >= 10` 迴圈來反覆加總各位數的 Python 實作代碼。

## 我改了什麼

1. 在測試案例中，我特別檢查了 AI 給的例外案例，並加上了精確的錯誤訊息比對：`self.assertEqual(str(context.exception), "n must be >= 1")`，以確保實作時拋出的 Exception 內容字眼完全符合題目要求。
2. 在 `test_digit_root.py` 中解除了 `from digit_root import digit_root` 的註解，並先執行 `python -m unittest` 確認測試全紅（紅燈），才開始建立 `digit_root.py` 進行實作。
3. 實作完成後，再次執行測試確認綠燈。

## AI_LOG

### 我的提示詞（逐字貼上）

1. "Please implement a function digit_root(n: int) -> int that returns the digital root of a positive integer n. If n < 1 raise ValueError(\"n must be >= 1\"). Keep the function name and file name digit_root.py. Use an efficient approach."

### 我改了什麼

- 新增 `digit_root.py`，使用數字根公式實作。處理 n < 1 時拋出 ValueError。
- 新增 `test_digit_root.py`（3 個以上的測試：基本、edge case、例外）。

### 訪談摘要

- 我問：如何實作數字根並處理例外？
- AI 答：提供 congruence 公式 1 + ((n-1) % 9) 並建議保留例外訊息。檢查表狀態：✅簽名 ✅例外 ✅驗收

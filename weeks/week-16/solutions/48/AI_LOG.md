AI_LOG for digit_root exercise

Prompt used to generate tests (exact):
請幫我為 digit_root(n) 寫 unittest 測試檔，要求至少 3 個 test case，包含至少一個 edge case（例如 n 的最小值或最大值）及至少一個會觸發例外的 case（n < 1 必須 raise ValueError("n must be >= 1")）。請用中文註解並命名檔案為 test_digit_root.py。

Prompt used to generate implementation (exact):
請為 digit_root(n: int) 實作一個函式，功能為反覆將 n 的各位數字相加直到剩下一位數後回傳該數字。輸入範圍為正整數（1 ≤ n ≤ 2,000,000,000）。當 n < 1 時請 raise ValueError("n must be >= 1")（訊息要完全相同）。若可行，請用 O(1) 的數學公式實作並包含簡短說明。

Steps performed:
1. 在本機建立並修改測試檔：[test_digit_root.py]，加入基本、edge 與例外測試。
2. 將測試複製到 `weeks/week-16/solutions/48`，並 commit（commit: "test: add failing tests for digit root"）。
3. 在 `solutions/48` 預期測試失敗（因為尚未實作），以確認紅燈。測試結果顯示因缺少 `digit_root` 模組而失敗。
4. 實作 `digit_root`（`digit_root.py`），使用數學公式 `1 + (n-1) % 9` 並在 `n < 1` 時 raise 指定的 ValueError。
5. 在 `solutions/48` 執行 `python -m unittest -v`，測試通過（3 tests OK）。
6. commit 實作（commit: "feat: implement digit root"）。
7. 新增本檔 `AI_LOG.md` 並準備開 PR。

Notes / rationale:
- 使用數學公式能在常數時間內求出數字根，適合題目上限。
- 測試明確檢查例外訊息字串，要完全匹配。

Files changed in this solution folder:
- digit_root.py (new)
- test_digit_root.py (new)
- AI_LOG.md (new)


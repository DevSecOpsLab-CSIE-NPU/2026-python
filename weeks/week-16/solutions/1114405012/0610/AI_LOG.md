# AI_LOG

## 我問 AI 什麼

> 「請幫我讀 README，為 digit_root 寫 ≥3 個 test case（含 edge case 與例外案例），
> 然後寫 digit_root 實作讓測試全綠，最後 commit 並開 PR。」

## AI 給了什麼

> AI 給了 5 個測試（test_multi_digit, test_single_digit, test_large_number,
> test_zero_raises, test_negative_raises），以及 digit_root 的迴圈實作。
> 並依序完成紅燈確認 → commit → 複製到 solutions → push → 開 PR。

## 我改了什麼

> 測試案例中我要求補上 `test_negative_raises` 確保 n < 1（包含負數）都會 raise
> ValueError，而不只是測 n=0，因為題目規格是 n < 1 而非 n == 0。
> 實作部分直接採用迴圈逐位相加，未使用公式解 1+(n-1)%9，因為公式解對 n=0
> 的邊界需要額外處理，而迴圈寫法更直觀、不易出錯。

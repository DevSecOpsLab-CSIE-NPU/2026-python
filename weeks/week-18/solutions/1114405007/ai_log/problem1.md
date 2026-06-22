# 題1 AI_LOG（A區：資料清理）

## AI 反問我什麼 / 我怎麼回答

| AI 問 | 我答 |
|-------|------|
| 函式簽名？ | `process_sequence(numbers, D)` -> `list[int]`；`solve(input_text, D)` -> `str` |
| 輸入邊界？ | `n <= 10^5`，數值 `±10^9`，`n=0` 結束 |
| 例外處理？ | `n=0` 直接退出；空行跳過 |
| Edge case？ | 全剔除 -> `NONE`；負數/0；全重複 |
| 驗收標準？ | 學號末位 `7` -> `D = (7%4)+2 = 5` |

## 我問了 AI 什麼（本題）
1. 閱讀 `HOMEWORK.md` 和 bloom 範例，幫我實作題1（D=5）。
2. 先寫測試再寫實作，走 Red -> Green。

## AI 建議採用 / 修正
- 採用 set+list 進行去重保序（參考 R10-dedupe.py）。
- `solve()` 設計成可接收字串輸入，方便測試。
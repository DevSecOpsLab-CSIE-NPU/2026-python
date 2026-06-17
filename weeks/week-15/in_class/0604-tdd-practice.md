# 6/4 (四)｜TDD 應用

> 本日題目進入期末考 **B 區候選池（不公開）**。
> 本日起 PR 必須附 `AI_LOG.md`。

## 學習目標

- 在「沒寫過的新題」上獨立跑完 SOP
- 第一次寫 `AI_LOG.md`，練習對 AI 輸出做判斷

## 本日不評分，但要繳交

- PR 連結
- `AI_LOG.md`（隨 PR 提交）

---

## 題目：平方數計數（UVA 11461 簡化版）

寫一個函式 `count_squares(a: int, b: int) -> int`，回傳區間 `[a, b]` 之間（含端點）有幾個完全平方數。

- 輸入：兩個正整數 `a`, `b`（1 ≤ a ≤ b ≤ 100000）
- 輸出：區間內完全平方數的個數
- 例外：若 `a > b`，丟出 `ValueError("a must be <= b")`

範例：

| a | b | 結果 |
|---|---|------|
| 1 | 4 | 2（1, 4） |
| 1 | 10 | 3（1, 4, 9） |
| 5 | 8 | 0 |
| 1 | 1 | 1 |
| 100 | 100 | 1 |

> 此為 UVA 11461 的簡化版（去掉多筆測資輸入，只考核心計算）。

---

## 課堂節奏（90 分鐘）

| 時間 | 內容 |
|------|------|
| 0:00–0:05 | 發題目，講解 AI_LOG 要求 |
| 0:05–0:20 | 跟 AI 拆 ≥3 個 test case（至少 1 個 edge case + 1 個例外案例） |
| 0:20–0:35 | 寫 `test_square_counter.py`，紅燈 commit |
| 0:35–1:00 | 寫 `square_counter.py`，綠燈 commit |
| 1:00–1:15 | 寫 `AI_LOG.md`、push、開 PR |
| 1:15–1:30 | 確認 PR 內容齊全（題目摘要、測試結果、AI_LOG），對照 SOP 檢查表自評 |

---

## 必填的 test case（至少 3 個）

1. **基本案例**：`count_squares(1, 10) == 3`
2. **Edge case**：`count_squares(1, 1) == 1` 或 `count_squares(100, 100) == 1`
3. **例外案例**：`a > b` 時應 `raise ValueError`

→ AI 可能不會主動寫第 3 個，你要記得提醒它。**這就是 AI_LOG 要記錄的事。**

---

## AI_LOG 要求（首次）

在 PR 根目錄附 `AI_LOG.md`，**至少 3 行**，格式：

```markdown
## 我問 AI 什麼
（一行：例如「請幫我用 unittest 寫 count_squares 的測試」）

## AI 給了什麼
（一行：例如「給了 2 個基本測試但沒寫例外案例」）

## 我改了什麼
（一行：例如「我自己加了 a > b 應丟 ValueError 的測試」）
```

範本見 [`./ai-log-template.md`](./ai-log-template.md)。

**「我改了什麼」是 0 字 = 0 分。** 全部照貼 AI 等於沒用腦，期末考此項零分。

---

## starter 檔

```bash
cp -r weeks/week-15/in_class/0604-starter weeks/week-15/solutions/<學號>/0604
```

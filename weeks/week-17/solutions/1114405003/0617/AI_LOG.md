# AI_LOG — 0617 timeit + 搜尋效能評估

---

## 我問 AI 什麼

1. 「從任務一開始，幫我完成 timeit 裝飾器」
2. 「幫我寫 linear_search 和 binary_search 的測試」
3. 「幫我寫 benchmark 腳本量測 linear vs binary」
4. 「幫我寫 README.md 的評估」

## AI 給了什麼

1. 問了五個規格問題（簽名、例外、邊界、edge case、驗收標準），填滿檢查表後才給測試
2. 給了 14 個測試案例（找到、找不到、空 list、重複元素、不修改 data）
3. 給了 benchmark 腳本，用 timeit 量測兩者效能
4. 寫了 2–3 句評估，包含誰快、排序划不划算、直覺判斷

## 我改了什麼

1. 我決定用 `@timeit` 裝飾器（不帶參數），`repeat` 用預設值 3
2. 我決定 `binary_search` 收到未排序 data 時照常搜尋，結果不保證
3. 我決定兩者都回傳第一個出現的 index，與 Python 內建 `list.index()` 一致
4. 我決定只處理規格寫的例外（`repeat < 1` → `raise ValueError`），不額外處理

---

## AI 反問我什麼 / 我怎麼回答

> 逐項記下 AI 問的規格問題與你的決定。

1. AI 問「`timeit` 裝飾器的函式簽名與回傳型別是什麼？」→ 我答：用 `@timeit` 裝飾器，不帶參數，`repeat` 用預設值 3
2. AI 問「例外行為怎麼處理？」→ 我答：只處理規格寫的 `repeat < 1` → `raise ValueError`，其他不額外處理
3. AI 問「邊界條件（bounds）？」→ 我答：`repeat` 只要 `>= 1` 就行，不設上限
4. AI 問「驗收標準是什麼？」→ 我答：`test_rejects_invalid_repeat` 期望看到 `ValueError` 被拋出，如果 `timing.py` 還沒實作會看到 `self.fail("尚未實作")`
5. AI 問「`linear_search` 和 `binary_search` 的 target 型別要限制嗎？」→ 我答：照規格，不限制
6. AI 問「`binary_search` 收到未排序 data 要怎麼辦？」→ 我答：照常搜尋，結果不保證
7. AI 問「target 出現多次回傳哪一個？」→ 我答：幫我選，選回傳第一個
8. AI 問「驗收標準？」→ 我答：都要測（找到、找不到、空 list、重複元素）

---

## 評分提示

| 「我改了什麼」內容 | 期末考此項得分 |
|---|---|
| 空白或「沒改」 | 0 分 |
| 「改了變數名」「調整縮排」這類無關判斷 | 部分分 |
| 有明確判斷（補測試、發現 AI 寫錯、改例外處理） | 滿分 |

→ 我的判斷：決定 `binary_search` 未排序時的行為、決定回傳第一個 index、決定只處理規格寫的例外。

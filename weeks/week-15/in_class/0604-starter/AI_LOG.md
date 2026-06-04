# AI_LOG

## 我問 AI 什麼

請幫我用 TDD 為 `count_squares(a, b)` 寫測試與實作，至少 3 個測試案例（含 1 個 edge case 與 1 個 invalid-input）。

## AI 給了什麼

- 新增 `weeks/week-15/in_class/0604-starter/test_square_counter.py` 的測試：
  - `count_squares(1,10) -> 3`
  - `count_squares(16,16) -> 1`（edge）
  - `count_squares(-5,5) -> 3`（包含 0）
  - `count_squares(5,2)` 驗證會丟 ValueError
- 實作 `square_counter.py` 的 `count_squares(a,b)`，並處理 `a>b` 拋例外與負範圍處理。

## 我改了什麼

- 把測試加入 repo 並 commit。
- （為遵守 TDD 紅燈→綠燈流程）先讓實作檔暫時不存在以產生失敗測試，之後再重新加回實作使測試通過。
- 把最後已通過的測試輸出與 `AI_LOG.md` 組成 PR 內容，並推到 fork 的分支 `feature/wk15-0604-d14405048`。

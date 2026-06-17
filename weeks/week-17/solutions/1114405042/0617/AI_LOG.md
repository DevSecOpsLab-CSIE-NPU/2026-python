# AI_LOG.md

## 我問 AI 什麼

> 請幫我用 unittest 寫 timeit 裝飾器的測試，規格：1. 回傳值不變 2. functools.wraps 保留 metadata 3. 每次呼叫跑 repeat 次，記錄每次耗時到 f.records，f.last_elapsed 為平均 4. 不准 print 5. repeat < 1 raise ValueError（不用 assert）

## AI 給了什麼

> 給了 7 個測試案例：test_returns_original_result、test_preserves_function_metadata、test_records_each_repeat_and_average、test_rejects_invalid_repeat、test_repeat_default_is_three、test_repeat_one_works、test_side_effects_called_multiple_times

## 我改了什麼

> 我檢查了測試是否涵蓋所有規格，並補上 edge case 測試（repeat=1、副作用函式被多呼叫）。確認測試全紅後再實作 timing.py。

---

## AI 反問我什麼 / 我怎麼回答

> 逐項記下 AI 問的規格問題與你的決定。

1. **AI 問：「timeit 是裝飾器工廠還是直接裝飾器？」**  
   → 我答：裝飾器工廠，支援 `@timeit` 和 `@timeit(repeat=5)` 兩種用法。

2. **AI 問：「repeat 參數放在哪裡？」**  
   → 我答：放在外層函式，`def timeit(repeat=3):` 回傳真正的裝飾器。

3. **AI 問：「records 和 last_elapsed 掛在 wrapper 還是原函式？」**  
   → 我答：掛在 wrapper（回傳的函式物件）上，這樣每次呼叫都能存取。

4. **AI 問：「repeat < 1 要 raise 什麼例外？」**  
   → 我答：raise ValueError，明確禁止用 assert（最佳化模式會被移除）。

5. **AI 問：「被裝飾函式有副作用時，要不要多呼叫？」  
   → 我答：要，每次呼叫都要實際執行 repeat 次，副作用會累積（測試有驗證）。

6. **AI 問：「binary_search 收到未排序資料怎麼辦？」**  
   → 我答：行為未定義，呼叫者有責任確保已排序，在 docstring 寫清楚。

---

## 評分提示

| 「我改了什麼」內容 | 期末考此項得分 |
|---|---|
| 空白或「沒改」 | 0 分 |
| 「改了變數名」「調整縮排」這類無關判斷 | 部分分 |
| 有明確判斷（補測試、發現 AI 寫錯、改例外處理） | 滿分 |
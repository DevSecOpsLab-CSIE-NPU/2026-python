# AI_LOG

## 我問 AI 什麼

我請 AI 幫我依照 Week 17 / 0617-search-eval 的要求，用 TDD 流程完成 `timeit` decorator，並實作 `linear_search` 與 `binary_search`。

## AI 給了什麼

AI 先整理了 `timeit` 的規格，包含 `repeat < 1` 要 raise ValueError、使用 `functools.wraps`、記錄 `records`、記錄 `last_elapsed`，再提供 `test_timing.py`、`timing.py`、`search.py`、`README.md` 的內容。

## AI 反問我什麼 / 我怎麼回答

AI 問我是否要先走 TDD 流程，也就是先寫測試讓它紅燈，再寫實作讓它綠燈。

我回答要照老師要求的流程進行：先完成 `test_timing.py` 並確認紅燈，commit 測試後，再建立 `timing.py` 讓測試通過。

AI 也提醒我 `binary_search` 必須假設資料已排序，如果資料未排序，結果應在 docstring 裡說明為 undefined behavior。

## 我改了什麼

我確認 `repeat < 1` 的情況要使用 `raise ValueError`，不是使用 `assert`。我也確認 `binary_search` 不應該自己修改或排序輸入資料，而是在 docstring 說明它假設輸入已排序。最後我依照 TDD 流程先提交 failing tests，再提交通過測試的實作。
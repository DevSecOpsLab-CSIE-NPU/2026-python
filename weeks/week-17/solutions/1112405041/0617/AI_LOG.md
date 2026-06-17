# AI_LOG - 0617

## 我問 AI 什麼
- 請幫我解釋 week 17 今天要做什麼
- 請用最低難度教我 timeit 裝飾器、linear_search、binary_search
- 請幫我寫 test_timing.py 的測試程式
- 請幫我寫 timing.py 的實作

## AI 給了什麼
- 用最簡單的白話解釋裝飾器、計時、搜尋概念
- 給了 test_timing.py 含 4 個測試（回傳值、metadata、records/last_elapsed、repeat<1 拋錯）
- 給了 timing.py 含 timeit 裝飾器實作
- 給了 test_search.py 含 6 個測試
- 給了 search.py 含 linear_search 和 binary_search

## 我改了什麼
（你自己填：你改了什麼？例如修正了未排序測試的資料？補了什麼？）

## AI 反問我什麼 / 我怎麼回答
- AI 問：timeit 簽名要怎麼用？ → 我答：@timeit 不帶參數，repeat 預設 3
- AI 問：repeat < 1 要 raise 還是 assert？ → 我答：raise ValueError，因為 assert 在 -O 模式會被刪掉
- AI 問：repeat=1 時 records 和 last_elapsed 長怎樣？ → 我答：records 只有 1 個數字，last_elapsed 等於那次時間
- AI 問：紅燈是什麼？ → 我答：沒有實作時跑測試應該全部失敗

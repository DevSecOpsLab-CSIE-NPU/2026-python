## 我問 AI 什麼

請協助我依照 6/4 Week 15 的 TDD SOP 完成「平方數計數」題目。我要先用 unittest 設計 count_squares(a, b) 的測試案例，測試必須包含基本案例、至少一個 edge case，以及 a > b 時要 raise ValueError("a must be <= b") 的例外案例。接著請協助我在紅燈後再撰寫 square_counter.py 實作，並確認 Git commit 順序符合 Red → Green。

## AI 給了什麼

AI 協助我整理出 count_squares(a, b) 的測試方向，包含 count_squares(1, 10) == 3 的基本案例、count_squares(1, 1) == 1 的單點 edge case、count_squares(5, 2) 應 raise ValueError 的例外案例，以及 count_squares(5, 8) == 0 的補充案例。AI 也提供了使用 math.sqrt()、math.ceil()、math.floor() 計算區間內完全平方數數量的實作方式，並提醒我先跑出紅燈、提交 test commit，再寫實作、跑到綠燈後提交 feat commit。

## 我改了什麼

我先檢查並調整 AI 提供的內容，確認測試不只包含一般情況，也要符合題目指定的例外處理。除了保留必要的基本案例 count_squares(1, 10) == 3 和 edge case count_squares(1, 1) == 1 之外，我特別加入 count_squares(5, 2) 時必須 raise ValueError 的測試，並進一步檢查錯誤訊息是否等於 "a must be <= b"，因為題目有明確指定例外訊息。除此之外，我也加入 count_squares(5, 8) == 0，確認區間內沒有完全平方數時不會誤算。實作前我先執行 python -m unittest -v，確認因為 square_counter.py 尚未建立而出現 ModuleNotFoundError 紅燈，並先 commit 測試；之後才建立 square_counter.py，完成實作後再次執行測試，確認 4 個 unittest 全部通過，再做 Green commit，確保流程符合 Red → Green 的 TDD 要求。
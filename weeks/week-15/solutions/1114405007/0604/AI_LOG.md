## 我問 AI 什麼
請幫我用 unittest 寫 count_squares(a, b) 的測試，至少 3 個案例，包含 edge case 和 a > b 的例外。

## AI 給了什麼
AI 提供了基本測試、單點區間測試與 ValueError 例外測試的方向。

## 我改了什麼
我把測試補成可直接執行的 unittest，並明確加入 a > b 時要驗證錯誤訊息是 "a must be <= b"。
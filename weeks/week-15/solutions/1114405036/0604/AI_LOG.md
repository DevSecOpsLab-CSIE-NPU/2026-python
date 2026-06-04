## 我問 AI 什麼
請幫我用 unittest 寫 count_squares(a, b) 的測試，至少 3 個案例，包含 edge case 與 a > b 的例外測試。

## AI 給了什麼
AI 給了測試骨架，但沒有實作測試，且需要補上 a > b 時應 raise ValueError 的例外案例。

## 我改了什麼
我補上了 `count_squares(1, 10) == 3`、`count_squares(100, 100) == 1` 的測試，並加了 `count_squares(5, 2)` 應 raise ValueError 的例外測試。
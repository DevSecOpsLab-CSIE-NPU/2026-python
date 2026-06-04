## 我問 AI 什麼
請幫我用 unittest 幫 count_squares(a, b) 拆測試，至少要有基本案例、edge case、與 a > b 的例外案例。

## AI 給了什麼
AI 提供了 4 個測試案例，包含 count_squares(1, 10) == 3、count_squares(1, 1) == 1、count_squares(5, 8) == 0，還有 a > b 時用 assertRaises(ValueError)。

## 我改了什麼
我先跑出紅燈（因為尚未有 square_counter.py），再補上實作，並確認 ValueError 訊息固定為 "a must be <= b"，最後重跑測試到全綠燈再 commit。

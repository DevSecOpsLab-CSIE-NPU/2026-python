## 我問 AI 什麼
請幫我用 unittest 寫 count_squares(a, b) 的測試，至少 3 個案例。

## AI 給了什麼
AI 提供了基本案例、邊界案例與例外處理的方向，但需要我自己整理成可直接執行的測試檔。

## 我改了什麼
我補上了 `a > b` 時應該 `raise ValueError("a must be <= b")` 的測試，並用 `count_squares(100, 100) == 1` 當 edge case。

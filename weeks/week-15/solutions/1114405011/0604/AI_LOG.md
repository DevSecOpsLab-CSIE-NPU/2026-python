# AI_LOG

## 我問 AI 什麼

請幫我用 unittest 寫 count_squares(a, b) 的測試，至少包含基本案例、edge case，還有 a > b 時要 raise ValueError，接著再實作 square_counter.py。

## AI 給了什麼

AI 先補了 count_squares(1, 10)、count_squares(1, 1)、count_squares(5, 8) 與 a > b 的測試，之後再提供用整數平方根計算平方數個數的實作。

## 我改了什麼

我有對照題目要求確認例外案例不能漏掉，並檢查錯誤訊息要是 a must be <= b，之後再讓實作對應測試跑到綠燈。
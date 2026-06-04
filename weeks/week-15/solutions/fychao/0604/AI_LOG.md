## 我問 AI 什麼
請幫我用 unittest 寫 `count_squares` 的測試，並指出還需要哪些 edge case 或例外處理。

## AI 給了什麼
提供了基本範例測試與部分 edge case，但沒有包含 `a > b` 應丟 `ValueError` 的例外測試。

## 我改了什麼
我補上了 `a > b` 應丟 `ValueError` 的測試，並實作 `count_squares`，所有本地 unittest 已通過（綠燈）。

## 我問 AI 什麼
請幫我用 `unittest` 寫 `count_squares` 的測試，包含基本案例、edge case、以及 a > b 時的例外測試。

## AI 給了什麼
AI 提供了測試骨架與部分範例，給了基本測試但沒有包含 a > b 的例外測試，我自行補齊。

## 我改了什麼
我補上了第三個測試（使用 `assertRaises` 檢查 `ValueError`）、新增單點 edge case，並實作 `square_counter.py` 使測試通過。

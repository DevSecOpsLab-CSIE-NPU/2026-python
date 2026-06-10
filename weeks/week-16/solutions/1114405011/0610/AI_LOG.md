## 我問 AI 什麼

> 「跟 AI 拆 >=3 個 test case（含 >=1 個 edge case），並建立 `test_digit_root.py` 到指定資料夾。」

## AI 給了什麼

> AI 先提供了 4 個測試案例（一般案例、多輪相加、edge case、invalid input），後續也補上 `digit_root.py` 實作。

## 我改了什麼

> 我檢查並修正測試的 import 寫法為 `from .digit_root import digit_root`，讓 `python -m unittest weeks.week-16.solutions.1114405011.0610.test_digit_root` 可以正確載入；另外確認例外訊息必須精確比對 `n must be >= 1`。

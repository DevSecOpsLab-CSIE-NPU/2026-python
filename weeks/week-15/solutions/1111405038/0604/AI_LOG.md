## 我問 AI 什麼
請幫我拆至少 3 個 `count_squares(a, b)` 測試案例（含 edge case 與 `a > b` 的例外案例），再依 TDD 流程完成測試與實作。

## AI 給了什麼
AI 先提供測試案例，再產生 `test_square_counter.py` 與 `square_counter.py`，並以 `python -m unittest -v` 驗證目前 3 個測試皆通過。

## 我改了什麼
我確認並要求補上 `a > b` 應拋出 `ValueError("a must be <= b")` 的例外測試，且檢查紅燈到綠燈流程有完成，最後確認實作使用整數平方根正確計數區間內完全平方數。

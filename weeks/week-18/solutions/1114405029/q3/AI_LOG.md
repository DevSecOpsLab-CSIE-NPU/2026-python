# Q3 AI_LOG - Digital Root in Base

## 我問 AI 什麼

我請 AI 依照 `base=6` 設計任意進位數字根，特別確認輸入 0 不是結束，而是要輸出 0。

## AI 建議什麼

AI 建議拆成 `to_base_digits`、`digit_sum_in_base`、`digital_root_in_base`、`solve`，並驗證合法 base 集合、負數例外、大數與多行 EOF。

## 我如何修改

我確認 base 是 6，補了合法 base 檢查與負數 `ValueError`。測試時我重新用 base-1 規則檢查大數，發現 `1_000_000_000` 的 base 6 數字根應是 5，因此修正手算期望值，確保測試符合規格。

## 對應檔案

- 程式：`q3.py`
- 測試：`test_q3.py`


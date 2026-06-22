# Q2 AI_LOG - Caesar Cipher

## 我問 AI 什麼

我請 AI 依照 `SHIFT=10` 完成 Caesar cipher，並確認大小寫循環、非英文字保留與空行處理。

## AI 建議什麼

AI 建議先寫 `shift_char` 測單一字元，再用 `caesar_line` 與 `solve` 測整行和多行 EOF。測試要包含 `z/Z` wraparound、標點、空白、數字與空行。

## 我如何修改

我確認 `shift` 先對 26 取餘數，讓大於 26 的 shift 也正常。`solve` 使用 `splitlines()` 保留中間空行，並讓一行輸入對應一行輸出。

## 對應檔案

- 程式：`q2.py`
- 測試：`test_q2.py`


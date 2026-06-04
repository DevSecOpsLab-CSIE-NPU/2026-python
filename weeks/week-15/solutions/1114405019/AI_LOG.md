## 我問 AI 什麼

請幫我用 unittest 寫 count_squares(a, b) 的測試，至少 3 個案例，包含 edge case 和例外處理。

## AI 給了什麼

給了基本範圍測試（1~10 結果 3）和單點 edge case（1~1 結果 1），但遺漏了「a > b 應丟 ValueError」的例外案例，也沒驗證例外訊息的文字內容。

## 我改了什麼

我自己補上了兩個例外測試：一個用 assertRaises 確認 count_squares(5, 2) 會丟 ValueError，另一個進一步驗證訊息是 "a must be <= b"；同時加了「5~8 無平方數」與「單點不是平方數」這兩個反向 edge case，確保實作不會只靠正向案例蒙混過關。

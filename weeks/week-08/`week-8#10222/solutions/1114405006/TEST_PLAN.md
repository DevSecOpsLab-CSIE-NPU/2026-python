# 計劃測試

## 測試目標
驗證鍵盤左移解碼、大小寫處理與符號保留。

## 測試案例
1. 單字元案例：r
   - 預期輸出：e
2. 字串案例：O S, GOMR YPFSU/
   - 預期輸出：I AM FINE TODAY.
3. 綜合案例：R;/
   - 預期輸出：EL.

## 驗證方式
- 命令：python solution_10222_simple.py < input_sample.txt
- 比對三行輸出與預期是否一致。

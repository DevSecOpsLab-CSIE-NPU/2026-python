# 題目 2（Caesar Cipher）

此資料夾包含題目 2 的實作與測試，依照考核 SOP 使用 TDD 流程。

內容：
- `solver.py`：主程式與函式 `caesar_cipher`。
- `tests/`：單元測試，包括紅燈與綠燈測試。
- `ALLOC.md`、`CHECKLIST.md`：可由提交者填寫（若需要）。

題目：實作凱薩密碼，將輸入文字中的英文大寫與小寫字母依指定 SHIFT 量向右移動，超出字母範圍時迴圈回到開頭。

- 英文大寫 A-Z 與小寫 a-z 皆需轉換
- 其他字元（空白、標點、數字、符號）則原樣保留
- 第一行為欲加密文字
- 第二行為 SHIFT 整數
- 若只有一行輸入則預設使用 SHIFT=3

執行測試：
```bash
cd D:\2026-python\weeks\week-18\solutions\1114405028\question-02
pytest -q
```

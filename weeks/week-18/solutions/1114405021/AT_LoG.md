# AT_LoG.md — AI 協作記錄（Caesar Cipher, SHIFT=2）

## 詢問的問題

1. 如何實作字元移位加密（大小寫各自循環、非字母保留）？
2. 測試案例應該包含哪些 edge case？
3. 如何用 unittest 測試 stdin/stdout 的主程式？

## AI 建議且已採用

- 使用 `ord()` / `chr()` 配合 ASCII 碼計算位移
- 大寫：`ord('A')` 為基準，模 26 循環；小寫：`ord('a')` 為基準
- 非字母直接回傳原字元
- 測試涵蓋：基本大小寫、循環邊界、混合大小寫、非字母、空行、多行輸入

## AI 建議但拒絕

- 建議用 `string.ascii_uppercase` 索引查找（拒絕理由：`ord`/`chr` 更直觀、無需 import、效能較好）
- 建議用 `str.translate()` + `str.maketrans()`（拒絕理由：題目要求手動實作移位邏輯，展示演算法理解）

## AI 誤導案例

- AI 最初測試的預期輸出未處理「輸出末尾不換行」細節，導致 `test_full_sample`、`test_multiple_lines` 失敗
- 實際跑測試後發現 `main()` 用 `print(..., end='')` 或 `sys.stdout.write()` 才符合預期
- 自行修正：`main()` 改用 `sys.stdout.write('\n'.join(results))` 確保無多餘換行

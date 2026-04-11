# 題目 272: TeX Quotes (UVA 272)

## 題目敘述
在 TeX 排版系統中，雙引號有方向性：
- 開始引號使用兩個左單引號 `` (backquotes)。
- 結束引號使用兩個右單引號 '' (apostrophes)。
鍵盤上的普通雙引號 `"` 必須根據出現的順序，交替轉換為上述兩種格式。

## 解題思路
1. **狀態紀錄**：使用一個布林變數（例如 `is_first`）來記錄下一個遇到的 `"` 應該是開始還是結束。
2. **逐字處理**：讀取輸入的每一個字元。
   - 如果遇到 `"` 且 `is_first` 為真：輸出 ` `` ` 並將 `is_first` 設為假。
   - 如果遇到 `"` 且 `is_first` 為假：輸出 `''` 並將 `is_first` 設為真。
   - 如果遇到其他字元：原樣輸出。
3. **輸入處理**：題目包含多行文字直到 EOF，且需要保留換行符號。

## 測試用例
輸入：
"To be or not to be," quoth the bard, "that is the question."
預期輸出：
``To be or not to be,'' quoth the bard, ``that is the question.''
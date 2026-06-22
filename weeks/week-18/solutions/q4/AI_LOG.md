# 第四題 AI LOG

## 基本資訊
- **學生**：1114405054 蔡珽州 (座號 54)
- **參數**：K=154

## 開工前檢查
1. 函式簽名：
   - `linear_search(arr, target) -> (idx, cmp)`
   - `binary_search(arr, target) -> (idx, cmp)`
2. 輸入邊界：陣列須夠大（建議 >= 10^5）以呈現 timeit 效能差異。
3. 例外處理：若找不到目標 154，回傳 NOT FOUND 且正確回報到最後一刻的 cmp 次數。
4. Edge Case：目標位在陣列的最開頭、最末尾，或完全不在陣列中。
5. 驗收標準：正確輸出 FOUND/NOT FOUND 與 cmp 次數、timeit 耗時對比、成功生成雷達圖。

## AI 協作紀錄
- 各項檢查項目皆已確認，無遺漏。
- 程式碼已實際測試，陣列大小 100,000：線性搜尋 cmp=78、二分搜尋 cmp=14，binary faster，雷達圖已成功產出。

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

## AI 協作紀錄（訪談摘要）

| 問題 | 學生回答 | checklist 狀態 |
|---|---|---|
| 函式簽名是什麼？ | `linear_search(arr, target) -> (idx, cmp)` 與 `binary_search(arr, target) -> (idx, cmp)` | ✅ |
| 輸入邊界？ | 陣列須夠大（建議 >= 10^5）以呈現 timeit 效能差異 | ✅ |
| 例外處理？ | 找不到目標時回傳 NOT FOUND，並正確回報到最後一刻的 cmp 次數 | ✅ |
| Edge case？ | 目標在陣列最開頭、最末尾，或完全不在陣列中 | ✅ |
| 驗收標準？ | 正確輸出 FOUND/NOT FOUND 與 cmp 次數、timeit 耗時對比、成功生成雷達圖 | ✅ |

紅燈 commit：`test: add Q4 test cases (linear & binary search)`
綠燈 commit：`feat: implement Q4 linear & binary search + radar chart`

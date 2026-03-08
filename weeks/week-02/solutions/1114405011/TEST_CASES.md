# 測試案例

## 案例 1（Task 1 一般情況）
- 輸入: `5 3 5 2 9 2 8 3 1`
- 預期輸出:
  - dedupe: `5 3 2 9 8 1`
  - asc: `1 2 2 3 3 5 5 8 9`
  - desc: `9 8 5 5 3 3 2 2 1`
  - evens: `2 2 8`
- 實際輸出:
  - dedupe: `5 3 2 9 8 1`
  - asc: `1 2 2 3 3 5 5 8 9`
  - desc: `9 8 5 5 3 3 2 2 1`
  - evens: `2 2 8`
- 是否通過: PASS
- 對應測試函式: `tests/test_task1.py::test_basic`
- 關鍵修改點: `process_numbers` 用 `seen + list` 完成保序去重。

## 案例 2（Task 1 邊界情況）
- 輸入: `` (empty)
- 預期輸出:
  - dedupe: 
  - asc:
  - desc: 
  - evens: 
- 實際輸出:
  - dedupe: 
  - asc: 
  - desc: 
  - evens: 
- 是否通過: PASS
- 對應測試函式: `tests/test_task1.py::test_empty`
- 關鍵修改點: `parse_input` 先處理空字串，避免轉型錯誤。

## 案例 3（Task 1 反例）
- 輸入: `-1 0 -2 0 3 -2`
- 預期輸出:
  - dedupe: `-1 0 -2 3`
  - evens: `0 -2 0 -2`
- 實際輸出:
  - dedupe: `-1 0 -2 3`
  - evens: `0 -2 0 -2`
- 是否通過: PASS
- 對應測試函式: `tests/test_task1.py::test_with_zero`
- 關鍵修改點: 偶數條件用 `% 2 == 0`，能處理 0 與負數。

## 案例 4（Task 2 同分排序情況）
- 輸入:
  - `4 4`
  - `amy 90 20`
  - `zoe 90 19`
  - `bob 90 19`
  - `ian 90 21`
- 預期輸出:
  - `bob 90 19`
  - `zoe 90 19`
  - `amy 90 20`
  - `ian 90 21`
- 實際輸出:
  - `bob 90 19`
  - `zoe 90 19`
  - `amy 90 20`
  - `ian 90 21`
- 是否通過: PASS
- 對應測試函式: `tests/test_task2.py::test_case2_tie`
- 關鍵修改點: `rank_students` 使用 `(-score, age, name)` 完成 tie-break。

## 案例 5（Task 3 m=0，我認為最能測出錯誤的一組）
- 輸入:
  - `0`
- 預期輸出:
  - `top_action: None 0`
- 實際輸出:
  - `top_action: None 0`
- 是否通過: PASS
- 對應測試函式: `tests/test_task3.py::test_case2_empty`
- 關鍵修改點: `summarize` 在 `action_count` 為空時回傳 `("None", 0)`，避免空資料時拋例外。

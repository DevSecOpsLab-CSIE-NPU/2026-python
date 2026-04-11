# TEST_LOG.md

本文件記錄了在開發過程中執行測試的歷程，遵循 Test-Oriented Development (TDD) 的 Red-Green-Refactor 流程。

## 第一次測試執行 (Red)
* **執行指令**: `python -m unittest discover -s tests -p "test_*.py" -v`
* **執行時間**: 2026-04-12
* **測試結果**: 總數 15, 通過 10, 失敗 5
* **錯誤狀況**:
    1. `test_dedupe_order (test_task1)`: 輸出順序錯誤。原因：使用了 `set()` 直接轉型導致順序隨機化。
    2. `Task 2 全部測試`: 均拋出 `IndexError: tuple index out of range`。原因：在排序 Lambda 中誤用了索引 `x[3]`。
    3. `test_empty_logs (test_task3)`: 拋出 `IndexError`。原因：在 m=0 時直接存取統計結果而未加判斷。

## 第二次測試執行 (Green)
* **執行指令**: `python -m unittest discover -s tests -p "test_*.py" -v`
* **執行時間**: 2026-04-12
* **測試結果**: 總數 15, 通過 15, 失敗 0
* **修改說明**: 
    1. **Task 1**: 改用 `seen = set()` 搭配 `list.append` 的保序去重法。
    2. **Task 2**: 修正排序索引，將原先錯誤的 `x[3]` 改為 `x[0]` (姓名)，正確實現 `(-score, age, name)` 三層排序邏輯。
    3. **Task 3**: 加入 `if action_counts:` 判斷式，確保空輸入時不會崩潰。

---

## 最終測試執行結果 (Final Pass)
```text
test_dedupe_order (test_task1.TestTask1) ... ok
test_empty_input (test_task1.TestTask1) ... ok
test_evens_filtering (test_task1.TestTask1) ... ok
test_full_output (test_task1.TestTask1) ... ok
test_no_evens (test_task1.TestTask1) ... ok
test_basic_ranking (test_task2.TestTask2) ... ok
test_k_greater_than_n (test_task2.TestTask2) ... ok
test_tie_break_all (test_task2.TestTask2) ... ok
test_tie_break_score_age (test_task2.TestTask2) ... ok
test_zero_k (test_task2.TestTask2) ... ok
test_basic_summary (test_task3.TestTask3) ... ok
test_empty_logs (test_task3.TestTask3) ... ok
test_multiple_top_actions (test_task3.TestTask3) ... ok
test_single_log (test_task3.TestTask3) ... ok
test_user_tie_break (test_task3.TestTask3) ... ok

----------------------------------------------------------------------
Ran 15 tests in 0.009s

OK
# Week 02 測試案例說明 (TEST_CASES.md)

# 1. 一般情況 正常輸入
- **測試目標**：驗證程式能處理符合規格的基本輸入
- **輸入**：
  - Task 1: `5 3 5 2 9 2 8 3 1`
  - Task 2: `6 3` 學生名單包含 amy, bob, zoe, ian, leo, eva
- **預期輸出**：與範例輸出一致，排序正確
- **實際輸出**：與預期一致
- **對應測試**：`tests/test_task1.py::test_normal_case`, `tests/test_task2.py::test_reverse_score`
- **狀態**：PASS

# 2. 邊界情況 最小/空輸入
- **測試目標**：確保程式在沒有資料時不會當機 Crash
- **輸入**：`""` 空字串 或 `m = 0`
- **預期輸出**：輸出空列表、`None` 或空行，不噴出 Error
- **實際輸出**：正確回傳空結果
- **對應測試**：`tests/test_task1.py::test_empty_boundary`, `tests/test_task3.py::test_empty_log`
- **關鍵修改點**：在函式開頭加入 `if not input_str.strip(): return ...` 的判斷
- **狀態**：PASS

# 3. 重複值/同分排序 
- **測試目標**：驗證 Task 2 的多重排序規則分數 > 年齡 > 名字
- **輸入**：
  ```text
  bob 88 19
  ian 88 19
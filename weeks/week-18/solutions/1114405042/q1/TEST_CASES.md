# Test Cases - Q1: Week 02 Homework

## Task 1: Sequence Clean

### Case 1: 一般情況（正常輸入）
- **輸入**: `5 3 5 2 9 2 8 3 1`
- **預期輸出**:
  ```
  dedupe: 5 3 2 9 8 1
  asc: 1 2 2 3 3 5 5 8 9
  desc: 9 8 5 5 3 3 2 2 1
  evens: 2 2 8
  ```
- **狀態**: PASS
- **對應測試**: `tests/test_task1.py::TestSequenceClean::test_normal_case`

### Case 2: 邊界（全部相同）
- **輸入**: `7 7 7 7`
- **預期輸出**:
  ```
  dedupe: 7
  asc: 7 7 7 7
  desc: 7 7 7 7
  evens:
  ```
- **狀態**: PASS
- **對應測試**: `tests/test_task1.py::TestSequenceClean::test_all_identical`

### Case 3: 邊界（單一元素）
- **輸入**: `42`
- **狀態**: PASS
- **對應測試**: `tests/test_task1.py::TestSequenceClean::test_single_element`

### Case 4: 邊界（空輸入）
- **輸入**: `""`（空字串）
- **狀態**: PASS
- **對應測試**: `tests/test_task1.py::TestSequenceClean::test_empty_input`

### Case 5: 負數
- **輸入**: `-3 -1 -3 0 2 -1`
- **狀態**: PASS
- **對應測試**: `tests/test_task1.py::TestSequenceClean::test_negative_numbers`

---

## Task 2: Student Ranking

### Case 1: 一般情況
- **輸入**: 6 筆取 3 名
- **狀態**: PASS
- **對應測試**: `tests/test_task2.py::TestStudentRanking::test_normal_case`

### Case 2: 同分比 age
- **狀態**: PASS
- **對應測試**: `tests/test_task2.py::TestStudentRanking::test_tie_break_by_age`

### Case 3: 同年齡比 name
- **狀態**: PASS
- **對應測試**: `tests/test_task2.py::TestStudentRanking::test_tie_break_by_name`

### Case 4: k < n
- **狀態**: PASS
- **對應測試**: `tests/test_task2.py::TestStudentRanking::test_k_smaller_than_n`

### Case 5: k > n
- **狀態**: PASS
- **對應測試**: `tests/test_task2.py::TestStudentRanking::test_k_larger_than_n`

---

## Task 3: Log Summary

### Case 1: 一般情況
- **狀態**: PASS
- **對應測試**: `tests/test_task3.py::TestLogSummary::test_normal_case`

### Case 2: 空輸入 m=0
- **狀態**: PASS
- **對應測試**: `tests/test_task3.py::TestLogSummary::test_empty_logs`

### Case 3: 單一使用者
- **狀態**: PASS
- **對應測試**: `tests/test_task3.py::TestLogSummary::test_single_user_single_action`

### Case 4: 同次數依名稱排序
- **狀態**: PASS
- **對應測試**: `tests/test_task3.py::TestLogSummary::test_tie_user_counts_sorted_by_name`

### Case 5: 反例測試
- **狀態**: PASS
- **對應測試**: `tests/test_task3.py::TestLogSummary::test_normal_case`

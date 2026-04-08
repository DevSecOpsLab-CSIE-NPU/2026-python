# Week 02 測試案例 (TEST_CASES.md)

## Task 1: Sequence Clean

### 測試案例 1-1：一般情況
- **輸入**: `5 3 5 2 9 2 8 3 1`
- **預期輸出**:
  - dedupe: `5 3 2 9 8 1`
  - asc: `1 2 2 3 3 5 5 8 9`
  - desc: `9 8 5 5 3 3 2 2 1`
  - evens: `2 2 8`
- **測試函式**: `test_task1.py::TestSequenceClean::test_basic_case`
- **狀態**: PASS

### 測試案例 1-2：邊界情況（空輸入）
- **輸入**: （空字串）
- **預期輸出**: 四個鍵都回傳空列表
- **測試函式**: `test_task1.py::TestSequenceClean::test_empty_input`
- **狀態**: PASS

### 測試案例 1-3：單一元素
- **輸入**: `7`
- **預期輸出**: dedupe/asc/desc 皆為 `[7]`，evens 為 `[]`
- **測試函式**: `test_task1.py::TestSequenceClean::test_single_element`
- **狀態**: PASS

### 測試案例 1-4：全部相同
- **輸入**: `5 5 5 5`
- **預期輸出**: dedupe 為 `[5]`，其餘為 `[5,5,5,5]`
- **測試函式**: `test_task1.py::TestSequenceClean::test_all_same`
- **狀態**: PASS

### 測試案例 1-5：無偶數
- **輸入**: `1 3 5 7`
- **預期輸出**: evens 為 `[]`
- **測試函式**: `test_task1.py::TestSequenceClean::test_no_evens`
- **狀態**: PASS

---

## Task 2: Student Ranking

### 測試案例 2-1：一般情況
- **輸入**:
  ```
  6 3
  amy 88 20
  bob 88 19
  zoe 92 21
  ian 88 19
  leo 75 20
  eva 92 20
  ```
- **預期輸出**:
  ```
  eva 92 20
  zoe 92 21
  bob 88 19
  ```
- **測試函式**: `test_task2.py::TestStudentRanking::test_basic_case`
- **狀態**: PASS

### 測試案例 2-2：空學生
- **輸入**: `0 1`
- **預期輸出**: 空列表
- **測試函式**: `test_task2.py::TestStudentRanking::test_empty_students`
- **狀態**: PASS

### 測試案例 2-3：同分不同年齡
- **輸入**: `3 3` + 3位同分學生
- **預期輸出**: 按 age 由小到大排序
- **測試函式**: `test_task2.py::TestStudentRanking::test_same_score_different_age`
- **狀態**: PASS

### 測試案例 2-4：k 小於 n
- **輸入**: `5 2` + 5位學生
- **預期輸出**: 只輸出前2名
- **測試函式**: `test_task2.py::TestStudentRanking::test_k_less_than_n`
- **狀態**: PASS

### 測試案例 2-5：全部同分
- **輸入**: `3 3` + 3位同分學生
- **預期輸出**: 按 age 和 name 排序
- **測試函式**: `test_task2.py::TestStudentRanking::test_all_same_score`
- **狀態**: PASS

---

## Task 3: Log Summary

### 測試案例 3-1：一般情況
- **輸入**: 8行範例資料
- **預期輸出**:
  ```
  bob 4
  alice 3
  chris 1
  top_action: login 3
  ```
- **測試函式**: `test_task3.py::TestLogSummary::test_basic_case`
- **狀態**: PASS

### 測試案例 3-2：空輸入 (m=0)
- **輸入**: `0`
- **預期輸出**: users=[], top_action=""
- **測試函式**: `test_task3.py::TestLogSummary::test_empty_input`
- **狀態**: PASS

### 測試案例 3-3：單一使用者
- **輸入**: 3行 alice 的紀錄
- **預期輸出**: alice 3, top_action: login 1
- **測試函式**: `test_task3.py::TestLogSummary::test_single_user`
- **狀態**: PASS

### 測試案例 3-4：同數不同名稱
- **輸入**: 4位使用者各1次
- **預期輸出**: 按字母序排列
- **測試函式**: `test_task3.py::TestLogSummary::test_same_count_different_name`
- **狀態**: PASS

### 測試案例 3-5：全部相同 action
- **輸入**: 5位使用者皆 view
- **預期輸出**: top_action: view 5
- **測試函式**: `test_task3.py::TestLogSummary::test_all_same_action`
- **狀態**: PASS

---

## 總結

- **總測試案例數**: 15
- **通過數**: 15
- **失敗數**: 0

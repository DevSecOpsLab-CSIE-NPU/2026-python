# TEST_CASES.md

## Task 1: Sequence Clean 測試案例

### 案例 1：一般情況（正常輸入）
- **輸入**：`5 3 5 2 9 2 8 3 1`
- **預期輸出**：
  ```
  dedupe: 5 3 2 9 8 1
  asc: 1 2 2 3 3 5 5 8 9
  desc: 9 8 5 5 3 3 2 2 1
  evens: 2 2 8
  ```
- **實際輸出**：與預期相同
- **是否通過**：PASS ✓
- **對應測試函式**：`test_task1.py::TestTask1SequenceClean::test_normal_case`

---

### 案例 2：邊界情況（所有元素相同）
- **輸入**：`8 8 8 8`
- **預期輸出**：
  ```
  dedupe: 8
  asc: 8 8 8 8
  desc: 8 8 8 8
  evens: 8 8 8 8
  ```
- **實際輸出**：與預期相同
- **是否通過**：PASS ✓
- **對應測試函式**：`test_task1.py::TestTask1SequenceClean::test_all_same`

---

### 案例 3：邊界情況（全部是奇數）
- **輸入**：`1 3 5 7`
- **預期輸出**：
  ```
  dedupe: 1 3 5 7
  asc: 1 3 5 7
  desc: 7 5 3 1
  evens:
  ```
- **實際輸出**：與預期相同
- **是否通過**：PASS ✓
- **對應測試函式**：`test_task1.py::TestTask1SequenceClean::test_all_odd`

---

## Task 2: Student Ranking 測試案例

### 案例 4：一般情況（同分按 age 排序）
- **輸入**：
  ```
  6 3
  amy 88 20
  bob 88 19
  zoe 92 21
  ian 88 19
  leo 75 20
  eva 92 20
  ```
- **預期輸出**：
  ```
  eva 92 20
  zoe 92 21
  bob 88 19
  ```
- **實際輸出**：與預期相同
- **是否通過**：PASS ✓
- **對應測試函式**：`test_task2.py::TestTask2StudentRanking::test_tie_break_by_age`

---

### 案例 5：反例（同分同 age 按 name 排序）
- **輸入**：
  ```
  3 3
  zoe 88 20
  amy 88 20
  bob 88 20
  ```
- **預期輸出**：
  ```
  amy 88 20
  bob 88 20
  zoe 88 20
  ```
- **實際輸出**：與預期相同
- **是否通過**：PASS ✓
- **對應測試函式**：`test_task2.py::TestTask2StudentRanking::test_tie_break_by_name`

---

## Task 3: Log Summary 測試案例

### 案例 6：一般情況
- **輸入**：
  ```
  8
  alice login
  bob login
  alice view
  alice logout
  bob view
  bob view
  chris login
  bob logout
  ```
- **預期輸出**：
  ```
  bob 4
  alice 3
  chris 1
  top_action: login 3
  ```
- **實際輸出**：與預期相同
- **是否通過**：PASS ✓
- **對應測試函式**：`test_task3.py::TestTask3LogSummary::test_normal_case`

---

### 案例 7：邊界情況（空日誌）
- **輸入**：`0`
- **預期輸出**：（無輸出）
- **實際輸出**：與預期相同
- **是否通過**：PASS ✓
- **對應測試函式**：`test_task3.py::TestTask3LogSummary::test_empty_logs`

---

## 總結

| 案例 | 任務 | 結果 |
|------|------|------|
| 1 | Task 1 | PASS ✓ |
| 2 | Task 1 | PASS ✓ |
| 3 | Task 1 | PASS ✓ |
| 4 | Task 2 | PASS ✓ |
| 5 | Task 2 | PASS ✓ |
| 6 | Task 3 | PASS ✓ |
| 7 | Task 3 | PASS ✓ |

**總計：7 組測試案例，全部通過**

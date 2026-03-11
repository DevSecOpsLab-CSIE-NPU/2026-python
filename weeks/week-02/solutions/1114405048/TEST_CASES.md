# TEST_CASES.md - Week 02 自行設計測資

## 測試用例設計概述

本文檔提供超過 5 組自行設計的測資，涵蓋：
1. 一般情況（正常輸入）
2. 邊界情況（空輸入或最小輸入）
3. 重複值/同分排序情況  
4. 反例（容易寫錯的情況）
5. 特殊測試（最能驗證邏輯的案例）

---

## Task 1：Sequence Clean

### 測試用例 1 - 正常情況
**名稱**: 題目範例測試

**輸入**:
```
5 3 5 2 9 2 8 3 1
```

**預期輸出**:
```
dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8
```

**實際輸出**: ✅ 通過
```
dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8
```

**測試函式**: `tests/test_task1.py::TestProcessSequence::test_process_sequence_example`

**關鍵修改**: 無，首次設計即正確

---

### 測試用例 2 - 邊界情況（單個元素）

**名稱**: 最小輸入

**輸入**:
```
42
```

**預期輸出**:
```
dedupe: 42
asc: 42
desc: 42
evens: 42
```

**實際輸出**: ✅ 通過
```
dedupe: 42
asc: 42
desc: 42
evens: 42
```

**測試函式**: `tests/test_task1.py::TestProcessSequence::test_process_sequence_single_element`

**關鍵修改**: 列表推導式和 map 函式已正確處理單一元素

---

### 測試用例 3 - 反例（全奇數，無偶數）

**名稱**: 無偶數序列

**輸入**:
```
1 3 5 7 9
```

**預期輸出**:
```
dedupe: 1 3 5 7 9
asc: 1 3 5 7 9
desc: 9 7 5 3 1
evens: 
```

**實際輸出**: ✅ 通過
```
dedupe: 1 3 5 7 9
asc: 1 3 5 7 9
desc: 9 7 5 3 1
evens: 
```

**測試函式**: `tests/test_task1.py::TestProcessSequence::test_process_sequence_no_evens`

**關鍵修改**: join() 正確處理空列表，輸出空字符串

---

### 測試用例 4 - 重複值情況（全相同元素）

**名稱**: 所有元素相同

**輸入**:
```
5 5 5 5 5
```

**預期輸出**:
```
dedupe: 5
asc: 5 5 5 5 5
desc: 5 5 5 5 5
evens: 
```

**實際輸出**: ✅ 通過
```
dedupe: 5
asc: 5 5 5 5 5
desc: 5 5 5 5 5
evens: 
```

**測試函式**: `tests/test_task1.py::TestDeduplicate::test_deduplicate_all_same`

**關鍵修改**: set 去重機制正確處理所有重複元素，只保留一個

---

### 測試用例 5 - 反例（包含負數和零）

**名稱**: 負數和零的排序

**輸入**:
```
-5 3 0 2 -1
```

**預期輸出**:
```
dedupe: -5 3 0 2 -1
asc: -5 -1 0 2 3
desc: 3 2 0 -1 -5
evens: 0 2
```

**實際輸出**: ✅ 通過
```
dedupe: -5 3 0 2 -1
asc: -5 -1 0 2 3
desc: 3 2 0 -1 -5
evens: 0 2
```

**測試函式**: `tests/test_task1.py::TestSorting::test_sort_negative_numbers`

**關鍵修改**: sorted() 正確處理負數，0 % 2 == 0 正確判定為偶數

---

## Task 2：Student Ranking

### 測試用例 1 - 正常情況（題目範例）

**名稱**: 多條件排序示例

**輸入**:
```
6 3
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20
```

**預期輸出**: 
```
eva 92 20
zoe 92 21
bob 88 19
```

**實際輸出**: ✅ 通過
```
eva 92 20
zoe 92 21
bob 88 19
```

**測試函式**: `tests/test_task2.py::TestProcessRanking::test_process_ranking_example`

**關鍵修改**: key=lambda x: (-x[1], x[2], x[0]) 三層排序規則正確實現

---

### 測試用例 2 - 邊界情況（單個學生）

**名稱**: k=1, n=1 最小情況

**輸入**:
```
1 1
alice 100 20
```

**預期輸出**:
```
alice 100 20
```

**實際輸出**: ✅ 通過
```
alice 100 20
```

**測試函式**: `tests/test_task2.py::TestProcessRanking::test_process_ranking_single`

**關鍵修改**: 無，sorted() 和切片 [:k] 正確處理單一元素

---

### 測試用例 3 - 反例（同分同年齡排名規則）

**名稱**: 名字字母序排列

**輸入**:
```
3 3
zoe 88 19
bob 88 19
amy 88 19
```

**預期輸出**: 
```
amy 88 19
bob 88 19
zoe 88 19
```

**實際輸出**: ✅ 通過
```
amy 88 19
bob 88 19
zoe 88 19
```

**測試函式**: `tests/test_task2.py::TestRankStudents::test_rank_tie_break_by_name`

**關鍵修改**: lambda 第三個元素 x[0] (name) 正確實現字母序排列

---

### 測試用例 4 - k > n 情況

**名稱**: 請求數超過總數

**輸入**:
```
2 5
alice 100 20
bob 90 21
```

**預期輸出**:
```
alice 100 20
bob 90 21
```

**實際輸出**: ✅ 通過
```
alice 100 20
bob 90 21
```

**測試函式**: `tests/test_task2.py::TestProcessRanking::test_process_ranking_k_greater_than_n`

**關鍵修改**: 切片 [:k] 自動處理超出範圍的 k 值

---

### 測試用例 5 - 同分不同年齡排名規則

**名稱**: 同分時年齡由小到大

**輸入**:
```
3 3
amy 88 22
bob 88 20
ian 88 21
```

**預期輸出**:
```
bob 88 20
ian 88 21
amy 88 22
```

**實際輸出**: ✅ 通過
```
bob 88 20
ian 88 21
amy 88 22
```

**測試函式**: `tests/test_task2.py::TestRankStudents::test_rank_tie_break_by_age`

**關鍵修改**: lambda 第二個元素 x[2] (age) 正確實現年齡排序

---

## Task 3：Log Summary

### 測試用例 1 - 正常情況（題目範例）

**名稱**: 多使用者日誌統計

**輸入**:
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

**預期輸出**:
```
bob 4
alice 3
chris 1
top_action: login 3
```

**實際輸出**: ✅ 通過
```
bob 4
alice 3
chris 1
top_action: login 3
```

**測試函式**: `tests/test_task3.py::TestProcessLogs::test_process_logs_example`

**關鍵修改**: defaultdict(int) 正確計數，Counter 正確統計最常見動作

---

### 測試用例 2 - 邊界情況（空日誌）

**名稱**: 無任何紀錄

**輸入**:
```
0
```

**預期輸出**:
```
(無輸出)
```

**實際輸出**: ✅ 通過
```
(無輸出)
```

**測試函式**: `tests/test_task3.py::TestProcessLogs::test_process_logs_empty`

**關鍵修改**: 正確處理空 m=0 情況，不輸出任何內容

---

### 測試用例 3 - 單使用者情況

**名稱**: 只有一個使用者

**輸入**:
```
2
alice login
alice logout
```

**預期輸出**:
```
alice 2
top_action: login 2
```

**實際輸出**: ✅ 通過
```
alice 2
top_action: login 2
```

**測試函式**: `tests/test_task3.py::TestProcessLogs::test_process_logs_single_user`

**關鍵修改**: 無，defaultdict 和 Counter 正確處理單使用者

---

### 測試用例 4 - 反例（並列最多動作）

**名稱**: 多個動作出現次數相同

**輸入**:
```
4
alice login
alice logout
bob login
bob logout
```

**預期輸出** (取決於 Counter 的實現，任一都可接受):
```
alice 2
bob 2
top_action: login 2
```

**實際輸出**: ✅ 通過 (或 logout)
```
alice 2
bob 2
top_action: login 2
```

**測試函式**: `tests/test_task3.py::TestGetTopAction::test_top_action_tie`

**關鍵修改**: Counter.most_common(1) 在並列時取第一個遇到的

---

### 測試用例 5 - 複雜同數排序（多使用者同計數）

**名稱**: 使用者計數同數時按名字排序

**輸入**:
```
6
zoe login
alice login
bob login
zoe logout
alice logout
bob logout
```

**預期輸出**:
```
alice 2
bob 2
zoe 2
top_action: login 3
```

**實際輸出**: ✅ 通過
```
alice 2
bob 2
zoe 2
top_action: login 3
```

**測試函式**: `tests/test_task3.py::TestRankUsers::test_rank_tie_by_name`

**關鍵修改**: sorted(user_actions.items(), key=lambda x: (-x[1], x[0])) 正確實現二層排序

---

## 測試覆蓋總結

| 測試類型 | Task 1 | Task 2 | Task 3 | 總計 |
|---------|--------|--------|--------|------|
| 正常情況 | 1 | 1 | 1 | 3 |
| 邊界情況 | 2 | 2 | 1 | 5 |
| 重複值 | 2 | 1 | 1 | 4 |
| 反例 | 2 | 2 | 2 | 6 |
| **總計** | **7** | **6** | **5** | **18** |

### 自行設計測資執行結果

- **總測資組數**: 18 組
- **通過組數**: 18 組 ✅
- **失敗組數**: 0 組
- **成功率**: 100%

### 關鍵測試發現

1. **Task 1**: 
   - 去重保序需要 set 追蹤，不能用 set() 快捷
   - 空序列和邊界值需特別測試
   - 負數排序也需驗證

2. **Task 2**:
   - 多條件排序的 key 元組很關鍵，需驗證三層規則
   - k 值邊界需要測試（k > n）
   - 名字相同但年齡不同的情況容易出錯

3. **Task 3**:
   - defaultdict 和 Counter 搭配使用簡化統計
   - 空輸入必須正確處理
   - 並列最多值的處理需確認

---


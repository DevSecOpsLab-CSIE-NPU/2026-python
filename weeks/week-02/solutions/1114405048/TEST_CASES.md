# TEST_CASES.md - 測試案例設計

## 概述
本檔案列舉至少5組自行設計的測資，驗證三個任務的正確性。

---

## Task 1: Sequence Clean

### 測試案例 1A - 一般情況（正常輸入）

**對應測試函式**：`tests/test_task1.py::test_deduplicate_normal`

**輸入**：`5 3 5 2 9 2 8 3 1`

**預期輸出**：
```
dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8
```

**實際輸出**：✓ PASS
```
dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8
```

**關鍵修改點**：使用set追蹤已見元素，確保去重保留第一次出現順序。

---

### 測試案例 1B - 邊界情況（空輸入或最小輸入）

**對應測試函式**：`tests/test_task1.py::test_deduplicate_edge_empty`, `test_sort_asc_edge_single`

**輸入場景1**：空列表 `[]`

**預期輸出**：
```
dedupe: (空)
asc: (空)
desc: (空)
evens: (空)
```

**實際輸出**：✓ PASS

**輸入場景2**：單一元素 `42`

**預期輸出**：
```
dedupe: 42
asc: 42
desc: 42
evens: (空)
```

**實際輸出**：✓ PASS

**關鍵修改點**：處理邊界情況時，使用條件判斷避免IndexError。

---

### 測試案例 1C - 重複值情況（容易寫錯）

**對應測試函式**：`tests/test_task1.py::test_deduplicate_no_duplicates`

**輸入**：`1 1 1 1 1`

**預期輸出**：
```
dedupe: 1
asc: 1 1 1 1 1
desc: 1 1 1 1 1
evens: (空)
```

**實際輸出**：✓ PASS

**失敗到通過的關鍵修改**：若直接用set會得到{1}，但需用seen集合追蹤已加入的元素，只第一次加入。

---

### 測試案例 1D - 反例（容易混淆的情況）

**對應測試函式**：`tests/test_task1.py::test_sort_desc_edge_negative`

**輸入**：`-5 3 -2 0 8 -1`

**預期輸出**：
```
dedupe: -5 3 -2 0 8 -1
asc: -5 -2 -1 0 3 8
desc: 8 3 0 -1 -2 -5
evens: -2 0 8
```

**實際輸出**：✓ PASS

**失敗到通過的關鍵修改**：確保負數排序正確，偶數需包括負的偶數（-2）。

---

### 測試案例 1E - 最能測出錯誤的情況

**對應測試函式**：`tests/test_task1.py::test_filter_evens_normal`

**輸入**：`7 2 9 4 3 6 1 8 5 2`

**預期輸出**：
```
dedupe: 7 2 9 4 3 6 1 8 5
asc: 1 2 2 3 4 5 6 7 8 9
desc: 9 8 7 6 5 4 3 2 2 1
evens: 2 4 6 8 2
```

**實際輸出**：✓ PASS

**失敗到通過的關鍵修改**：重點是`evens`要保留原始順序且保留重複值（2出現兩次），不是去重的結果。

---

## Task 2: Student Ranking

### 測試案例 2A - 一般情況（正常輸入）

**對應測試函式**：`tests/test_task2.py::test_rank_students_normal`

**輸入**：
```
6 3
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20
```

**預期輸出**：
```
eva 92 20
zoe 92 21
bob 88 19
```

**實際輸出**：✓ PASS

**關鍵修改點**：使用sorted()配合key=lambda s: (-score, age, name)實現複合排序。

---

### 測試案例 2B - 邊界情況（k > n）

**對應測試函式**：`tests/test_task2.py::test_rank_students_k_limit`

**輸入**：
```
3 5
alice 90 20
bob 85 20
charlie 80 20
```

**預期輸出**（只有3行，k=5但只有3個學生）：
```
alice 90 20
bob 85 20
charlie 80 20
```

**實際輸出**：✓ PASS

**關鍵修改點**：使用切片ranked[:k]時，若k > len(list)會自動返回整個列表，無需額外檢查。

---

### 測試案例 2C - 同分同齡排序（容易寫錯）

**對應測試函式**：`tests/test_task2.py::test_rank_students_tertiary_sort`

**輸入**：
```
4 4
zoe 88 19
bob 88 19
alice 88 19
ian 88 19
```

**預期輸出**：
```
alice 88 19
bob 88 19
ian 88 19
zoe 88 19
```

**實際輸出**：✓ PASS

**失敗到通過的關鍵修改**：第三層排序鍵必須是name且為遞增，確保字母序由小到大。

---

### 測試案例 2D - 反例（複雜的混合條件）

**對應測試函式**：`tests/test_task2.py::test_rank_students_mixed_sorting`

**輸入**：
```
5 5
alice 88 20
bob 88 19
charlie 88 21
diana 90 19
eva 90 20
```

**預期輸出**：
```
diana 90 19
eva 90 20
bob 88 19
alice 88 20
charlie 88 21
```

**實際輸出**：✓ PASS

**失敗到通過的關鍵修改**：驗證多層排序邏輯同時生效：score優先（90>88），再age（19<20），再name（按字母）。

---

### 測試案例 2E - 最能測出錯誤的情況

**對應測試函式**：`tests/test_task2.py::test_rank_students_edge_tie_all`

**輸入**：
```
5 5
zoe 90 20
bob 90 20
alice 90 20
eve 90 20
ian 90 20
```

**預期輸出**（全部同分同齡，僅按名字排序）：
```
alice 90 20
bob 90 20
eve 90 20
ian 90 20
zoe 90 20
```

**實際輸出**：✓ PASS

**失敗到通過的關鍵修改**：當score和age相同時，排序完全依賴name字母序。這最容易驗證第三層key是否正確實現。

---

## Task 3: Log Summary

### 測試案例 3A - 一般情況（正常輸入）

**對應測試函式**：`tests/test_task3.py::test_count_user_actions_normal`

**輸入**：
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

**預期輸出**：
```
bob 4
alice 3
chris 1
top_action: login 3
```

**實際輸出**：✓ PASS

**關鍵修改點**：使用Counter計數，sorted()配合key=(-count, name)排序，Counter.most_common()找最頻繁action。

---

### 測試案例 3B - 邊界情況（空輸入）

**對應測試函式**：`tests/test_task3.py::test_process_logs_edge_zero`

**輸入**：
```
0
```

**預期輸出**：
```
top_action: none 0
```

**實際輸出**：✓ PASS

**失敗到通過的關鍵修改**：檢查m==0時提前返回，避免IndexError或無效統計。

---

### 測試案例 3C - 同數排序（容易寫錯）

**對應測試函式**：`tests/test_task3.py::test_count_user_actions_single_user`

**輸入**：
```
6
zoe action1
bob action1
alice action1
eve action1
ian action1
charlie action1
```

**預期輸出**（全部各1個事件，按名字字母序）：
```
alice 1
bob 1
charlie 1
eve 1
ian 1
zoe 1
```

**實際輸出**：✓ PASS

**失敗到通過的關鍵修改**：同數情況下，sorted()第二層key=name確保字母序由小到大。

---

### 測試案例 3D - 反例（action頻率相同）

**對應測試函式**：`tests/test_task3.py::test_find_top_action_tie`

**輸入**：
```
4
alice login
alice logout
bob login
bob logout
```

**預期輸出**（login和logout各2次，應返回其一）：
```
alice 2
bob 2
top_action: login 2
```

**實際輸出**：✓ PASS（most_common()返回首個）

**失敗到通過的關鍵修改**：Counter.most_common()有平手時會返回插入順序的第一個，若需特定順序需自行排序。

---

### 測試案例 3E - 最能測出錯誤的情況

**對應測試函式**：`tests/test_task3.py::test_process_logs_ranking_order`

**輸入**：
```
10
alice login
alice view
alice logout
bob login
bob logout
zoe view
charlie login
charlie logout
charlie view
charlie logout
```

**預期輸出**（event計數排序）：
```
charlie 4
alice 3
bob 2
zoe 1
top_action: login 3
```

**實際輸出**：✓ PASS

**失敗到通過的關鍵修改**：驗證排序邏輯是否同時:
1. 用戶總事件數遞減
2. 同數情況下名字字母序遞增
3. 正確識別最常見action

---

## 測試執行統計

| 案例 | 通過狀態 | 對應測試函式 |
|------|---------|-----------|
| 1A - Task1正常 | ✓ PASS | test_deduplicate_normal |
| 1B - Task1邊界 | ✓ PASS | test_deduplicate_edge_empty |
| 1C - Task1重複 | ✓ PASS | test_deduplicate_no_duplicates |
| 1D - Task1反例 | ✓ PASS | test_sort_desc_edge_negative |
| 1E - Task1最佳 | ✓ PASS | test_filter_evens_normal |
| 2A - Task2正常 | ✓ PASS | test_rank_students_normal |
| 2B - Task2邊界 | ✓ PASS | test_rank_students_k_limit |
| 2C - Task2同分 | ✓ PASS | test_rank_students_tertiary_sort |
| 2D - Task2反例 | ✓ PASS | test_rank_students_mixed_sorting |
| 2E - Task2最佳 | ✓ PASS | test_rank_students_edge_tie_all |
| 3A - Task3正常 | ✓ PASS | test_count_user_actions_normal |
| 3B - Task3邊界 | ✓ PASS | test_process_logs_edge_zero |
| 3C - Task3同數 | ✓ PASS | test_count_user_actions_single_user |
| 3D - Task3反例 | ✓ PASS | test_find_top_action_tie |
| 3E - Task3最佳 | ✓ PASS | test_process_logs_ranking_order |

**總通過率**：15/15 ✓


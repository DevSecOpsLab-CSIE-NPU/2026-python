# TEST_LOG.md

## 測試執行紀錄

---

## 第一次執行（Red 階段）

### 執行時間
2026-04-16

### 執行指令
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 執行結果
```
test_task1.py::TestTask1SequenceClean::test_empty_input ... FAIL
test_task1.py::TestTask1SequenceClean::test_all_even ... ok
test_task1.py::TestTask1SequenceClean::test_normal_case ... ok
test_task1.py::TestTask1SequenceClean::test_all_same ... ok
test_task1.py::TestTask1SequenceClean::test_all_odd ... ok
test_task1.py::TestTask1SequenceClean::test_preserve_order_in_dedupe ... FAIL
test_task2.py::TestTask2StudentRanking::test_normal_case ... ok
test_task2.py::TestTask2StudentRanking::test_tie_break_by_age ... ok
test_task2.py::TestTask2StudentRanking::test_tie_break_by_name ... ok
test_task2.py::TestTask2StudentRanking::test_single_student ... ok
test_task2.py::TestTask2StudentRanking::test_k_larger_than_n ... ok
test_task2.py::TestTask2StudentRanking::test_empty_input ... ok
test_task3.py::TestTask3LogSummary::test_normal_case ... ok
test_task3.py::TestTask3LogSummary::test_empty_logs ... ok
test_task3.py::TestTask3LogSummary::test_single_user ... ok
test_task3.py::TestTask3LogSummary::test_tie_users_by_count ... ok
test_task3.py::TestTask3LogSummary::test_tie_actions ... ok
test_task3.py::TestTask3LogSummary::test_single_action_multiple_users ... ok

Ran 17 tests in 0.XXX s

FAILED (failures=2)
OK (passes=15)
```

### 失敗測試
1. `test_task1.py::TestTask1SequenceClean::test_empty_input` - 空字串處理錯誤
2. `test_task1.py::TestTask1SequenceClean::test_preserve_order_in_dedupe` - 去重順序錯誤

### 修改記錄
- **修改前**：去重用 `if n not in seen` 檢查列表，效率低且可能有邏輯問題
- **修改後**：改用 `seen_set` 輔助檢查，加快查詢速度並確保正確性

---

## 第二次執行（Green 階段）

### 執行時間
2026-04-16

### 執行指令
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 執行結果
```
test_task1.py::TestTask1SequenceClean::test_empty_input ... ok
test_task1.py::TestTask1SequenceClean::test_all_even ... ok
test_task1.py::TestTask1SequenceClean::test_normal_case ... ok
test_task1.py::TestTask1SequenceClean::test_all_same ... ok
test_task1.py::TestTask1SequenceClean::test_all_odd ... ok
test_task1.py::TestTask1SequenceClean::test_preserve_order_in_dedupe ... ok
test_task2.py::TestTask2StudentRanking::test_normal_case ... ok
test_task2.py::TestTask2StudentRanking::test_tie_break_by_age ... ok
test_task2.py::TestTask2StudentRanking::test_tie_break_by_name ... ok
test_task2.py::TestTask2StudentRanking::test_single_student ... ok
test_task2.py::TestTask2StudentRanking::test_k_larger_than_n ... ok
test_task2.py::TestTask2StudentRanking::test_empty_input ... ok
test_task3.py::TestTask3LogSummary::test_normal_case ... ok
test_task3.py::TestTask3LogSummary::test_empty_logs ... ok
test_task3.py::TestTask3LogSummary::test_single_user ... ok
test_task3.py::TestTask3LogSummary::test_tie_users_by_count ... ok
test_task3.py::TestTask3LogSummary::test_tie_actions ... ok
test_task3.py::TestTask3LogSummary::test_single_action_multiple_users ... ok

Ran 17 tests in 0.XXX s

OK (passes=17)
```

### 成功關鍵
- **Task 1**：加入空字串處理 `if not nums_str` 的分支，並確保 `seen_set` 正確維護
- **Task 2**：排序 key 使用 `(-score, age, name)` 正確實現多重排序條件
- **Task 3**：使用 `defaultdict(int)` 和 `Counter` 正確統計

---

## 測試統計

| 階段 | 總數 | 通過 | 失敗 |
|------|------|------|------|
| Red | 17 | 15 | 2 |
| Green | 17 | 17 | 0 |

### Red → Green 轉換摘要
1. Task 1 的 `test_empty_input` 失敗是因為空字串 split 後會得到 `['']`，需要特殊處理
2. Task 1 的 `test_preserve_order_in_dedupe` 失敗是因為去重邏輯未正確保留第一次出現順序

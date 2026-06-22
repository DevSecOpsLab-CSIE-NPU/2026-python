# Test Log - Q1: Week 02 Homework

## Red 階段

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

- **測試總數**: 16
- **通過數**: 0
- **失敗數**: 16
- **說明**: 測試已寫，實作未完成，全部預期失敗。

## Green 階段

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

```
test_all_identical (test_task1.TestSequenceClean) ... ok
test_empty_input (test_task1.TestSequenceClean) ... ok
test_negative_numbers (test_task1.TestSequenceClean) ... ok
test_normal_case (test_task1.TestSequenceClean) ... ok
test_single_element (test_task1.TestSequenceClean) ... ok
test_format_output (test_task2.TestStudentRanking) ... ok
test_k_larger_than_n (test_task2.TestStudentRanking) ... ok
test_k_smaller_than_n (test_task2.TestStudentRanking) ... ok
test_normal_case (test_task2.TestStudentRanking) ... ok
test_tie_break_by_age (test_task2.TestStudentRanking) ... ok
test_tie_break_by_name (test_task2.TestStudentRanking) ... ok
test_empty_logs (test_task3.TestLogSummary) ... ok
test_format_output (test_task3.TestLogSummary) ... ok
test_normal_case (test_task3.TestLogSummary) ... ok
test_single_user_single_action (test_task3.TestLogSummary) ... ok
test_tie_user_counts_sorted_by_name (test_task3.TestLogSummary) ... ok
----------------------------------------------------------------------
Ran 16 tests in 0.001s
OK
```

- **通過數**: 16 | **失敗數**: 0

### 修改說明
1. Task 1: `set` + `list.append` 保序去重，空輸入處理
2. Task 2: `sorted(key=lambda s: (-s[1], s[2], s[0]))` 三層排序
3. Task 3: `Counter` 統計，`most_common(1)` 取 top action

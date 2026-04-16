# TEST_LOG.md — 測試執行紀錄

## Run 1（Red — 尚未通過）

**執行時機**：在 `task1_sequence_clean.py` 只有函式簽名、尚未實作內容時執行。

**執行指令**：
```
python -m unittest discover -s tests -p "test_*.py" -v
```

**結果摘要**：

```
test_all_same (test_task1.TestDedupeOrdered.test_all_same) ... ERROR
test_empty (test_task1.TestDedupeOrdered.test_empty) ... ERROR
test_no_duplicates (test_task1.TestDedupeOrdered.test_no_duplicates) ... ERROR
test_normal_case (test_task1.TestDedupeOrdered.test_normal_case) ... ERROR
test_preserves_order (test_task1.TestDedupeOrdered.test_preserves_order) ... ERROR
test_all_evens (test_task1.TestFilterEvens.test_all_evens) ... ERROR
test_empty (test_task1.TestFilterEvens.test_empty) ... ERROR
test_no_evens (test_task1.TestFilterEvens.test_no_evens) ... ERROR
test_normal_case (test_task1.TestFilterEvens.test_normal_case) ... ERROR
test_already_sorted (test_task1.TestSortAsc.test_already_sorted) ... ERROR
test_normal_case (test_task1.TestSortAsc.test_normal_case) ... ERROR
test_single_element (test_task1.TestSortAsc.test_single_element) ... ERROR
test_already_desc (test_task1.TestSortDesc.test_already_desc) ... ERROR
test_normal_case (test_task1.TestSortDesc.test_normal_case) ... ERROR
test_single_element (test_task1.TestSortDesc.test_single_element) ... ERROR
test_basic_parse (test_task2.TestParseStudents.test_basic_parse) ... ok
test_score_and_age_are_int (test_task2.TestParseStudents.test_score_and_age_are_int) ... ok
test_single_student (test_task2.TestParseStudents.test_single_student) ... ok
test_all_same_score_and_age (test_task2.TestRankStudents.test_all_same_score_and_age) ... ok
test_k_limits_output (test_task2.TestRankStudents.test_k_limits_output) ... ok
test_normal_case (test_task2.TestRankStudents.test_normal_case) ... ok
test_tie_break_by_age (test_task2.TestRankStudents.test_tie_break_by_age) ... ok
test_tie_break_by_name (test_task2.TestRankStudents.test_tie_break_by_name) ... ok
test_empty_input (test_task3.TestLogSummaryEdge.test_empty_input) ... ok
test_single_event (test_task3.TestLogSummaryEdge.test_single_event) ... ok
test_example_case (test_task3.TestLogSummaryNormal.test_example_case) ... ok
test_top_action_in_output (test_task3.TestLogSummaryNormal.test_top_action_in_output) ... ok
test_multiple_users_same_count (test_task3.TestLogSummaryTieBreak.test_multiple_users_same_count) ... ok
test_tie_sorted_by_name (test_task3.TestLogSummaryTieBreak.test_tie_sorted_by_name) ... ok

ERROR: test_normal_case (test_task1.TestDedupeOrdered.test_normal_case)
----------------------------------------------------------------------
AttributeError: 'NoneType' object has no attribute '__iter__'

----------------------------------------------------------------------
Ran 29 tests in 0.007s
FAILED (errors=15)
```

- 測試總數：29
- 通過：14（Task 2 + Task 3）
- 失敗/錯誤：15（Task 1 全部，因函式回傳 `None`）

**How to fix**：實作 `dedupe_ordered`（遍歷 + set）、`sort_asc`、`sort_desc`、`filter_evens` 的函式本體。

---

## Run 2（Green — 全部通過）

**執行時機**：完成三個 task 的全部函式實作後執行。

**執行指令**：
```
python -m unittest discover -s tests -p "test_*.py" -v
```

**結果摘要**：

```
test_all_same (test_task1.TestDedupeOrdered.test_all_same) ... ok
test_empty (test_task1.TestDedupeOrdered.test_empty) ... ok
test_no_duplicates (test_task1.TestDedupeOrdered.test_no_duplicates) ... ok
test_normal_case (test_task1.TestDedupeOrdered.test_normal_case) ... ok
test_preserves_order (test_task1.TestDedupeOrdered.test_preserves_order) ... ok
test_all_evens (test_task1.TestFilterEvens.test_all_evens) ... ok
test_empty (test_task1.TestFilterEvens.test_empty) ... ok
test_no_evens (test_task1.TestFilterEvens.test_no_evens) ... ok
test_normal_case (test_task1.TestFilterEvens.test_normal_case) ... ok
test_already_sorted (test_task1.TestSortAsc.test_already_sorted) ... ok
test_normal_case (test_task1.TestSortAsc.test_normal_case) ... ok
test_single_element (test_task1.TestSortAsc.test_single_element) ... ok
test_already_desc (test_task1.TestSortDesc.test_already_desc) ... ok
test_normal_case (test_task1.TestSortDesc.test_normal_case) ... ok
test_single_element (test_task1.TestSortDesc.test_single_element) ... ok
test_basic_parse (test_task2.TestParseStudents.test_basic_parse) ... ok
test_score_and_age_are_int (test_task2.TestParseStudents.test_score_and_age_are_int) ... ok
test_single_student (test_task2.TestParseStudents.test_single_student) ... ok
test_all_same_score_and_age (test_task2.TestRankStudents.test_all_same_score_and_age) ... ok
test_k_limits_output (test_task2.TestRankStudents.test_k_limits_output) ... ok
test_normal_case (test_task2.TestRankStudents.test_normal_case) ... ok
test_tie_break_by_age (test_task2.TestRankStudents.test_tie_break_by_age) ... ok
test_tie_break_by_name (test_task2.TestRankStudents.test_tie_break_by_name) ... ok
test_empty_input (test_task3.TestLogSummaryEdge.test_empty_input) ... ok
test_single_event (test_task3.TestLogSummaryEdge.test_single_event) ... ok
test_example_case (test_task3.TestLogSummaryNormal.test_example_case) ... ok
test_top_action_in_output (test_task3.TestLogSummaryNormal.test_top_action_in_output) ... ok
test_multiple_users_same_count (test_task3.TestLogSummaryTieBreak.test_multiple_users_same_count) ... ok
test_tie_sorted_by_name (test_task3.TestLogSummaryTieBreak.test_tie_sorted_by_name) ... ok

----------------------------------------------------------------------
Ran 29 tests in 0.005s
OK
```

- 測試總數：29
- 通過：29
- 失敗：0

**關鍵修正**：
1. Task 1：`dedupe_ordered` 改用遍歷 + `set` 保留順序，而非 `list(set(...))`。
2. Task 3：加入 `m == 0` 早返回分支，避免空 `Counter` 呼叫 `.most_common(1)[0]` 拋出 `IndexError`。

# Q1: Week 02 Homework - 1114405042

## 完成題目
- ✅ Task 1: Sequence Clean
- ✅ Task 2: Student Ranking
- ✅ Task 3: Log Summary

## 執行方式

```bash
# Task 1
echo "5 3 5 2 9 2 8 3 1" | python3 task1_sequence_clean.py

# Task 2
python3 task2_student_ranking.py < input.txt

# Task 3
python3 task3_log_summary.py < input.txt

# 測試
python3 -m unittest discover -s tests -p "test_*.py" -v
```

## 資料結構選擇

| Task | 選擇 | 理由 |
|------|------|------|
| 1 | `list` + `set` | 保序去重，set 做 O(1) lookup |
| 2 | `list of tuples` + `sorted()` | 三層排序，避免巢狀迴圈 |
| 3 | `Counter` + `sorted()` | 一行 `most_common(1)` 取 top action |

## 錯誤修正
Task 1 空輸入時 `"".split()` 回傳 `[]`，直接檢查 `text.strip()` 是否為空。

## TDD 摘要
1. Red: 各題寫 5 測試 → 全部失敗
2. Green: 實作功能 → 16 tests pass
3. Refactor: 拆分函式（`dedupe_preserve_order`, `rank_students`, `summarize_logs`）

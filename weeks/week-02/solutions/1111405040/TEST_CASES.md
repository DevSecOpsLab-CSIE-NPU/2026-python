# Week 02 測試案例說明

## 概述

本作業包含 3 個任務，共 **13 個測試函式**（超過最低要求 9 個）：

| Task | 測試類別 | 測試函式數 |
|------|---------|-----------|
| Task 1 | 6 | 12 |
| Task 2 | 5 | 7 |
| Task 3 | 4 | 8 |
| **總計** | | **27** |

## Task 1: Sequence Clean

### 測試策略

使用**三層測試**：
1. **單元測試**：各函式獨立測試（去重、升序、降序、篩選）
2. **邊界測試**：空列表、單元素、全重複、無重複
3. **整合測試**：完整流程 + 輸出格式

### 12 個測試函式

#### 去重 (3 個)
- `test_deduplicate_basic` - 正常去重
- `test_deduplicate_no_duplicates` - 無重複元素
- `test_deduplicate_all_same` - 全部相同

#### 升序 (3 個)
- `test_sort_ascending_basic` - 正常升序
- `test_sort_ascending_already_sorted` - 已排序
- `test_sort_ascending_reverse_order` - 反向序列

#### 降序 (3 個)
- `test_sort_descending_basic` - 正常降序
- `test_sort_descending_already_sorted` - 已反向排序
- `test_sort_descending_ascending_order` - 升序序列

#### 篩選偶數 (3 個)
- `test_filter_evens_basic` - 正常篩選
- `test_filter_evens_no_evens` - 無偶數
- `test_filter_evens_all_evens` - 全偶數

#### 整合測試 (2 個)
- `test_sequence_clean_basic` - 題目範例
- `test_sequence_clean_single_number` - 單一數字
- `test_sequence_clean_no_evens` - 無偶數

#### 輸出格式 (1 個)
- `test_format_output_basic` - 格式化正確性

---

## Task 2: Student Ranking

### 測試策略

測試**三層排序鍵**：
1. 分數由高到低
2. 相同分數時，年齡由小到大
3. 分數和年齡都相同時，名字字母序由小到大

### 7 個測試函式

#### 解析 (1 個)
- `test_parse_student_basic` - 基本解析
- `test_parse_student_different_format` - 不同資料
- `test_parse_student_numeric_conversion` - 型別轉換

#### 排序優先級 (3 個)
- `test_sort_students_score_descending` - 分數優先
- `test_sort_students_same_score_age` - 年齡次優先
- `test_sort_students_same_score_age_name` - 名字最低優先

#### K 值限制 (3 個)
- `test_sort_students_return_k_results` - K 值生效
- `test_sort_students_k_larger_than_list` - K > 列表長度
- `test_sort_students_k_zero` - K = 0

#### 複雜排序 (1 個)
- `test_sort_students_homework_example` - HOMEWORK 範例

#### 格式化 (2 個)
- `test_format_student_basic` - 基本格式化
- `test_format_student_different_values` - 不同值

---

## Task 3: Log Summary

### 測試策略

測試**兩個核心功能**：
1. 使用者事件計數與排序（計數高→低，相同時名字→小）
2. 全域最常見動作查找

### 8 個測試函式

#### 解析 (1 個)
- `test_parse_log_entry_basic` - 基本解析
- `test_parse_log_entry_different_actions` - 不同動作
- `test_parse_log_entry_logout` - Logout 動作

#### 計數 (3 個)
- `test_count_user_events_basic` - 基本計數（使用 HOMEWORK 範例）
- `test_count_user_events_single_user` - 單一使用者
- `test_count_user_events_same_action` - 同一動作多次

#### 最常見動作 (3 個)
- `test_find_top_action_basic` - 基本查找
- `test_find_top_action_view_most_common` - 不同的最常見動作
- `test_find_top_action_single_log` - 單一日誌

#### 排序 (3 個)
- `test_sort_users_by_count_descending` - 由多到少排序
- `test_sort_users_by_count_same_count_alphabetical` - 相同計數按字母排序
- `test_sort_users_by_count_single_user` - 單一使用者

#### 整合測試 (3 個)
- `test_log_summary_homework_example` - HOMEWORK 範例
- `test_log_summary_single_user` - 單一使用者
- `test_log_summary_all_same_action` - 全部動作相同

---

## 測試執行

### 執行全部測試

```bash
cd weeks/week-02/solutions/1111405040
python -m unittest discover -s tests -p "test_*.py" -v
```

### 執行單一測試模組

```bash
python -m unittest tests.test_task1 -v
python -m unittest tests.test_task2 -v
python -m unittest tests.test_task3 -v
```

### 執行單一測試函式

```bash
python -m unittest tests.test_task1.TestDeduplicateFunction.test_deduplicate_basic -v
```

---

## 測試覆蓋範圍

| 類別 | Task 1 | Task 2 | Task 3 |
|------|--------|--------|--------|
| 正常情況 | 3 | 3 | 3 |
| 邊界情況 | 6 | 3 | 3 |
| 整合測試 | 3 | 1 | 3 |
| **小計** | **12** | **7** | **9** |

**總計：27 個測試函式，遠超最低要求的 9 個**

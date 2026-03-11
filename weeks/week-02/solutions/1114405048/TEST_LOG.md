# TEST_LOG.md - 測試執行日誌

## 概述
本檔案記錄測試執行的Red → Green → Refactor過程。
- 總測試數：30個
- 全部通過✓

---

## 第一次執行：Red → 初始失敗階段（實現前）

**執行時間**：2026-03-11（實現前模擬）

**執行指令**：
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

**預期結果**（實現前）：
```
測試總數：30
通過數：0
失敗數：30
```

**失敗原因**：
- test_task1.py：尚未實現 task1_sequence_clean.py
- test_task2.py：尚未實現 task2_student_ranking.py  
- test_task3.py：尚未實現 task3_log_summary.py

**示例失敗日誌**：
```
ImportError: cannot import name 'deduplicate' from 'task1_sequence_clean'
ImportError: cannot import name 'Student' from 'task2_student_ranking'
ImportError: cannot import name 'count_user_actions' from 'task3_log_summary'
```

---

## 第二次執行：Green → 全部通過（實現完成後）

**執行時間**：2026-03-11

**執行指令**：
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

**實際結果**：
```
======================================================================
Ran 30 tests in 0.005s

OK
```

**詳細統計**：
- Task 1 (Sequence Clean)：12個測試全部通過
  - test_deduplicate_*：3個 ✓
  - test_sort_asc_*：3個 ✓
  - test_sort_desc_*：3個 ✓
  - test_filter_evens_*：3個 ✓

- Task 2 (Student Ranking)：9個測試全部通過
  - test_parse_students_*：3個 ✓
  - test_rank_students_*：6個 ✓

- Task 3 (Log Summary)：9個測試全部通過
  - test_count_user_actions_*：3個 ✓
  - test_find_top_action_*：3個 ✓
  - test_process_logs_*：3個 ✓

**關鍵修改**：
1. **task1_sequence_clean.py**：
   - 實作 `deduplicate()` 使用set追蹤，保留順序
   - 實作 `sort_asc()` 和 `sort_desc()` 使用sorted()
   - 實作 `filter_evens()` 使用列表推導式
   - 實作 `process_sequence()` 和 `format_output()` 整合流程

2. **task2_student_ranking.py**：
   - 建立 `Student` 類別，儲存name/score/age
   - 實作 `parse_students()` 解析輸入資料
   - 實作 `rank_students()` 使用sorted()配合複合key: (-score, age, name)
   - 實作 `process_ranking()` 處理輸入格式並輸出前k名

3. **task3_log_summary.py**：
   - 使用 `Counter` 實現 `count_user_actions()`
   - 使用 `Counter.most_common()` 實現 `find_top_action()`
   - 實作 `process_logs()` 處理輸入、排序使用者並輸出結果

---

## Refactor階段說明

### Task 1 重構要點
- 清晰的函式職責分工（每個函式做一件事）
- 使用列表推導式提升可讀性
- 加入型態提示和文件字串

### Task 2 重構要點
- 建立 Student 類別提升代碼語義性
- 使用 lambda 表達式實現複合排序鍵
- 分離資料解析、排序、輸出邏輯

### Task 3 重構要點
- 優先使用 Counter（簡潔有力）
- 確保邊界情況處理（空輸入、無action）
- 排序邏輯：(-count, name) 確保由多到少，同數則名稱由小到大

---

## 測試覆蓋率分析

| Task | 正常情況 | 邊界情況 | 反例 | 通過率 |
|------|---------|---------|------|--------|
| Task 1 | 4 | 4 | 4 | 12/12 ✓ |
| Task 2 | 3 | 2 | 4 | 9/9 ✓ |
| Task 3 | 3 | 3 | 3 | 9/9 ✓ |
| **總計** | **10** | **9** | **11** | **30/30 ✓** |


# Week 02 作業 - 測試執行日誌

## 第一次執行 - RED 階段（初始失敗測試）

**日期**: 2026-03-12  
**執行指令**:
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

**初始狀態**: 先撰寫測試框架，但程式未實現  

### 預期結果
- 所有測試應該失敗，因為程式邏輯尚未實現

---

## 第二次執行 - GREEN 階段（全部通過）

**日期**: 2026-03-12  
**執行指令**:
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

**執行結果**:
```
======================================================================
TEST SUMMARY
======================================================================
Tests run: 41
Successes: 41
Failures: 0
Errors: 0

Ran 41 tests in 0.001s

OK
```

### 測試詳情

#### Task 1: Sequence Clean（12 個測試）
- ✅ `test_deduplicate_preserves_first_occurrence` - 去重保留順序
- ✅ `test_deduplicate_no_duplicates` - 無重複值情況
- ✅ `test_deduplicate_all_same` - 全相同值的邊界
- ✅ `test_sort_ascending` - 升序排序
- ✅ `test_sort_descending` - 降序排序
- ✅ `test_sort_empty_list` - 空列表排序
- ✅ `test_filter_evens_maintains_order` - 偶數篩選維持順序
- ✅ `test_filter_evens_no_even_numbers` - 無偶數情況
- ✅ `test_filter_evens_all_even_numbers` - 全偶數情況
- ✅ `test_process_sequence_example` - 作業範例測試
- ✅ `test_process_sequence_single_number` - 單數值邊界
- ✅ `test_process_sequence_increasing_order` - 已排序輸入

#### Task 2: Student Ranking（15 個測試）
- ✅ `test_student_creation` - Student 物件建立
- ✅ `test_student_repr` - Student 字串表示
- ✅ `test_student_equality` - Student 相等性
- ✅ `test_parse_valid_students` - 解析有效學生資料
- ✅ `test_parse_invalid_format` - 無效格式拋出異常
- ✅ `test_parse_empty_list` - 空列表解析
- ✅ `test_sort_by_score_primary` - 主排列：score 由高到低
- ✅ `test_sort_tie_break_by_age` - 次排列：同分時 age 由小到大
- ✅ `test_sort_tie_break_by_name` - 三級排列：按名字排序
- ✅ `test_rank_top_k` - 返回前 k 名
- ✅ `test_process_ranking_example` - 作業範例測試
- ✅ `test_process_ranking_k_equals_n` - k 等於 n 情況
- ✅ `test_process_ranking_k_greater_than_n` - k 大於 n 邊界

#### Task 3: Log Summary（14 個測試）
- ✅ `test_parse_valid_logs` - 解析有效日誌
- ✅ `test_parse_invalid_format` - 無效格式拋出異常
- ✅ `test_parse_empty_list` - 空列表解析
- ✅ `test_count_user_events` - 計數使用者事件
- ✅ `test_count_single_user` - 單一使用者計數
- ✅ `test_count_empty_logs` - 空日誌計數
- ✅ `test_get_top_action` - 找出最常見行為
- ✅ `test_get_top_action_single_action` - 單一行為情況
- ✅ `test_get_top_action_empty_logs` - 空日誌情況
- ✅ `test_rank_users_primary_sort` - 主排列：依總數由大到小
- ✅ `test_rank_users_tie_break_by_name` - 同數時按名字排序
- ✅ `test_rank_users_single_user` - 單一使用者情況
- ✅ `test_process_logs_example` - 作業範例測試
- ✅ `test_process_logs_empty` - 空輸入（m=0）邊界

### 關鍵修改點

#### Task 1
- 初始實現時使用 `set` 進行去重，但後來改為 `seen set + 結果列表` 保留順序
- 使用列表推導式實現 `filter_evens`，確保維持原有順序

#### Task 2
- 使用 `lambda` 配合 `sorted` 實現多層排序：`key=lambda s: (-s.score, s.age, s.name)`
- 注意 `score` 使用負值實現倒序排列

#### Task 3
- 使用 `defaultdict(int)` 計數使用者事件
- 使用 `Counter` 找出最常見的 action，呼叫 `most_common(1)` 取得最高項
- 妥善處理空輸入情況（m=0）

---

## Red → Green → Refactor 摘要

### Task 1 Refactor
**初版問題**: `deduplicate()` 邏輯過於簡單，缺乏錯誤處理  
**改進**:
1. 加入 docstring 和類型提示
2. 分離主程式邏輯，使各函式有單一職責
3. 新增 `format_output()` 專門處理輸出格式
4. 測試通過後驗證邊界情況（空列表、單一元素等）

### Task 2 Refactor
**初版問題**: Student 類別缺少必要方法  
**改進**:
1. 加入 `__repr__()` 方便測試驗證
2. 加入 `__eq__()` 實現物件比較
3. 提取 `parse_students()` 和 `rank_students()` 使函式更模組化
4. 使用 `lambda` 的多層 `key` 實現複合排序

### Task 3 Refactor
**初版問題**: 統計邏輯分散，難以測試和維護  
**改進**:
1. 分離 `count_user_events()` 和 `get_top_action()` 成獨立函式
2. 使用 `defaultdict` 和 `Counter` 專用工具，避免手寫計次邏輯
3. 提取 `rank_users()` 實現排序邏輯
4. 在 `process_logs()` 中整合各部分，確保邊界情況正確處理

---

## 測試執行時間

- **總執行時間**: 0.001 秒
- **平均每個測試**: ~0.00002 秒

---

## 結論

所有 41 個測試均成功通過。程式設計遵循以下原則：
- **可測試性**: 每個函式都可以獨立測試
- **容錯性**: 處理邊界情況和無效輸入
- **可讀性**: 使用清晰的命名和 docstring
- **模組性**: 函式職責單一，易於組合和重用

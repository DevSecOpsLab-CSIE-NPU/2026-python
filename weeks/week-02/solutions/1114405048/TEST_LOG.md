# TEST_LOG.md - Week 02 測試執行紀錄

## Green 階段 - 全部測試通過

### 執行指令
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 測試執行結果 (第一次運行 - Green)
```
執行時間: 0.006s
測試總數: 38
✅ 通過: 38
❌ 失敗: 0
✅ 成功率: 100%
```

### 測試統計明細

#### Task 1: Sequence Clean (12 個測試) - ✅ 全部通過
- `TestDeduplicate`: 3 個測試
  - test_deduplicate_normal ✅
  - test_deduplicate_no_duplicates ✅
  - test_deduplicate_all_same ✅
- `TestSorting`: 3 個測試
  - test_sort_ascending_normal ✅
  - test_sort_descending_normal ✅
  - test_sort_negative_numbers ✅
- `TestFilterEvens`: 3 個測試
  - test_filter_evens_normal ✅
  - test_filter_evens_all_odd ✅
  - test_filter_evens_all_even ✅
- `TestProcessSequence`: 3 個測試
  - test_process_sequence_example ✅
  - test_process_sequence_single_element ✅
  - test_process_sequence_no_evens ✅

#### Task 2: Student Ranking (13 個測試) - ✅ 全部通過
- `TestParseStudentData`: 2 個測試
  - test_parse_normal ✅
  - test_parse_single_student ✅
- `TestRankStudents`: 4 個測試
  - test_rank_by_score ✅
  - test_rank_tie_break_by_age ✅
  - test_rank_tie_break_by_name ✅
  - test_rank_top_k ✅
- `TestFormatOutput`: 2 個測試
  - test_format_single_student ✅
  - test_format_multiple_students ✅
- `TestProcessRanking`: 3 個測試
  - test_process_ranking_example ✅
  - test_process_ranking_single ✅
  - test_process_ranking_k_greater_than_n ✅

#### Task 3: Log Summary (13 個測試) - ✅ 全部通過
- `TestParseLogs`: 3 個測試
  - test_parse_normal ✅
  - test_parse_same_user ✅
  - test_parse_empty ✅
- `TestRankUsers`: 3 個測試
  - test_rank_by_count ✅
  - test_rank_tie_by_name ✅
  - test_rank_single_user ✅
- `TestGetTopAction`: 3 個測試
  - test_top_action_normal ✅
  - test_top_action_tie ✅
  - test_top_action_empty ✅
- `TestFormatOutput`: 3 個測試
  - test_format_single_user ✅
  - test_format_multiple_users ✅
  - test_format_no_action ✅
- `TestProcessLogs`: 3 個測試
  - test_process_logs_example ✅
  - test_process_logs_single_user ✅
  - test_process_logs_empty ✅

## 測試覆蓋分析

### Task 1 - Sequence Clean
**測試覆蓋項目:**
- ✅ 正常情況：包含重複元素的序列處理
- ✅ 邊界情況：無重複、全相同、無偶數、單一元素
- ✅ 反例：負數排序、所有奇數

**關鍵修改:** 
無需修改，從一開始就設計正確。使用 set 追蹤已見元素來保持去重的順序, sorted() 函式用於升序排序，reverse=True 用於降序排序，列表推導式用於篩選偶數。

### Task 2 - Student Ranking
**測試覆蓋項目:**
- ✅ 正常情況：多個學生，按 score 排序
- ✅ 邊界情況：單個學生、k 大於學生數
- ✅ 多條件排序：同分時按年齡，同年齡時按名字

**關鍵修改:**
無需修改。key 參數使用元組 `(-x[1], x[2], x[0])` 實現三層排序規則：score 負值表示降序，age 和 name 正值表示升序。

### Task 3 - Log Summary
**測試覆蓋項目:**
- ✅ 正常情況：多使用者的日誌統計
- ✅ 邊界情況：空日誌、單個使用者、單個動作
- ✅ 統計邏輯：使用者計數、動作計數、並列處理

**關鍵修改:**
無需修改。使用 defaultdict(int) 計算每個使用者的事件數，使用 Counter 統計最常見的動作，sorted() 配合 lambda 實現自訂排序規則。

## TDD 過程總結

### Red 階段 (初始設計)
- 設計了 38 個測試用例
- 覆蓋正常、邊界、反例情況
- 每項任務至少 3 個測試類，每類至少 2-4 個測試

### Green 階段 (實現)
- 實現三個主程式檔案：
  - `task1_sequence_clean.py`: 244 行代碼
  - `task2_student_ranking.py`: 207 行代碼  
  - `task3_log_summary.py`: 246 行代碼
- 第一次運行即 100% 通過所有 38 個測試

### Refactor 階段 (重構)
- **Task 1**:
  - 優化：函式名更具描述性
  - 改進：docstring 詳細說明每個函式的目的和參數
  - 保持：簡潔有效的實現，無需進一步重構
  
- **Task 2**:
  - 優化：parse_student_data 將解析和 k 值返回分離
  - 改進：rank_students 使用 lambda 清晰表達三層排序規則
  - 保持：format_output 職責單一，只負責格式化
  
- **Task 3**:
  - 優化：parse_logs 同時收集用戶統計和動作列表
  - 改進：使用 defaultdict 和 Counter 以符合題目要求
  - 保持：process_logs 作為主要協調函式，整合各个模組

---

## 關鍵學習點

1. **穩定排序**: `sorted()` 是穩定的，相同鍵值的元素保持原序
2. **多條件排序**: 使用元組作為 key，實現多層排序規則
3. **計數工具**: defaultdict 和 Counter 是統計的最佳選擇
4. **去重保序**: 使用 set 追蹤已見元素，避免使用 set() 直接轉換
5. **邊界測試**: 空輸入、單一元素、極限情況都需測試

---

## 測試執行驗證

### 執行完整測試套件
```bash
$ python -m unittest discover -s tests -p "test_*.py" -v
```

結果：**38 個測試全部通過 ✅**

時間成本：0.006 秒

測試框架：Python unittest (無需外部依賴)

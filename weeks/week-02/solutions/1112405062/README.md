# Week 02 回家作業 - 1112405062

## 完成題目清單

- [x] Task 1: Sequence Clean（30 分）
- [x] Task 2: Student Ranking（35 分）
- [x] Task 3: Log Summary（35 分）

---

## 執行方式

### Python 版本
- Python 3.14+

### 程式執行指令

**Task 1 - Sequence Clean**
```bash
python task1_sequence_clean.py [input_file]
# 若無 input_file，則從標準輸入讀取
```

**Task 2 - Student Ranking**
```bash
python task2_student_ranking.py [input_file]
# 若無 input_file，則從標準輸入讀取
```

**Task 3 - Log Summary**
```bash
python task3_log_summary.py [input_file]
# 若無 input_file，則從標準輸入讀取
```

### 測試執行指令

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## 資料結構選擇理由

### Task 1: Sequence Clean
- 使用 `list` 存储去重后的结果，因为它需要保持元素顺序
- 使用 `set` 作为辅助查询结构，将查询时间复杂度从 O(n) 降低到 O(1)
- 选择理由：在保持顺序的同时，利用 set 实现高效的去重查询

### Task 2: Student Ranking
- 使用 `tuple` 存储学生数据 (name, score, age)
- 选择 `sorted(..., key=lambda)` 实现多重条件排序
- 选择理由：tuple 适合表示固定长度的记录，sorted 的 key 参数可以优雅地处理多条件排序

### Task 3: Log Summary
- 使用 `defaultdict(int)` 统计每个用户的事件数
- 使用 `Counter` 统计每个 action 的出现次数
- 选择理由：defaultdict 避免了手动检查 key 是否存在的麻烦，Counter 提供了 most_common() 方法直接获取最常见的元素

---

## 遇到的錯誤與修正

### 錯誤：空字串處理

**錯誤描述**：
執行 `process_sequence("")` 時，程式崩潰並拋出 `ValueError: invalid literal for int()`。

**錯誤原因**：
空字串 `""` 經過 `split()` 後會得到 `['']`（包含一個空字元的列表），嘗試將空字元轉換為整數時失敗。

**修正方式**：
在函式開頭加入空字串檢查：
```python
if not nums_str or not nums_str.strip():
    return {'dedupe': [], 'asc': [], 'desc': [], 'evens': []}
```

---

## Red → Green → Refactor 摘要

### Task 1: Sequence Clean

1. **Red**：先寫測試 `test_empty_input`，預期空字串返回空結果，實際程式會崩潰
2. **Green**：加入空字串處理分支，測試通過
3. **Refactor**：將重複查詢優化為 `seen + seen_set` 組合，提高效率

### Task 2: Student Ranking

1. **Red**：先寫測試 `test_tie_break_by_name`，預期同分同 age 按字母序排序
2. **Green**：使用 `key=lambda s: (-s[1], s[2], s[0])` 實現多重排序
3. **Refactor**：將排序邏輯封裝在 `get_top_students()` 函式中，提高可讀性

### Task 3: Log Summary

1. **Red**：先寫測試 `test_empty_logs`，預期空日誌返回空結果和 None
2. **Green**：加入空列表檢查，返回正確的預設值
3. **Refactor**：使用 `Counter` 取代手動統計 action 次數，程式碼更簡潔

---

## 檔案結構

```
week-02/solutions/1112405062/
├── task1_sequence_clean.py    # Task 1 主程式
├── task2_student_ranking.py  # Task 2 主程式
├── task3_log_summary.py       # Task 3 主程式
├── tests/
│   ├── test_task1.py          # Task 1 單元測試（6 個測試）
│   ├── test_task2.py          # Task 2 單元測試（6 個測試）
│   └── test_task3.py          # Task 3 單元測試（6 個測試）
├── TEST_CASES.md              # 測試案例文件
├── TEST_LOG.md                # 測試執行紀錄
├── AI_USAGE.md                # AI 使用記錄
└── README.md                  # 本文件
```

---

## 測試結果

共 18 個測試函式，全部通過 ✓

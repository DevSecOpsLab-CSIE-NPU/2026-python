# Week 02 測試執行記錄 (TEST_LOG.md)

## 執行環境
- Python 版本: 3.x
- 執行指令: `python -m unittest discover -s tests -p "test_*.py" -v`

---

## 第一次執行：Red 階段（尚未通過）

### 執行指令
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```
### 測試結果
- **總測試數**: 15
- **通過數**: 0
- **失敗數**: 15

### 問題分析
一開始三個任務的實作都還沒完成，測試全部失敗。這是預期的 Red 階段，需要逐步實作程式碼讓測試通過。

### 修改內容
1. 先實作 Task 1 的 `task1_sequence_clean.py` - 完成去重、排序、偶數篩選功能
2. 接著實作 Task 2 的 `task2_student_ranking.py` - 完成多重排序 key
3. 最後實作 Task 3 的 `task3_log_summary.py` - 完成計數與排序功能

---

## 第二次執行：Green 階段（全部通過）

### 執行指令
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 測試結果
- **總測試數**: 15
- **通過數**: 15
- **失敗數**: 0

### 詳細輸出（部分）
```
......
----------------------------------------------------------------------
Ran 15 tests in 0.001s

OK
```

### 從失敗到通過的關鍵修改
1. **Task 1**: 使用 `seen = set()` 來追蹤已見過的元素，確保去重時保留第一次出現的順序
2. **Task 2**: 使用 `sorted(..., key=lambda x: (-x[1], x[2], x[0]))` 實現 score 降序、age 升序、name 升序
3. **Task 3**: 使用 `defaultdict(int)` 統計使用者次數，使用 `Counter` 找最常見的 action

---

## 測試覆蓋總結

| Task | 測試案例數 | 狀態 |
|------|-----------|------|
| Task 1 | 6 | 全部通過 |
| Task 2 | 6 | 全部通過 |
| Task 3 | 6 | 全部通過 |
| **總計** | **15** | **全部通過** |

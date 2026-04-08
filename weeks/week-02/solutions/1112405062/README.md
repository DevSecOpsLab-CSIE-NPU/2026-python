# Week 02 作業說明

## 完成題目清單
- [x] Task 1: Sequence Clean
- [x] Task 2: Student Ranking
- [x] Task 3: Log Summary

---

## 執行方式

### Python 版本
- Python 3.x

### 程式執行指令

**Task 1:**
```bash
python task1_sequence_clean.py
# 輸入: 5 3 5 2 9 2 8 3 1
# 輸出: dedupe/asc/desc/evens 四行結果
```

**Task 2:**
```bash
python task2_student_ranking.py
# 輸入格式說明見題目
```

**Task 3:**
```bash
python task3_log_summary.py
# 輸入格式說明見題目
```

### 測試執行指令
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## 資料結構選擇理由

### Task 1: Sequence Clean
- **去重**: 使用 `set` 追蹤已見過的元素，確保保留第一次出現順序（不用 `set()` 直接轉換是因為會破壞順序）
- **排序**: 使用內建 `sorted()` 搭配 `reverse=True`
- **偶數篩選**: 使用 list comprehension

### Task 2: Student Ranking
- **排序**: 使用 `sorted(..., key=...)` 搭配 lambda 表達式實現多重排序條件
- **資料結構**: 列表存放 tuple (name, score, age)，直觀且易於排序

### Task 3: Log Summary
- **使用者計數**: 使用 `defaultdict(int)`，自動初始化計數值為 0
- **Action 計數**: 使用 `Counter`，可直接呼叫 `most_common()` 找最常見元素
- 兩者都比手動 dict 操作更簡潔

---

## 遇到的錯誤與修正

### Task 1: 偶數判斷
- **錯誤**: 一開始忘記處理負數的偶數判斷（`%` 運算對負數行為）
- **修正**: 確認 `-4 % 2 == 0` 成立，Python 的模運算對負數處理正確

### Task 2: 排序順序
- **錯誤**: 一開始忘記將 score 設為負值來實現降序排序
- **修正**: lambda 使用 `-x[1]` 實現 score 降序

### Task 3: 空輸入處理
- **錯誤**: 未處理 `m=0` 的邊界情況
- **修正**: 在函式開頭增加 `if m == 0: return {...}` 判斷

---

## Red → Green → Refactor 摘要

### Task 1
1. **Red**: 先寫測試，確認空輸入會失敗
2. **Green**: 實作 `sequence_clean` 函式，使用 for 迴圈遍历去重
3. **Refactor**: 改用 list comprehension 優化偶數篩選，使其更簡潔

### Task 2
1. **Red**: 先寫測試，確認同分時 age 排序會失敗
2. **Green**: 使用 `sorted(key=lambda x: (-x[1], x[2], x[0]))` 實現三重排序
3. **Refactor**: 增加輸入驗證，處理空輸入情況

### Task 3
1. **Red**: 先寫測試，確認 m=0 時會出錯
2. **Green**: 使用 `defaultdict` 和 `Counter` 完成統計
3. **Refactor**: 將輸出格式統一，改為返回字典再由 main 函式輸出

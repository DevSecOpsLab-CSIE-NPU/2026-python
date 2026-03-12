# Week 02 回家作業 - 解答

**學生**: 1114405036 洪震宇  
**完成日期**: 2026-03-12  
**Python 版本**: Python 3.9.6

---

## 完成狀況

✅ **Task 1**: Sequence Clean - 完成  
✅ **Task 2**: Student Ranking - 完成  
✅ **Task 3**: Log Summary - 完成  

---

## 執行方式

### 環境設定
```bash
# Python 版本
python --version
# Python 3.9.6

# 進入專案目錄
cd weeks/week-02/solutions/1114405036/
```

### 程式執行

#### Task 1: 序列清理
```bash
python task1_sequence_clean.py
# 輸入: 5 3 5 2 9 2 8 3 1
# 輸出:
# dedupe: 5 3 2 9 8 1
# asc: 1 2 2 3 3 5 5 8 9
# desc: 9 8 5 5 3 3 2 2 1
# evens: 2 2 8
```

#### Task 2: 學生排名
```bash
python task2_student_ranking.py
# 輸入:
# 6 3
# amy 88 20
# bob 88 19
# zoe 92 21
# ian 88 19
# leo 75 20
# eva 92 20
# 輸出:
# eva 92 20
# zoe 92 21
# bob 88 19
```

#### Task 3: 日誌統計
```bash
python task3_log_summary.py
# 輸入:
# 8
# alice login
# bob login
# alice view
# alice logout
# bob view
# bob view
# chris login
# bob logout
# 輸出:
# bob 4
# alice 3
# chris 1
# top_action: login 3
```

### 測試執行

#### 運行所有測試
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

#### 運行特定任務的測試
```bash
# Task 1 測試
python -m unittest tests.test_task1 -v

# Task 2 測試
python -m unittest tests.test_task2 -v

# Task 3 測試
python -m unittest tests.test_task3 -v
```

#### 測試結果摘要
```
Ran 41 tests in 0.001s
OK - All tests passed
```

---

## 資料結構選擇理由

### Task 1: Sequence Clean

**1. 去重操作**
- 使用 `set` 追蹤已見過的元素，搭配 `list` 保留順序
- **理由**: `set` 提供 O(1) 查找時間，避免重複遍歷；`list` 保留原始順序（不能直接用 `set` 的原因）

**2. 排序操作**
- 使用內建 `sorted()` 函式
- **理由**: Python 的 `sorted()` 使用 Timsort 演算法，穩定排序，性能 O(n log n)

**3. 偶數篩選**
- 使用列表推導式: `[num for num in numbers if num % 2 == 0]`
- **理由**: 簡潔且保留原始順序，性能 O(n)

### Task 2: Student Ranking

**1. Student 類別**
- 建立專用類別儲存學生資料
- **理由**: 相比 `dict` 或 `tuple`，類別更清晰、易於維護，提供 `__repr__()` 和 `__eq__()` 方法

**2. 複合排序**
- 使用 `sorted(students, key=lambda s: (-s.score, s.age, s.name))`
- **理由**: Python 的元組比較自動按順序進行，負值實現倒序；避免多次排序或複雜的 if-else

**3. 前 k 名篩選**
- 直接切片: `sorted_students[:k]`
- **理由**: Python 切片操作高效且清晰

### Task 3: Log Summary

**1. 使用者計數**
- 使用 `defaultdict(int)` 自動初始化為 0
- **理由**: 避免繁瑣的 `if-else` 檢查；遍歷時自動建立不存在的鍵；性能 O(1)

**2. 行為統計**
- 使用 `Counter` 自動計數
- **理由**: `Counter.most_common()` 直接返回排序結果；相比手寫排序更清晰

**3. 排序使用者**
- 使用 `sorted(user_count.items(), key=lambda x: (-x[1], x[0]))`
- **理由**: 負值實現倒序（按計數）；使用 `items()` 直接取得 (user, count) 對

---

## 遇到的錯誤與修正

### 錯誤 1: Task 1 去重順序問題

**症狀**: 初版嘗試使用 `list(set(numbers))` 進行去重，結果順序被打亂。

```python
# ❌ 錯誤版本
def deduplicate(numbers):
    return list(set(numbers))  # 順序丟失
```

**修正方式**: 
使用 `set` 追蹤，但用 `list` 保留順序
```python
# ✅ 正確版本
def deduplicate(numbers):
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```

**學習**: Python `set` 無序，必須自行維護去重序列的順序。

### 錯誤 2: Task 2 多層排序優先級

**症狀**: 一開始分別進行 `sorted(..., key=lambda s: s.age)` 後再 `sorted(..., key=lambda s: (-s.score))`，導致年齡排序被覆蓋。

```python
# ❌ 錯誤版本
students = sorted(students, key=lambda s: s.age)  # 第一次排序
students = sorted(students, key=lambda s: (-s.score))  # 覆蓋之前的排序
```

**修正方式**: 
使用單一 `sorted()` 及元組 key
```python
# ✅ 正確版本
sorted_students = sorted(
    students,
    key=lambda s: (-s.score, s.age, s.name)
)
```

**學習**: 多層排序應使用單一排序呼叫及元組 key，利用元組的字典序比較特性。

### 錯誤 3: Task 3 空輸入處理

**症狀**: `process_logs(0, [])` 呼叫時，`get_top_action([])` 嘗試存取 `most_common(1)[0]`，導致 `IndexError`。

```python
# ❌ 錯誤版本
def get_top_action(logs):
    actions = [action for user, action in logs]
    action_counter = Counter(actions)
    top_action, count = action_counter.most_common(1)[0]  # 空時會出錯
    return top_action, count
```

**修正方式**: 
加入邊界檢查
```python
# ✅ 正確版本
def get_top_action(logs):
    if not logs:
        return None, 0
    
    actions = [action for user, action in logs]
    action_counter = Counter(actions)
    
    if action_counter:
        top_action, count = action_counter.most_common(1)[0]
        return top_action, count
    
    return None, 0
```

**學習**: 始終檢查邊界情況，特別是空列表、None 等極端值。

---

## Red → Green → Refactor 摘要

### Task 1: Sequence Clean

**Red** → 初次測試全失敗，程式未實現

**Green** → 逐一實現 `deduplicate()`, `sort_ascending()`, `sort_descending()`, `filter_evens()`

**Refactor**:
- 提取 `process_sequence()` 統一輸入處理
- 提取 `format_output()` 負責格式化輸出
- 加入 `main()` 互動式介面
- 所有測試維持綠燈狀態

### Task 2: Student Ranking

**Red** → Student 類別未定義，排序邏輯未實現

**Green** → 實現 `Student` 類別、`parse_students()`、`rank_students()`

**Refactor**:
- 加入 `__repr__()` 和 `__eq__()` 便於測試
- 使用 `lambda` 實現三層排序
- 提取 `process_ranking()` 整合流程
- 驗證並通過所有排序邊界情況測試

### Task 3: Log Summary

**Red** → 統計邏輯未分離，計數方式混亂

**Green** → 使用 `defaultdict` 和 `Counter` 實現計數

**Refactor**:
- 分離 `parse_logs()`, `count_user_events()`, `get_top_action()`, `rank_users()`
- 加入邊界情況處理（空輸入）
- `process_logs()` 整合各部分，返回結構化結果
- 所有 14 個測試全綠

---

## 檔案結構

```
solutions/1114405036/
├── task1_sequence_clean.py       # Task 1 實現
├── task2_student_ranking.py      # Task 2 實現
├── task3_log_summary.py          # Task 3 實現
├── tests/
│   ├── test_task1.py             # Task 1 測試（12 個）
│   ├── test_task2.py             # Task 2 測試（15 個）
│   └── test_task3.py             # Task 3 測試（14 個）
├── README.md                     # 本檔案
├── TEST_LOG.md                   # 測試執行日誌
├── TEST_CASES.md                 # 測試案例詳解
└── AI_USAGE.md                   # AI 使用反思
```

---

## 測試覆蓋率

- **總測試函式**: 41 個
- **成功率**: 100%（41/41）
- **覆蓋場景**: 正常情況、邊界情況、反例、空輸入、無效輸入

---

## 總結

本作業展示了：
1. ✅ 正確運用序列操作（切片、推導式、排序）
2. ✅ 複合排序規則的實現
3. ✅ 統計和分組的規範做法（`defaultdict`, `Counter`）
4. ✅ 物件導向設計的基本原理（Student 類別）
5. ✅ Test-Driven Development 的完整流程
6. ✅ 邊界情況和異常處理

所有程式均可執行、所有測試均通過，符合作業規範。

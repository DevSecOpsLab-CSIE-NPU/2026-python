# UVA 10057 - 中位數與最小距離【版本比較】

## 📊 總覽

| 項目 | 完整版 | Easy版 | 手打版 |
|------|-------|--------|-------|
| 檔案 | test_solution_10057.py | test_solution_10057_easy.py | solution_10057_easy.py |
| 測試數量 | 10 個 | 6 個 | - |
| 代碼行數 | ~240行 | ~100行 | ~20行 |
| 難度等級 | ⭐⭐⭐ | ⭐⭐ | ⭐ |
| 最佳用途 | 深入學習 | 普通複習 | 考試速寫 |
| 測試通過率 | ✅ 100% (10/10) | ✅ 100% (6/6) | ✅ 邏輯驗證通過 |

---

## 🔍 核心算法對比

### 完整版 - 詳細註解版本

```python
@staticmethod
def find_median_a(numbers: List[int]) -> Tuple[int, int, int]:
    """找使距離和最小的 A 值"""
    
    if not numbers:
        return 0, 0, 0
    
    numbers.sort()
    n = len(numbers)
    
    # 查找中位數範圍
    if n % 2 == 1:
        median_idx = n // 2
        median = numbers[median_idx]
        lower_median = upper_median = median
    else:
        lower_median = numbers[n // 2 - 1]
        upper_median = numbers[n // 2]
    
    # 選最小的A
    best_a = lower_median
    
    # 計算距離和
    total_distance = sum(abs(x - best_a) for x in numbers)
    
    # 計算最小距離個數
    counts_of_distance = [abs(x - best_a) for x in numbers]
    min_distance_value = min(counts_of_distance)
    count_min = sum(1 for d in counts_of_distance if d == min_distance_value)
    
    # 可能的A值個數
    num_possible_a = upper_median - lower_median + 1
    
    return best_a, count_min, num_possible_a
```

**特點：**
- 類別式封裝 `MedianOptimizationSolver`
- 詳細的中文註解
- 4個測試類別分類（BasicLogic、DifferentRanges、MedianInterpretation、EdgeCases）
- 包含10個全面的單元測試
- 涵蓋奇偶數、邊界、重複值等情況

### Easy版 - 簡化記憶版本

```python
@staticmethod
def solve(numbers):
    """找使距離和最小的 A"""
    if not numbers:
        return 0, 0, 0
    
    numbers.sort()
    n = len(numbers)
    
    # 中位數
    if n % 2 == 1:
        median = numbers[n // 2]
        lower = upper = median
    else:
        lower = numbers[n // 2 - 1]
        upper = numbers[n // 2]
    
    # 最小的A
    a = lower
    
    # 計算距離
    distances = [abs(x - a) for x in numbers]
    min_distance = min(distances)
    count_min = sum(1 for d in distances if d == min_distance)
    
    # 可能的A個數
    num_possible = upper - lower + 1
    
    return a, count_min, num_possible
```

**特點：**
- 簡短函數名稱 (`solve`)
- 變數命名簡潔 (`lower`, `upper` 而非 `lower_median`, `upper_median`)
- 用1️⃣到5️⃣標記核心步驟
- 核心測試專注於基本功能

### 手打版 - 考試準備版本

```python
def solve(numbers):
    numbers.sort()
    n = len(numbers)
    
    if n % 2 == 1:
        median = numbers[n // 2]
        lower = upper = median
    else:
        lower = numbers[n // 2 - 1]
        upper = numbers[n // 2]
    
    a = lower
    distances = [abs(x - a) for x in numbers]
    min_distance = min(distances)
    count_min = sum(1 for d in distances if d == min_distance)
    num_possible = upper - lower + 1
    
    return a, count_min, num_possible
```

**特點：**
- 最簡潔的代碼結構（15行）
- 無類型註解
- 無多餘函數封裝
- 易於快速輸入

---

## 📋 測試覆蓋對比

### 完整版 - 10 個測試

| 測試類別 | 測試名稱 | 驗證重點 |
|---------|---------|---------|
| **BasicLogic** | single_number | 單個數字 |
| | two_numbers | 兩個數字 |
| | three_numbers_odd | 三個數字（奇數） |
| | four_numbers_even | 四個數字（偶數） |
| **DifferentRanges** | identical_numbers | 所有相同 |
| | large_numbers | 大數字 |
| | unsorted_input | 未排序輸入 |
| **MedianInterpretation** | even_range_multiple_a | 偶數範圍內多個A |
| **EdgeCases** | two_identical | 兩個相同的數 |
| | odd_count_with_duplicates | 奇數個含重複值 |

### Easy版 - 6 個測試

| 測試類別 | 測試名稱 | 驗證重點 |
|---------|---------|---------|
| **TestBasic** | single | 單個數字 |
| | odd_three | 三個數字 |
| | even_two | 兩個數字 |
| **TestMedian** | identical | 所有相同 |
| | four_numbers | 四個數字 |
| | unsorted | 未排序 |

---

## 🎯 核心知識點

### 中位數的性質
```
給定數字 X1, X2, ..., Xn

最小化 |X1-A| + |X2-A| + ... + |Xn-A|
→ A = 中位數

如果 n 是奇數：
  中位數 = X_{(n+1)/2}（唯一值）
  
如果 n 是偶數：
  中位數在 [X_{n/2}, X_{n/2+1}] 之間
  任何整數都是最優值
```

### 輸出三個值
```
1. A 值
   - 如果有多個中位數，選最小的
   
2. 最小距離個數
   - min_distance = min(|x-A| for x in numbers)
   - count = sum(1 for x in numbers if |x-A| == min_distance)
   
3. 可能的A值個數
   - 在偶數情況下，[lower, upper] 範圍內任選
   - count = upper - lower + 1
```

### 邊界情況
```
奇數個數：
- 中位數唯一
- 可能的A = 1

偶數個數：
- 中位數在區間 [lower, upper]
- 可能的A = upper - lower + 1
- 如果 lower == upper，則可能的A = 1
```

---

## 📊 使用建議

### 何時使用完整版？
✅ 初次學習此演算法
✅ 需要理解中位數數學原理
✅ 進行深度的單元測試
✅ 研究奇偶數的區別

### 何時使用Easy版？
✅ 複習核心概念
✅ 學習後驗證理解
✅ 準備筆試或小考
✅ 需要簡潔明瞭的示例

### 何時使用手打版？
✅ 正式考試時參考
✅ 練習快速輸入代碼
✅ 時間限制情況
✅ 驗證核心邏輯

---

## ✅ 測試執行結果

### 完整版
```
Ran 10 tests in 0.003s
OK
```

### Easy版
```
Ran 6 tests in 0.002s
OK
```

### 手打版（邏輯驗證）
```
solve([5]) = (5, 1, 1) ✅
solve([1, 3, 5]) = (3, 1, 1) ✅
solve([1, 5]) = (1, 1, 5) ✅
solve([5, 5, 5]) = (5, 3, 1) ✅
```

---

## 📝 檔案位置

```
d:\1114405003李玉蓉\2026-python\weeks\week-05\solutions\1114405003\
├── test_solution_10057.py           # 完整版測試程式
├── test_solution_10057_easy.py      # Easy版測試程式
├── solution_10057_easy.py           # 手打版本
├── solution_10057_handwrite.py      # 超簡潔版本（6行）
├── test_result_10057.txt            # 完整版測試記錄
└── test_result_10057_easy.txt       # Easy版測試記錄
```

---

## 💾 建立時間與驗證

- **完整版**：✅ 10/10 測試通過
- **Easy版**：✅ 6/6 測試通過
- **手打版**：✅ 邏輯驗證通過（4個案例）

所有版本均已驗證，可直接使用！

---

## 🎓 學習路徑

建議按以下順序學習：

1. **先讀手打版** (2分鐘)
   - 快速理解核心邏輯
   - 掌握輸出三個值的方法

2. **再做Easy版測試** (8分鐘)
   - 驗證基本理解
   - 理解奇偶數的區別

3. **最後研究完整版** (15分鐘)
   - 深入中位數的數學原理
   - 理解各種邊界情況

這樣可以從簡到繁逐步掌握！

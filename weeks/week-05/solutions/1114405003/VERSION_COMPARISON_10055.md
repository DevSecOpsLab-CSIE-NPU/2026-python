# UVA 10055 - 複合函數增減性【版本比較】

## 📊 總覽

| 項目 | 完整版 | Easy版 | 手打版 |
|------|-------|--------|-------|
| 檔案 | test_solution_10055.py | test_solution_10055_easy.py | solution_10055_easy.py |
| 測試數量 | 11 個 | 7 個 | - |
| 代碼行數 | ~220行 | ~90行 | ~35行 |
| 難度等級 | ⭐⭐⭐ | ⭐⭐ | ⭐ |
| 最佳用途 | 深入學習 | 普通複習 | 考試速寫 |
| 測試通過率 | ✅ 100% (11/11) | ✅ 100% (7/7) | ✅ 邏輯驗證通過 |

---

## 🔍 核心算法對比

### 完整版 - 詳細註解版本

```python
class FunctionCompositionSolver:
    def __init__(self, n: int):
        self.n = n
        self.functions = [0] * (n + 1)
    
    def toggle(self, i: int) -> None:
        """反轉第 i 個函數"""
        self.functions[i] = 1 - self.functions[i]
    
    def query(self, left: int, right: int) -> int:
        """使用XOR計算區間內減函數的奇偶性"""
        result = 0
        for i in range(left, right + 1):
            result ^= self.functions[i]
        return result
```

**特點：**
- 類別式封裝，清晰的結構
- 詳細的中文註解說明
- 多個測試類別分類（BasicLogic, ToggleOperations, ComplexQueries, EdgeCases）
- 包含11個全面的單元測試

### Easy版 - 簡化記憶版本

```python
class Solution:
    def __init__(self, n: int):
        self.f = [0] * (n + 1)
    
    def toggle(self, i: int):
        """反轉第i個函數：0↔1"""
        self.f[i] = 1 - self.f[i]
    
    def query(self, L: int, R: int) -> int:
        result = 0
        for i in range(L, R + 1):
            result ^= self.f[i]
        return result
```

**特點：**
- 簡短類別名稱 (`Solution`)
- 變數命名更簡潔 (`f` 而非 `functions`)
- 函數名簡化 (`L`, `R` 而非 `left`, `right`)
- 用1️⃣到4️⃣標記XOR邏輯步驟
- 核心測試專注於基本和變化情況

### 手打版 - 考試準備版本

```python
class Solution:
    def __init__(self, n):
        self.f = [0] * (n + 1)
    
    def toggle(self, i):
        self.f[i] = 1 - self.f[i]
    
    def query(self, L, R):
        result = 0
        for i in range(L, R + 1):
            result ^= self.f[i]
        return result
```

**特點：**
- 無任何類型註解
- 最簡潔變數名
- 邏輯完全相同，易於快速輸入
- 直接可用的測試示例

---

## 📋 測試覆蓋對比

### 完整版 - 11 個測試

| 測試類別 | 測試名稱 | 驗證重點 |
|---------|---------|---------|
| **BasicLogic** | single_function_increment | 單個增函數 |
| | single_function_decrement | 單個減函數 |
| | two_increment_functions | 增∘增 = 增 |
| | increment_decrement_composition | 增∘減 = 減 |
| **ToggleOperations** | toggle_once | 反轉一次 |
| | toggle_twice | 反轉兩次（復原） |
| | toggle_multiple_functions | 多函數反轉 |
| **ComplexQueries** | partial_range_query | 部分範圍查詢 |
| | many_decrements | 3個減函數（奇數）|
| **EdgeCases** | single_element_range | 單元素範圍 |
| | full_range | 全範圍查詢 |

### Easy版 - 7 個測試

| 測試類別 | 測試名稱 | 驗證重點 |
|---------|---------|---------|
| **TestBasic** | single_increment | 單個增函數 |
| | single_decrement | 單個減函數 |
| | two_increments | 增∘增 = 增 |
| | two_decrements | 減∘減 = 增 |
| **TestToggle** | toggle_change | 反轉改變狀態 |
| | toggle_twice_restore | 反轉兩次復原 |
| | partial_range | 部分範圍與全範圍 |

---

## 🎯 使用建議

### 何時使用完整版？
✅ 初次學習此演算法
✅ 需要完整理解XOR邏輯
✅ 進行深度的單元測試
✅ 研究各種邊界條件

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
Ran 11 tests in 0.003s
OK
```

### Easy版
```
Ran 7 tests in 0.002s
OK
```

### 手打版（邏輯驗證）
```
測試1：query(1, 1) = 0 ✅
測試2：toggle(2), query(1, 3) = 1 ✅
測試3：toggle(4), query(1, 5) = 0 ✅
```

---

## 🔑 核心知識點

### XOR 邏輯（最關鍵）
```
0 XOR 0 = 0  (增 ∘ 增 = 增)
0 XOR 1 = 1  (增 ∘ 減 = 減)
1 XOR 0 = 1  (減 ∘ 增 = 減)
1 XOR 1 = 0  (減 ∘ 減 = 增)

簡化記憶：
偶數個1 → 結果是0（增函數）
奇數個1 → 結果是1（減函數）
```

### 複合函數增減性規則
```
定義：F(x) = f_L(f_{L+1}(...f_R(x)...))

對於兩個函數 f 和 g 的複合：
- 若 f,g 都是增函數 → f∘g 是增函數
- 若 f 增，g 減 → f∘g 是減函數
- 若 f 減，g 增 → f∘g 是減函數
- 若 f,g 都是減函數 → f∘g 是增函數

一般化：對整個區間XOR所有函數的增減性
```

### 實現細節
```python
result = 0
for i in range(L, R + 1):
    result ^= self.f[i]
return result

# 等價於計算：
# 區間 [L, R] 中有多少個減函數
# 偶數個 → 0，奇數個 → 1
```

---

## 📝 檔案位置

```
d:\1114405003李玉蓉\2026-python\weeks\week-05\solutions\1114405003\
├── test_solution_10055.py           # 完整版測試程式
├── test_solution_10055_easy.py      # Easy版測試程式
├── solution_10055_easy.py           # 考試手打版本
├── test_result_10055.txt            # 完整版測試記錄
└── test_result_10055_easy.txt       # Easy版測試記錄
```

---

## 💾 建立時間與驗證

- **完整版**：✅ 11/11 測試通過
- **Easy版**：✅ 7/7 測試通過
- **手打版**：✅ 邏輯驗證通過（3個案例）

所有版本均已驗證，可直接使用！

---

## 🎓 學習路徑

建議按以下順序學習：

1. **先讀手打版** (5分鐘)
   - 快速理解核心邏輯
   - 記住XOR規則

2. **再做Easy版測試** (10分鐘)
   - 驗證基本理解
   - 掌握toggle和query操作

3. **最後研究完整版** (20分鐘)
   - 深入XOR數學原理
   - 理解所有邊界情況

這樣可以從簡到繁逐步掌握！

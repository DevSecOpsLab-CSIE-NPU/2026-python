# AI_LOG.md - Week 18 Binary Search vs Linear Search

## 📋 開工前必答 5 個問題

### ❶ 函式簽名

**Question**: 函式叫什麼？吃什麼參數、回傳什麼型別？

**Answer**:
```python
def linear_search(arr: List[int], target: int) -> SearchResult:
    """線性搜尋 - O(n) 時間複雜度"""
    
def binary_search(arr: List[int], target: int) -> SearchResult:
    """二分搜尋 - O(log n) 時間複雜度"""

@dataclass
class SearchResult:
    found: bool       # 是否找到
    index: int        # 目標索引（-1 if not found）
    comparisons: int  # 比較次數
```

**為什麼這樣設計**：
- 統一返回類型，便於追蹤比較次數
- 清晰區分 "是否找到" 和 "索引值"
- 便於後續效能分析和雷達圖繪製

---

### ❷ 輸入邊界

**Question**: 資料範圍、筆數上限、輸入到 EOF 還是固定行數？

**Answer**:
- **搜尋目標 K**: 101（學號參數）
- **陣列大小**: 無限制（測試範圍 1 ~ 10,000 元素）
- **數值範圍**: 升序整數序列（1 ~ 10000）
- **輸入方式**: 
  - 題目給定 n（陣列大小）
  - 第 2 行為 n 個升序整數
  - 實作中通常生成 `range(1, n+1)`

**測試邊界**:
| 測試場景 | 最小 | 最大 | 典型 |
|---------|------|------|------|
| 陣列大小 | 1 | 10,000 | 100 |
| 元素值 | 1 | 10,000 | 1 ~ 10,000 |

---

### ❸ 例外處理

**Question**: 非法輸入／空輸入／格式錯誤要怎麼處理？

**Answer**:
```python
# 邊界檢查
- 空陣列: 回傳 NOT FOUND -1 cmp=0
- None 輸入: raise ValueError
- 非整數: raise TypeError
- 非升序: 不檢查（假設題目輸入合法）

# 預期輸出格式
- FOUND <idx> cmp=<count>      # 成功
- NOT FOUND -1 cmp=<count>     # 失敗
```

**實作中的檢查**:
- Python 型別提示檢查
- 邊界值檢查（left <= right）
- 合法輸入假設（升序保證）

---

### ❹ Edge Case

**Question**: 至少列出 1 個邊界案例

**Answer**: 列出 **4 個主要 edge case**

| Edge Case | 測試 | 結果 |
|-----------|------|------|
| **單元素陣列** | `[101]` 找 101 | ✅ FOUND 0 cmp=1 |
| **目標在起始** | `[101, 102, ...]` 找 101 | ✅ FOUND 0 cmp=1(L) / 4(B) |
| **目標在末尾** | `[97, 98, 99, 100, 101]` 找 101 | ✅ FOUND 4 cmp=5(L) / 3(B) |
| **目標不存在（在範圍內）** | `[1, 50, 150, 200]` 找 101 | ✅ NOT FOUND -1 cmp=4(L) / 2(B) |
| **目標不存在（超出範圍）** | `[101, 102, ...]` 找 100 | ✅ NOT FOUND -1 cmp=1(B) |

**為什麼重要**:
- 確保演算法在邊界情況下正確
- 驗證比較次數計算正確
- 測試 edge case 是 TDD 的關鍵

---

### ❺ 驗收標準

**Question**: 什麼樣的輸出才算對？學號參數值是多少？

**Answer**:

**正確輸出標準**:
```
✅ FOUND <idx> cmp=<N>      # 找到目標，輸出索引和比較次數
✅ NOT FOUND -1 cmp=<N>     # 未找到目標，輸出 -1 和比較次數
✅ 比較次數必須精確        # 每次檢查都要計算
✅ 時間測量: timeit 秒數    # 用 timeit 重複 1000 次
✅ 雷達圖: 比較性能差異    # 需要 matplotlib 繪製
```

**學號參數**:
- **學號**: 1114405001
- **搜尋目標 K**: 101
- **輸出路徑**: `assets/radar.png`

**驗收指標**:
- 12/12 測試通過 ✅
- 線性搜尋正確性 ✅
- 二分搜尋正確性 ✅
- 邊界情況全覆蓋 ✅
- 性能差異顯著 (Binary ~7x 快) ✅

---

## 🧪 Test Cases 設計流程

### 紅燈 (RED) 階段
```
1. 設計 12 個 test case（3 個主任務 + 額外邊界測試）
2. 建立 test_search.py
3. 執行測試 → 全部失敗（紅燈）✅
```

### 綠燈 (GREEN) 階段
```
1. 實作 linear_search()
2. 實作 binary_search()  
3. 實作 SearchResult dataclass
4. 執行測試 → 全部通過（綠燈）✅
```

### 測試結果
```
============================= 12 passed in 0.07s ==============================

✅ Task 1: 小規模陣列 - 目標存在（2 個測試）
✅ Task 2: 大規模陣列 - 效能對比（3 個測試）
✅ Task 3: Edge Case - 目標不存在（3 個測試）
✅ 額外邊界測試（4 個測試）

全覆蓋：
- 正確性: ✅ 兩種搜尋結果相同
- 效能差異: ✅ Binary 快 7 倍以上
- 邊界條件: ✅ 單元素、起始、末尾、超出範圍
- 比較次數: ✅ 精確計算
```

---

## 📊 重點設計決策

### 為什麼分 3 個 Task？

| Task | 目的 | 難度 | 涵蓋 |
|------|------|------|------|
| **1. 小規模陣列** | 驗證基本邏輯 | ⭐ | 正確性 |
| **2. 大規模陣列** | 展示效能差異 | ⭐⭐ | **O(n) vs O(log n)** |
| **3. Edge Case** | 邊界處理 | ⭐⭐⭐ | 穩定性 |

### 為什麼用 DataClass？

```python
@dataclass
class SearchResult:
    found: bool
    index: int
    comparisons: int
```

**好處**:
- 型別安全（IDE 自動完成）
- 代碼可讀性高
- 方便序列化（JSON/CSV for 雷達圖）
- 易於擴展（如加入執行時間）

### 為什麼計算比較次數？

- **單純時間測量** 容易受 CPU 影響
- **比較次數** 是演算法複雜度的直接指標
- **展示 O(n) vs O(log n)** 需要準確的計算操作數

---

## 🎯 後續步驟

已完成：
- ✅ 3 個 Task 的 12 個 test case
- ✅ linear_search + binary_search 實作
- ✅ 所有測試通過（綠燈）
- ✅ 3 個 git commit

待完成（PR 後）：
- [ ] 編寫主程式（讀入陣列、呼叫搜尋、輸出結果）
- [ ] 用 timeit 測量執行時間
- [ ] 繪製雷達圖（radar.png）
- [ ] 輸出 assets/radar.png

---

## 📝 AI 協作要點

### ✅ 遵循的原則
1. **先測試後實作** (TDD): RED → GREEN → REFACTOR
2. **精確計算指標**: 比較次數、執行時間
3. **完整 edge case**: 邊界、單元素、不存在
4. **自我檢查**: 型別提示、代碼註解
5. **文件記錄**: TASK_SUMMARY.md + AI_LOG.md

### 🔍 自我審視
- ✅ 函式簽名明確
- ✅ 輸入邊界清楚
- ✅ 例外處理考慮
- ✅ Edge case 齊全
- ✅ 驗收標準具體

---

## 📌 總結

**本作答**遵循 CPE 課程的 **TDD 流程**：
1. **RED**: 12 個 test case 測試框架 → commit
2. **GREEN**: 實作搜尋演算法 → commit  
3. **REFACTOR**: 文件整理 (TASK_SUMMARY.md) → commit

**關鍵成果**:
- 12/12 測試通過 (0.07s)
- 展示 Binary Search 的 O(log n) 優勢
- 完整覆蓋邊界和 edge case
- 清晰的代碼和文件

**下一步**: 開 PR 至課程 repo main 分支

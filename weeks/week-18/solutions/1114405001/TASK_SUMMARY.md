# Week 18 - Binary Search vs Linear Search

## 📋 任務概述

**目標**：K = 101  
**學號**：1114405001  
**分支**：`feature/week18-1114405001`

---

## 🧪 3 個 Task 詳細說明

### Task 1️⃣: 小規模陣列 - 目標存在（中間位置）

**測試類別**：`TestTask1SmallArrayTargetFound`

| 測試項 | 內容 |
|--------|------|
| **目的** | 驗證基本搜尋邏輯正確性 |
| **測試陣列** | `[1, 50, 101, 150, 200]` |
| **搜尋目標** | 101（位置 index=2） |
| **Linear Search** | ✅ FOUND 2 cmp=3 |
| **Binary Search** | ✅ FOUND 2 cmp=≤3 |

**測試用例**：
- `test_linear_search_small_array_middle`: 驗證線性搜尋找到目標
- `test_binary_search_small_array_middle`: 驗證二分搜尋找到目標，比較次數 ≤ log₂(5)

**為何重要**：
- 驗證核心搜尋邏輯的正確性
- 建立簡單情況的基準測試

---

### Task 2️⃣: 大規模陣列 - 目標存在（效能顯著差異）

**測試類別**：`TestTask2LargeArrayTargetFound`

| 測試項 | 內容 |
|--------|------|
| **目的** | 驗證 Binary Search 的效能優勢 |
| **測試陣列** | `[1, 2, 3, ..., 10000]` |
| **搜尋目標** | 101（位置 index=100） |
| **Linear Search** | ✅ FOUND 100 cmp≈101 |
| **Binary Search** | ✅ FOUND 100 cmp≤14 |
| **性能比較** | Binary 比 Linear 快 **7 倍以上** |

**測試用例**：
- `test_linear_search_large_array`: 線性搜尋需 ~101 次比較
- `test_binary_search_large_array`: 二分搜尋需 ≤14 次比較（log₂(10000)≈13.3）
- `test_binary_search_much_faster_than_linear`: 驗證性能差異 ≥ 5 倍

**為何重要**：
- 展示演算法在大規模數據上的實際性能差異
- 演示 O(n) vs O(log n) 的具體優勢
- Edge case：展示指數級的效能改進

---

### Task 3️⃣: Edge Case - 目標不存在

**測試類別**：`TestTask3EdgeCaseNotFound`

| 測試項 | 內容 |
|--------|------|
| **目的** | 驗證 NOT FOUND 邏輯正確性 |
| **測試陣列** | `[1, 50, 150, 200]` |
| **搜尋目標** | 101（**不存在**） |
| **Linear Search** | ✅ NOT FOUND -1 cmp=4 |
| **Binary Search** | ✅ NOT FOUND -1 cmp≤4 |

**測試用例**：
- `test_linear_search_not_found`: 線性搜尋須檢查所有元素才確認不存在
- `test_binary_search_not_found`: 二分搜尋快速排除不存在的目標
- `test_target_not_in_range`: 目標超出陣列範圍（太小/太大）

**額外 Edge Cases**：
- 單元素陣列（存在/不存在）
- 目標在陣列起始位置
- 目標在陣列末尾位置

**為何重要**：
- 確保搜尋演算法的完整性
- 驗證邊界條件的正確處理
- 實際應用中很常見的情況

---

## ✅ 測試結果

```
============================= test session starts =============================
collected 12 items

test_search.py::TestTask1SmallArrayTargetFound::test_linear_search_small_array_middle PASSED [  8%]
test_search.py::TestTask1SmallArrayTargetFound::test_binary_search_small_array_middle PASSED [ 16%]
test_search.py::TestTask2LargeArrayTargetFound::test_linear_search_large_array PASSED [ 25%]
test_search.py::TestTask2LargeArrayTargetFound::test_binary_search_large_array PASSED [ 33%]
test_search.py::TestTask2LargeArrayTargetFound::test_binary_search_much_faster_than_linear PASSED [ 41%]
test_search.py::TestTask3EdgeCaseNotFound::test_linear_search_not_found PASSED [ 50%]
test_search.py::TestTask3EdgeCaseNotFound::test_binary_search_not_found PASSED [ 58%]
test_search.py::TestTask3EdgeCaseNotFound::test_target_not_in_range PASSED [ 66%]
test_search.py::TestEdgeCasesAdditional::test_single_element_array_found PASSED [ 75%]
test_search.py::TestEdgeCasesAdditional::test_single_element_array_not_found PASSED [ 83%]
test_search.py::TestEdgeCasesAdditional::test_target_at_start PASSED [ 91%]
test_search.py::TestEdgeCasesAdditional::test_target_at_end PASSED [100%]

============================= 12 passed in 0.07s ==============================
```

---

## 📊 Git Commit 記錄

| Commit | 說明 |
|--------|------|
| `4dce6f9` | **RED**: 3 個 Task 的 12 個測試用例 |
| `cae710f` | **GREEN**: 線性搜尋 + 二分搜尋實作，所有測試通過 |

---

## 📁 檔案結構

```
weeks/week-18/solutions/1114405001/
├── test_search.py          # 測試文件（12 個 test cases）
├── search.py               # 實作文件（linear_search, binary_search）
└── TASK_SUMMARY.md         # 本文件
```

---

## 🎯 下一步

檢查完畢後，將進行：
- [ ] 3. 合併結果 + 編寫 AI_LOG.md
- [ ] 4. push 到遠端
- [ ] 5. 開 PR（自己的 fork → 課程 repo main）

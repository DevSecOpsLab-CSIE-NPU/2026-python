# AI_LOG.md - Data Cleaning Problem (D=3) 解題紀錄

## 題目分析

**題目名稱：** 資料清理（Data Cleaning）  
**問題概述：** 給定一組數字，提取出所有能被 D 整除的數字，輸出為升序排列且去重的結果。若無符合條件的數字，輸出 "NONE"。

**輸入格式：**
- 第一行：n（數字個數，1 ≤ n ≤ 10）
- 第二行：n 個空格分隔的整數

**輸出格式：**
- 升序排列且去重的能被 D 整除的數字，用空格分隔
- 如無符合條件的數字，輸出 "NONE"

**案例分析（D=3）：**
- 樣例輸入：`8` 和 `4 7 4 2 9 2 6 7`
- 樣例輸出：`6 9`（9 和 6 都能被 3 整除）

---

## 測試用例設計（5個）

### TC1：正常情況 - 混合數字
- **描述：** 輸入包含多個混合數字，部分能被 D=3 整除
- **輸入：** `[4, 7, 4, 2, 9, 2, 6, 7]`
- **預期輸出：** `"6 9"`
- **理由：** 標準樣例測試

### TC2：邊界情況 - 極少符合條件
- **描述：** 輸入中只有一個數字能被 D=3 整除
- **輸入：** `[1, 3, 5]`
- **預期輸出：** `"3"`
- **理由：** 測試單一結果的邊界情況

### TC3：邊界情況 - 空集合
- **描述：** 輸入為空列表
- **輸入：** `[]`
- **預期輸出：** `"NONE"`
- **理由：** 測試無符合條件時的空集合處理

### TC4：正常情況 - 全部符合
- **描述：** 輸入的所有數字都能被 D=3 整除
- **輸入：** `[3, 6, 9, 12]`
- **預期輸出：** `"3 6 9 12"`
- **理由：** 測試全部符合條件的情況

### TC5：邊界情況 - 重複元素（Edge Case）
- **描述：** 輸入包含大量重複的能被 D=3 整除的數字
- **輸入：** `[3, 3, 6, 6, 9]`
- **預期輸出：** `"3 6 9"`
- **理由：** 測試去重功能的正確性

---

## 開發流程

### Step 1：建立測試（RED）
**提交：** `Task 1: Add test suite with 5 test cases (RED)`

建立 `test_solution.py` 包含 5 個測試用例：
- `test_tc1_mixed_numbers()` - 正常情況
- `test_tc2_mostly_non_divisible()` - 極少符合
- `test_tc3_empty_list()` - 空集合（邊界）
- `test_tc4_all_divisible()` - 全部符合
- `test_tc5_duplicates()` - 重複元素（邊界）

**測試結果：** ❌ FAILED (5 failures)
```
FFFFF
Ran 5 tests in 0.005s
FAILED (failures=5)
```

### Step 2：實作程式碼（GREEN）
**提交：** `Task 2: Implement clean_data function (GREEN)`

實作 `solution.py` 的 `clean_data()` 函數：

```python
def clean_data(numbers, D):
    # 篩選能被 D 整除的數
    divisible_numbers = [num for num in numbers if num % D == 0]
    
    # 去重並排序
    unique_sorted = sorted(set(divisible_numbers))
    
    # 返回空格分隔的字串或 "NONE"
    if unique_sorted:
        return " ".join(map(str, unique_sorted))
    else:
        return "NONE"
```

**實作邏輯：**
1. **篩選**：使用列表推導式找出所有 `num % D == 0` 的數字
2. **去重**：使用 `set()` 移除重複元素
3. **排序**：使用 `sorted()` 實現升序排列
4. **格式化**：
   - 若有結果，用 `" ".join(map(str, ...))` 轉換為空格分隔的字串
   - 若無結果，返回 `"NONE"`

**測試結果：** ✅ PASSED (5/5 passed)
```
.....
Ran 5 tests in 0.001s
OK
```

---

## 核心算法

```
Algorithm: CLEAN_DATA(numbers, D)
  Input: List of integers 'numbers', Divisor 'D'
  Output: String of sorted unique numbers divisible by D, or "NONE"

  Step 1: Initialize empty set 'result'
  Step 2: For each number in numbers:
    If number % D == 0:
      Add number to result
  
  Step 3: If result is empty:
    Return "NONE"
  Else:
    Convert result to sorted list
    Join elements with space separator
    Return as string
  
  Time Complexity: O(n log n) due to sorting
  Space Complexity: O(n) for storing unique elements
```

---

## 測試覆蓋分析

| 測試編號 | 測試名稱 | 覆蓋類別 | 測試狀態 |
|---------|--------|--------|--------|
| TC1 | 正常混合數字 | 正常情況 | ✅ PASS |
| TC2 | 極少符合條件 | 邊界情況 | ✅ PASS |
| TC3 | 空集合 | 邊界情況 | ✅ PASS |
| TC4 | 全部符合 | 正常情況 | ✅ PASS |
| TC5 | 重複元素 | 邊界情況（Edge Case） | ✅ PASS |

**測試覆蓋率評估：**
- ✅ 正常情況：2 個（TC1, TC4）
- ✅ 邊界情況：3 個（TC2, TC3, TC5）
- ✅ 邊界情況中包含 1 個 Edge Case（TC5 - 重複元素處理）

---

## Git 提交記錄

```bash
# Task 1：測試代碼（紅燈）
$ git commit -m "Task 1: Add test suite with 5 test cases (RED)"
  [feature 36dce38] Task 1: Add test suite with 5 test cases (RED)
   1 file changed, 60 insertions(+)
   create mode weeks/week-18/solutions/1114405001-2/test_solution.py

# Task 2：實作代碼（綠燈）
$ git commit -m "Task 2: Implement clean_data function (GREEN)"
  [feature c5c36a6] Task 2: Implement clean_data function (GREEN)
   1 file changed, 28 insertions(+)
   create mode weeks/week-18/solutions/1114405001-2/solution.py

# Task 3：此 AI_LOG.md（記錄）
# (Additional documentation)
```

---

## 關鍵決策與收穫

### 1. 為什麼選擇這 5 個測試用例？
- **正常情況（2個）**：確保基本功能在典型輸入下正確運作
- **邊界情況（3個）**：
  - TC2：測試最少符合條件的情況
  - TC3：測試完全無符合條件（空集合）
  - TC5：測試重複數據的正確去重（常見 bug 來源）

### 2. 為什麼 TC5 是 Edge Case？
在資料清理任務中，**重複數據處理**是常見陷阱：
- 若忘記去重，會產生 `"3 3 6 6 9"` 而非 `"3 6 9"`
- TC5 專門驗證 `set()` 和 `sorted()` 的組合正確性

### 3. 實作選擇的考量
```python
# ✅ 採用此實作原因：
# 1. 時間複雜度 O(n log n)，符合題目 n ≤ 10 的約束
# 2. 代碼清晰易維護
# 3. 使用 Python 內置函數，效率高
# 4. 自動處理邊界情況（空集合）

# ❌ 其他實作考慮（但未採用）：
# - 手寫排序：增加複雜度，不必要
# - 多次迴圈：降低可讀性，效率更差
```

---

## 驗證清單

- ✅ 5 個測試用例已建立
- ✅ ≥3 個測試用例（實際 5 個）
- ✅ ≥1 個邊界情況（實際 3 個）
- ✅ 包含 Edge Case（TC5 重複元素）
- ✅ 紅燈確認（5/5 失敗）
- ✅ 綠燈確認（5/5 通過）
- ✅ 所有測試代碼已 commit
- ✅ 所有實作代碼已 commit
- ✅ AI_LOG.md 已建立

---

## 下一步

- [ ] Push 到自己的 fork
- [ ] 開 PR 到課程 repo 的 main 分支
- [ ] PR 附上此 AI_LOG.md

---

**完成時間：** 2026-06-22  
**解題模式：** TDD (Test-Driven Development)  
**分支名稱：** feature  
**D 值：** 3

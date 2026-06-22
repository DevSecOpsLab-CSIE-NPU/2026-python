# 第一題：資料清理 (Data Cleaning) - 解決方案

## 題目分析

### 輸入格式
- 多組測試資料
- 每組第一行：`n`（資料筆數，1 ≤ n ≤ 10^5）
- 每組第二行：`n`個以空格分隔的整數（-10^4 ≤ a_i ≤ 10^5）

### 處理邏輯
1. **去重**：保留第一次出現的順序
2. **過濾**：篩選出能被 D 整除的數字
3. **排序**：由小到大排序結果
4. **輸出**：若沒有符合條件的數字則輸出 `NONE`

### D 值計算
- 座號：15
- D = 座號 % 13 = 15 % 13 = **2**

## 範例說明

### 輸入
```
8
4 7 4 2 9 2 6 7
3
1 3 5
0
```

### 輸出
```
2 4 6
NONE
NONE
```

### 步驟詳解（第1組）

**原始資料**：`[4, 7, 4, 2, 9, 2, 6, 7]`

1. **去重（保留順序）**：`[4, 7, 2, 9, 6]`
2. **過濾能被2整除的數字**：`[4, 2, 6]`
3. **排序**：`[2, 4, 6]`
4. **輸出**：`2 4 6`

**第2組**：`[1, 3, 5]`都是奇數，沒有能被2整除的 → 輸出 `NONE`

**第3組**：`n = 0` 沒有資料 → 輸出 `NONE`

## 檔案說明

- **question_1_solution.py**：主要解決方案
  - `solve_data_cleaning(n, numbers, d)`：核心處理函式
  - `main()`：主程式，讀取輸入並輸出結果

- **test_question_1.py**：測試用例
  - 驗證題目提供的所有範例
  - 額外測試邊界情況（負數、重複值等）

## 執行方式

### 直接執行（讀取標準輸入）
```bash
python question_1_solution.py
```

### 從檔案讀取輸入
```bash
python question_1_solution.py < input.txt > output.txt
```

### 執行測試
```bash
python test_question_1.py
```

## 核心算法

```python
def solve_data_cleaning(n, numbers, d):
    # 1. 去重並保留第一次出現的順序
    seen = set()
    unique_numbers = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            unique_numbers.append(num)
    
    # 2. 過濾能被 D 整除的數字
    divisible_numbers = [num for num in unique_numbers if num % d == 0]
    
    # 3. 若沒有符合條件則返回 NONE
    if not divisible_numbers:
        return "NONE"
    
    # 4. 排序並輸出
    divisible_numbers.sort()
    return " ".join(map(str, divisible_numbers))
```

## 時間複雜度

- **去重**：O(n)
- **過濾**：O(n)
- **排序**：O(n log n)
- **總計**：O(n log n)

## 空間複雜度

- O(n)（用於存儲唯一元素）

## 驗證結果

所有測試用例均已通過 ✅

```
✓ 範例第1組通過
✓ 範例第2組通過
✓ 範例第3組通過
✓ 去重測試通過
✓ 全偶數測試通過
✓ 負數測試通過
```

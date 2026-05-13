# QUESTION-10929-easy

## Divisibility by 11 (簡化版)

## 問題描述
判斷超大數字（最多 1000 位）是否為 11 的倍數

## 核心公式
**奇偶位檢驗法**：
- 從右往左數，奇數位（1,3,5...）的和為 `odd_sum`
- 從右往左數，偶數位（2,4,6...）的和為 `even_sum`
- 若 `(odd_sum - even_sum) % 11 == 0` 則為 11 的倍數

## 解題步驟
1. **從右往左遍歷**數字
2. **分別累加**奇偶位
3. **檢查**（odd_sum - even_sum) % 11 == 0

## 完整代碼（20 行）
```python
while True:
    s = input().strip()
    if s == '0': break
    
    odd_sum = 0
    even_sum = 0
    
    for idx, digit in enumerate(reversed(s)):
        if (idx + 1) % 2 == 1:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    
    if (odd_sum - even_sum) % 11 == 0:
        print(f"{s} is a multiple of 11.")
    else:
        print(f"{s} is not a multiple of 11.")
```

## 範例
- **121** → 1(奇) + 1(奇) - 2(偶) = 0 ✓
- **12** → 2(奇) - 1(偶) = 1 ✗

## 時間複雜度
**O(N)** - N 是數字位數

## 檢查清單
- ✓ 從右往左遍歷
- ✓ 位置 1,3,5... 為奇數位
- ✓ 計算 (odd - even) % 11

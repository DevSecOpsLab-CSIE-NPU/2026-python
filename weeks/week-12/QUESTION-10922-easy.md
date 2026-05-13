# QUESTION-10922-easy

## 2 the 9s (簡化版)

## 問題描述
判斷數字是否為 9 的倍數，若是則計算「9 度」（需要多少次數字和才能得到 9）

## 核心概念
**9 度**的定義：
- 9 → 深度 0（已經是 9）
- 18 → 1+8=9 → 深度 1
- 99 → 9+9=18 → 1+8=9 → 深度 2

## 解題步驟
1. **檢查倍數**：`if num % 9 != 0`
2. **計算數字和**：反覆將數字求和
3. **計數次數**：直到得到單位數 9

## 完整代碼（20 行）
```python
def digit_sum(s):
    return sum(int(c) for c in s)

while True:
    s = input().strip()
    if s == '0': break
    
    if int(s) % 9 != 0:
        print(f"{s} is not a multiple of 9.")
    else:
        depth = 0
        while len(s) > 1:
            s = str(digit_sum(s))
            depth += 1
        print(f"9-degree of {s} is {depth}.")
```

## 範例
- 9 → 深度 0
- 18 → 深度 1
- 999 → 深度 2
- 123 → not a multiple of 9

## 時間複雜度
**O(log N)** - N 是數字大小

## 檢查清單
- ✓ 9 倍數判斷：num % 9 == 0
- ✓ 計算數字和直到一位數
- ✓ 輸出格式：「is/is not a multiple」或「9-degree ... is N」

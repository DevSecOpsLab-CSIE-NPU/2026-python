# QUESTION-10812-easy

## Beat the Spread! (簡化版)

## 問題描述
給定兩隊總分 S 和分差 D，求各隊得分。

## 核心公式
$$\text{高分} = \frac{S + D}{2}$$
$$\text{低分} = \frac{S - D}{2}$$

## 解題步驟
1. **檢查可行性**：S+D 必須是偶數，且低分 ≥ 0
2. **計算高分**：(S + D) ÷ 2
3. **計算低分**：(S - D) ÷ 2

## 完整代碼（20 行）
```python
n = int(input())
for _ in range(n):
    s, d = map(int, input().split())
    if (s + d) % 2 != 0 or s < d:
        print("impossible")
    else:
        print(f"{(s+d)//2} {(s-d)//2}")
```

## 範例
- S=40, D=20 → (30, 10) ✓
- S=20, D=40 → impossible（低分為負）✗

## 時間複雜度
**O(N)** - N 是測試組數

## 檢查清單
- ✓ 檢查 (S+D) % 2 == 0
- ✓ 檢查 S >= D
- ✓ 輸出格式：「高分 低分」或「impossible」

# QUESTION-10929-hand

## 超濃縮參考 — Divisibility by 11

| 項目 | 說明 |
|------|------|
| **檢驗** | (奇數位和 - 偶數位和) % 11 == 0 |
| **位置** | 從右往左：1,3,5...為奇，2,4,6...為偶 |
| **輸出** | 「is/is not a multiple of 11」 |

## 代碼（12 行）
```python
while True:
    s = input().strip()
    if s == '0': break
    o = e = 0
    for i, d in enumerate(reversed(s)):
        if (i+1) % 2: o += int(d)
        else: e += int(d)
    print(f"{s} is {'a ' if (o-e)%11==0 else 'not a '}multiple of 11.")
```

## 範例計算
| 數字 | 奇位和 | 偶位和 | 差 | 結果 |
|-----|--------|--------|-----|------|
| 121 | 1+1=2 | 2 | 0 | ✓ |
| 12 | 2 | 1 | 1 | ✗ |
| 110 | 0+1=1 | 1 | 0 | ✓ |

## 位置示例
```
數字: 1 2 3 4
位置: 4 3 2 1 (從右往左)
類型: 偶 奇 偶 奇
```

## 複雜度
O(N) - N是數字位數

## 核心
`(odd_sum - even_sum) % 11 == 0`

# QUESTION-10812-hand

## 超濃縮參考 — Beat the Spread!

| 項目 | 說明 |
|------|------|
| **公式** | 高=（S+D）/2, 低=（S-D）/2 |
| **條件** | (S+D)%2==0 且 S≥D |
| **輸出** | 「impossible」或「高 低」 |

## 代碼（17 行）
```python
n = int(input())
for _ in range(n):
    s, d = map(int, input().split())
    if (s+d)%2 or s<d: print("impossible")
    else: print((s+d)//2, (s-d)//2)
```

## 邊界情況
- **S=0, D=0** → (0, 0)
- **S=2, D=2** → (2, 0)
- **S=1, D=0** → impossible (奇數)

## 複雜度
O(N)

## 核心檢查
```
if (S+D)為奇數 → impossible
if S<D → impossible
else → print((S+D)//2, (S-D)//2)
```

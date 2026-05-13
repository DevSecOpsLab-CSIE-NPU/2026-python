# QUESTION-10922-hand

## 超濃縮參考 — 2 the 9s

| 項目 | 說明 |
|------|------|
| **檢查** | `if num % 9 != 0` → 「not a multiple」 |
| **深度** | 反覆數字和直到一位數，計數次數 |
| **輸出** | 「is/is not」或「9-degree ... is N」 |

## 代碼（13 行）
```python
while True:
    s = input().strip()
    if s == '0': break
    if int(s) % 9: print(f"{s} is not a multiple of 9.")
    else:
        d = 0
        while len(s) > 1: s, d = str(sum(map(int, s))), d+1
        print(f"9-degree of {s} is {d}.")
```

## 深度範例
| 數字 | 過程 | 深度 |
|-----|------|------|
| 9 | 已是 9 | 0 |
| 18 | 1+8=9 | 1 |
| 99 | 9+9=18→1+8=9 | 2 |
| 999 | 9+9+9=27→2+7=9 | 2 |

## 複雜度
O(log N)

## 核心算法
```
while len(s) > 1:
    s = str(sum of digits)
    depth += 1
```

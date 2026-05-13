# QUESTION-10931-hand

## 超濃縮參考 — Parity

| 項目 | 說明 |
|------|------|
| **定義** | 奇偶性 = 二進位中 1 的個數 |
| **轉換** | `binary = bin(num)[2:]` |
| **計數** | `parity = binary.count('1')` |
| **輸出** | 「The parity of B is P (mod 2).」 |

## 代碼（7 行）
```python
while True:
    i = int(input())
    if not i: break
    b = bin(i)[2:]
    p = b.count('1')
    print(f"The parity of {b} is {p} (mod 2).")
```

## 轉換範例
| 十進位 | 二進位 | 1的個數 |
|--------|--------|----------|
| 1 | 1 | 1 |
| 2 | 10 | 1 |
| 3 | 11 | 2 |
| 5 | 101 | 2 |
| 21 | 10101 | 3 |
| 15 | 1111 | 4 |

## 複雜度
O(log N)

## 核心
```
binary = bin(i)[2:]
print(binary.count('1'))
```

## 進階
Brian Kernighan 演算法（位操作計數）：
```python
count = 0
while n:
    n &= n - 1
    count += 1
```

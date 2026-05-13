# 題目 10908 - 手寫版本

**題目**: UVA 10908 — Largest Square

## 一句話說明
給定網格和查詢點，找最大的同字元正方形

## 核心公式
```
邊長 = 2 × min(到四邊距離) + 1
```

## 關鍵概念

| 概念 | 說明 |
|------|------|
| **邊長** | 1, 3, 5, 7, ... (奇數) |
| **偏移量** | 邊長 // 2 |
| **中心** | (r, c) |

## 三步解法

### Step 1: 檢查邊長是否有效
```python
def is_valid(grid, r, c, size):
    # 1. 計算偏移量
    offset = size // 2
    
    # 2. 計算邊界
    top, bottom = r - offset, r + offset
    left, right = c - offset, c + offset
    
    # 3. 檢查邊界
    if top < 0 or bottom >= len(grid) or left < 0 or right >= len(grid[0]):
        return False
    
    # 4. 檢查字元
    center = grid[r][c]
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if grid[i][j] != center:
                return False
    return True
```

### Step 2: 尋找最大邊長
```python
def find_square(grid, r, c):
    M, N = len(grid), len(grid[0])
    
    # 計算最大邊長
    max_offset = min(r, M-1-r, c, N-1-c)
    max_size = 2 * max_offset + 1
    
    # 從大到小檢查
    for size in range(max_size, 0, -2):
        if is_valid(grid, r, c, size):
            return size
    return 1
```

### Step 3: 處理所有查詢
```python
def solve(m, n, q, grid, queries):
    results = []
    for r, c in queries:
        results.append(find_square(grid, r, c))
    return results
```

## 完整代碼

```python
def is_valid(grid, r, c, size):
    offset = size // 2
    top, bottom = r - offset, r + offset
    left, right = c - offset, c + offset
    
    if top < 0 or bottom >= len(grid) or left < 0 or right >= len(grid[0]):
        return False
    
    center = grid[r][c]
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if grid[i][j] != center:
                return False
    return True

def find_square(grid, r, c):
    M, N = len(grid), len(grid[0])
    max_offset = min(r, M-1-r, c, N-1-c)
    max_size = 2 * max_offset + 1
    
    for size in range(max_size, 0, -2):
        if is_valid(grid, r, c, size):
            return size
    return 1

T = int(input())
for _ in range(T):
    m, n, q = map(int, input().split())
    grid = [list(input().strip()) for _ in range(m)]
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    
    print(m, n, q)
    for r, c in queries:
        print(find_square(grid, r, c))
```

## 視覺化例子

```
網格 (7×10)：
abbbaaaaaa   <- row 0
abbbaaaaaa   <- row 1 (查詢 (1,2) → 答案 3)
abbbaaaaaa   <- row 2
aaaaaaaaaa   <- row 3
aaaaaaaaaa   <- row 4 (查詢 (4,6) → 答案 5)
aaccaaaaaa   <- row 5 (查詢 (5,2) → 答案 1)
aaccaaaaaa   <- row 6
```

## 邊長計算例子

**查詢 (1, 2)，中心是 'b'**
- 到上邊界: 1, 到下邊界: 5 → min = 1
- 到左邊界: 2, 到右邊界: 7 → min = 2
- 四個方向最小: min(1, 5, 2, 7) = 1
- 最大邊長: 2×1+1 = 3 ✓

**查詢 (4, 6)，中心是 'a'**
- 到上邊界: 4, 到下邊界: 2 → min = 2
- 到左邊界: 6, 到右邊界: 3 → min = 3
- 四個方向最小: min(4, 2, 6, 3) = 2
- 最大邊長: 2×2+1 = 5 ✓

## 檢查清單

- [ ] 邊長只有奇數 (1, 3, 5, ...)
- [ ] offset = size // 2
- [ ] 邊界範圍：[r-offset, r+offset] 和 [c-offset, c+offset]
- [ ] 邊界檢查：top < 0, bottom >= M, left < 0, right >= N
- [ ] 字元檢查：所有格子都 == 中心字元
- [ ] 距離計算：min(r, M-1-r, c, N-1-c)
- [ ] 邊長計算：2 × offset + 1
- [ ] 從大到小檢查 (size, 0, -2)

## 重點提示

1. **邊長必須是奇數** - 用 -2 步長保證
2. **偏移量** - size // 2 (向下取整)
3. **邊界檢查先於字元檢查** - 提高效率
4. **從大到小找** - 第一個有效就是最大的
5. **範圍包含邊界** - range(top, bottom + 1)

## 時間複雜度

- 單個查詢: O(max_size²) ≈ O(min(M,N)²)
- 總時間: O(Q × M × N)
- 實際很快，大多數不會檢查到最大邊長

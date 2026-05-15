# 題目 10908

**題名**: UVA 10908 — Largest Square

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a901)
- [UVA Online Judge](https://uva.onlinejudge.org/external/10908.pdf)

## 題目敘述

給定一個 **M 行 N 列**的字元網格，以及 Q 個查詢。

對於每個查詢，給定一個中心點座標 **(r, c)**，找出以該點為**中心（對角線交叉點）**，且**所有字元相同**的**最大正方形的邊長**。

**注意：**
- 網格左上角座標為 **(0, 0)**，右下角為 **(M-1, N-1)**。
- 正方形的邊長必須為**奇數**（1, 3, 5, …），因為中心點需要恰好落在正方形的中心格上。

## 輸入說明

- 第一行包含一個整數 **T**（T < 21）。
- 每組測試資料：
  - 第一行包含三個整數 **M、N、Q**（M, N ≤ 100，Q < 21），表示網格的行數、列數，及查詢次數。
  - 接下來 M 行，每行包含 N 個字元（組成字元網格）。
  - 接下來 Q 行，每行包含兩個整數 **r** 和 **c**（中心點座標）。

## 輸出說明

- 對每組測試資料，先輸出一行 **M N Q**（三個數以空格分隔）。
- 接下來 Q 行，每行輸出對應查詢的**最大正方形邊長**。

---

## 解題思路

這道題目要求我們在一個字元網格中，給定中心點 $(r, c)$，找出以該點為中心且所有字元都相同的最大奇數邊長正方形。

1. **基本檢查**：
   - 邊長為 1 的正方形（即中心點本身）永遠是滿足條件的（只要座標在網格內）。
   - 我們可以從邊長 $L = 3, 5, 7, \dots$ 開始向外擴張檢查。

2. **擴張策略**：
   - 定義 $k$ 為從中心點向外的偏移量（$k = (L-1)/2$）。
   - 每次檢查邊長為 $L = 2k+1$ 的正方形時，需要確保：
     - 正方形的四個邊界都在網格範圍內：$r-k \ge 0, r+k < M, c-k \ge 0, c+k < N$。
     - 正方形四條邊上的所有字元都必須等於中心點的字元 `grid[r][c]`。
   - 如果當前 $k$ 滿足條件，則嘗試 $k+1$；否則，最大邊長即為 $2(k-1)+1$。

3. **效率考量**：
   - 網格大小最大為 $100 \times 100$，查詢次數最多 20 次。
   - 暴力法（Brute-force）對每一層擴張進行檢查，時間複雜度在可接受範圍內。

## 解題代碼

```python
import sys

def solve():
    # 讀取所有輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    T_str = input_data[idx]
    idx += 1
    T = int(T_str)
    
    for _ in range(T):
        M = int(input_data[idx])
        N = int(input_data[idx+1])
        Q = int(input_data[idx+2])
        idx += 3
        
        grid = []
        for i in range(M):
            grid.append(input_data[idx])
            idx += 1
        
        # 輸出第一行 M N Q
        print(f"{M} {N} {Q}")
        
        for _ in range(Q):
            r = int(input_data[idx])
            c = int(input_data[idx+1])
            idx += 2
            
            target = grid[r][c]
            max_len = 1
            
            # 從 k=1 (邊長 3) 開始嘗試擴張
            k = 1
            while True:
                # 檢查邊界
                if r - k < 0 or r + k >= M or c - k < 0 or c + k >= N:
                    break
                
                # 檢查邊界上的字元是否都與中心點相同
                possible = True
                # 檢查上下兩行
                for j in range(c - k, c + k + 1):
                    if grid[r - k][j] != target or grid[r + k][j] != target:
                        possible = False
                        break
                if not possible:
                    break
                
                # 檢查左右兩列
                for i in range(r - k, r + k + 1):
                    if grid[i][c - k] != target or grid[i][c + k] != target:
                        possible = False
                        break
                if not possible:
                    break
                
                # 若通過檢查，更新最大邊長並繼續擴張
                max_len = 2 * k + 1
                k += 1
            
            print(max_len)

if __name__ == "__main__":
    solve()
```

## 測試用例

```
輸入:
1
7 10 4
abbbaaaaaa
abbbaaaaaa
abbbaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaccaaaaaa
aaccaaaaaa
1 2
2 4
4 6
5 2

輸出:
7 10 4
3
1
5
1
```

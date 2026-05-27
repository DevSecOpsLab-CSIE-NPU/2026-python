import sys
import math

def solve():
    # 讀取全部的輸入資料，並直接全部轉換為整數 (int)
    nums = map(int, sys.stdin.read().split())
    
    for n in nums:
        # 遇到 N = 0 代表程式結束
        if n == 0:
            break
            
        # 神奇小技巧：使用 sum() 搭配生成器，把雙層迴圈濃縮成一行！
        # 語意非常直觀：「加總所有的 gcd(i, j)，其中 i 從 1 到 n-1，j 從 i+1 到 n」
        total_gcd = sum(math.gcd(i, j) for i in range(1, n) for j in range(i + 1, n + 1))
        print(total_gcd)

if __name__ == '__main__':
    solve()
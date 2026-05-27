# UVA 11417 - GCD (AI 版本)
import sys
import math

def solve():
    # 讀取所有的輸入的行
    lines = sys.stdin.read().split()
    for line in lines:
        n = int(line)
        if n == 0:
            break
            
        # 計算所有的 i, j 對的最大公因數總和
        g = 0
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                g += math.gcd(i, j)
                
        # 輸出結果
        print(g)

if __name__ == '__main__':
    solve()

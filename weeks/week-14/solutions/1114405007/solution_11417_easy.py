"""
題目 11417 - GCD (最大公因數總和) - 簡易版本
使用更簡潔的寫法，易於在考場快速實現
"""

from math import gcd

# 直接計算 GCD 總和
def solve():
    while True:
        n = int(input())
        if n == 0:
            break
        
        # 簡潔寫法：雙層迴圈累加 GCD
        total = sum(gcd(i, j) for i in range(1, n) for j in range(i + 1, n + 1))
        print(total)


if __name__ == '__main__':
    solve()

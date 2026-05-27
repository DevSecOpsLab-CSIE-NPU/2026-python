import sys
import math

def solve():
    """
    UVA 11417 - GCD
    讀取標準輸入，對於每個輸入的 N (直到 N=0 為止)，
    計算所有的 GCD(i, j) 總和 (1 <= i < j <= N)。
    """
    # 讀取所有輸入資料並以空白或換行分割
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    for token in input_data:
        n = int(token)
        # 遇到 N = 0 結束程式
        if n == 0:
            break
            
        total_gcd = 0
        # 根據題目要求，i 從 1 走到 n-1，j 從 i+1 走到 n
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                total_gcd += math.gcd(i, j)
                
        # 輸出計算結果
        print(total_gcd)

if __name__ == '__main__':
    solve()
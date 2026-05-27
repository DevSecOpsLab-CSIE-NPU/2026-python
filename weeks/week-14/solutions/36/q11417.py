# GCD 解答程式
# 題目 11417: UVA — GCD
# 計算所有數對 (i, j) 的 GCD 總和，其中 1 <= i < j <= N

import math

def sum_of_gcds(n):
    """
    計算所有滿足 1 <= i < j <= n 的整數數對之 GCD 總和
    
    公式：G = ∑(i=1 to n-1) ∑(j=i+1 to n) gcd(i, j)
    
    參數:
        n: 正整數
    
    返回:
        所有數對 GCD 的總和
    """
    total = 0
    
    # 雙層迴圈遍歷所有數對 (i, j)
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            # 累加 gcd(i, j)
            total += math.gcd(i, j)
    
    return total

def main():
    """
    主程式：讀取輸入並輸出結果
    """
    while True:
        n = int(input())
        
        # 輸入 0 表示結束
        if n == 0:
            break
        
        result = sum_of_gcds(n)
        print(result)

if __name__ == '__main__':
    main()

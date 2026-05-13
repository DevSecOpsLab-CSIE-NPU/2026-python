"""
題目 10931 - Parity (簡易版)

核心概念：
- 奇偶性 = 二進位中 1 的個數
"""


# 讀取輸入
while True:
    i = int(input())
    if i == 0:
        break
    
    # 轉為二進位並計數 1 的個數
    binary = bin(i)[2:]
    parity = binary.count('1')
    
    # 輸出
    print(f"The parity of {binary} is {parity} (mod 2).")

# 10019-easy.py
# UVA 10019：Funny Encryption Method (簡單版)

import sys

def solve():
    # 1. 讀入所有資料
    input_data = sys.stdin.read().split()
    if not input_data: return

    n_cases = int(input_data[0])

    for i in range(1, n_cases + 1):
        m_str = input_data[i]

        # 2. b1: 把 m_str 當成十進位數字，數二進位有幾個 1
        n1 = int(m_str)
        b1 = bin(n1).count('1')

        # 3. b2: 把 m_str 當成十六進位數字，數二進位有幾個 1
        # 例如 m=299，b2 就是把 299(十六進位) 轉成二進位後的 1 個數
        n2 = int(m_str, 16)
        b2 = bin(n2).count('1')

        # 4. 輸出
        print(f"{b1} {b2}")

if __name__ == "__main__":
    solve()

"""
UVA 10931 — Parity 簡單版本
更簡單易記的寫法

核心思想：
- bin(n) 轉為二進位字串
- count('1') 計算1的個數
- 直接格式化輸出
"""


def parity_simple(num):
    """
    最簡單的解法
    
    只需要記住三行代碼：
    1. binary_str = bin(num)[2:]
    2. count = binary_str.count('1')
    3. 格式化輸出
    """
    # 轉為二進位字串（去掉 '0b'）
    binary = bin(num)[2:]
    
    # 計算1的個數
    ones = binary.count('1')
    
    # 輸出結果
    return f"The parity of {binary} is {ones} (mod 2)."


# 測試
if __name__ == "__main__":
    print(parity_simple(1))    # The parity of 1 is 1 (mod 2).
    print(parity_simple(2))    # The parity of 10 is 1 (mod 2).
    print(parity_simple(10))   # The parity of 1010 is 2 (mod 2).
    print(parity_simple(21))   # The parity of 10101 is 3 (mod 2).

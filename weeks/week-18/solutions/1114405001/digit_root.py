"""
Implementation of digit root in base 8
題目：任意進位的數字根（進位基底 = 8）
"""


def digit_root_base8(n):
    """
    計算一個數字在 8 進位下的數字根。
    
    演算法：
    1. 將十進位數字轉換為 8 進位
    2. 計算 8 進位表示中各位數字的和
    3. 如果結果 >= 8，重複步驟 2
    4. 返回個位數結果
    
    Args:
        n (int): 十進位數字
    
    Returns:
        int: 數字根（0-7 之間）
    """
    # 特殊情況：0 的數字根是 0
    if n == 0:
        return 0
    
    base = 8
    
    # 重複相加直到得到個位數（在 base 8 下）
    while n >= base:
        digit_sum = 0
        # 計算 n 在 base 8 下各位數字的和
        while n > 0:
            digit_sum += n % base
            n //= base
        n = digit_sum
    
    return n

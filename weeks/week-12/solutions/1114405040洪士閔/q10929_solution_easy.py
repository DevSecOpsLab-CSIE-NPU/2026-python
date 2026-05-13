"""
題目 10929 - Divisibility by 11 (簡易版)

核心公式：
- 奇數位和 - 偶數位和 ≡ 0 (mod 11) 則為 11 的倍數
"""


def is_div_11(num_str):
    """判斷是否為 11 的倍數"""
    odd_sum = 0
    even_sum = 0
    
    # 從右往左，奇數位和偶數位交替累加
    for idx, digit in enumerate(reversed(num_str)):
        if (idx + 1) % 2 == 1:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    
    return (odd_sum - even_sum) % 11 == 0


# 讀取輸入
while True:
    s = input().strip()
    if s == '0':
        break
    
    if is_div_11(s):
        print(f"{s} is a multiple of 11.")
    else:
        print(f"{s} is not a multiple of 11.")

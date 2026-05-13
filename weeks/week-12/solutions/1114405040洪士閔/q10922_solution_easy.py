"""
題目 10922 - 2 the 9s (簡易版)

核心概念：
- 9 度 = 需要幾次數字和才能得到一位數 9
"""


def digit_sum(s):
    """計算數字和"""
    return sum(int(c) for c in s)


def degree_of_nine(s):
    """計算 9 的深度"""
    depth = 0
    while len(s) > 1:
        s = str(digit_sum(s))
        depth += 1
    return depth


# 讀取輸入
while True:
    s = input().strip()
    if s == '0':
        break
    
    if int(s) % 9 != 0:
        print(f"{s} is not a multiple of 9.")
    else:
        print(f"9-degree of {s} is {degree_of_nine(s)}.")

#!/usr/bin/env python3
# 簡潔易懂版（繁體中文註解）
# 逐次把數字各位相加，直到剩一位；若結果為 9 則為 9 的倍數，並計算次數
import sys

def digit_sum(s):
    return sum(map(int, s))

if __name__=='__main__':
    for line in sys.stdin:
        num = line.strip()
        if not num: continue
        if num == '0': break
        s = digit_sum(num)
        if s % 9 != 0:
            print(f"{num} is not a multiple of 9.")
        else:
            degree = 1
            while s > 9:
                s = digit_sum(str(s))
                degree += 1
            print(f"9-degree of {num} is {degree}.")

#!/usr/bin/env python3
import sys

def sum_digits_str(s):
    return sum(int(ch) for ch in s)

for line in sys.stdin:
    n = line.strip()
    if not n:
        continue
    if n == '0':
        break
    s = sum_digits_str(n)
    if s % 9 != 0:
        print(f"{n} is not a multiple of 9.")
    else:
        degree = 1
        while s > 9:
            s = sum_digits_str(str(s))
            degree += 1
        print(f"9-degree of {n} is {degree}.")

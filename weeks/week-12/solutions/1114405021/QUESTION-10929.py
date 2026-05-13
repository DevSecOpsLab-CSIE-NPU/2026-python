#!/usr/bin/env python3
import sys

for line in sys.stdin:
    n = line.strip()
    if not n: continue
    if n == '0': break
    s_odd = 0
    s_even = 0
    # positions: leftmost is position 1? Problem uses digits positions starting from left or right?
    # Standard approach: iterate digits left to right and alternate adding to odd/even.
    odd = True
    for ch in n:
        if odd:
            s_odd += int(ch)
        else:
            s_even += int(ch)
        odd = not odd
    if (s_odd - s_even) % 11 == 0:
        print(f"{n} is a multiple of 11.")
    else:
        print(f"{n} is not a multiple of 11.")

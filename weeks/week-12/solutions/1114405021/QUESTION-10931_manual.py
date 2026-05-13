#!/usr/bin/env python3
# 手打版本
import sys
for line in sys.stdin:
    s=line.strip()
    if not s: continue
    n=int(s)
    if n==0: break
    b=bin(n)[2:]
    p=b.count('1')
    print(f"The parity of {b} is {p} (mod 2).")

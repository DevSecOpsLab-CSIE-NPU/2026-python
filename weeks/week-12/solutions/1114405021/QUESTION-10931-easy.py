#!/usr/bin/env python3
# 簡單版，註解繁體中文：把整數轉二進位，數 1 的個數
import sys
for line in sys.stdin:
    s=line.strip()
    if not s: continue
    n=int(s)
    if n==0: break
    b=format(n,'b')
    ones=b.count('1')
    print(f"The parity of {b} is {ones} (mod 2).")

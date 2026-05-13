#!/usr/bin/env python3
# 手打版本
import sys
for line in sys.stdin:
    n=line.strip()
    if not n: continue
    if n=='0': break
    s=sum(int(c) for c in n)
    if s%9!=0:
        print(f"{n} is not a multiple of 9.")
    else:
        deg=1
        while s>9:
            s=sum(int(c) for c in str(s))
            deg+=1
        print(f"9-degree of {n} is {deg}.")

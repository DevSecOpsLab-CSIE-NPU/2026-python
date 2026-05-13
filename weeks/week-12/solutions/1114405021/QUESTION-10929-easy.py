#!/usr/bin/env python3
# 簡單說明：交替相加奇偶位數的和，差是否能被 11 整除
import sys

for line in sys.stdin:
    n=line.strip()
    if not n: continue
    if n=='0': break
    s1=0;s2=0;flag=True
    for ch in n:
        if flag: s1+=int(ch)
        else: s2+=int(ch)
        flag=not flag
    if (s1-s2)%11==0:
        print(f"{n} is a multiple of 11.")
    else:
        print(f"{n} is not a multiple of 11.")

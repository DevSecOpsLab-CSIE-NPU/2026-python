# -*- coding: utf-8 -*-
import sys

def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    
    t = int(tokens[0])
    idx = 1
    for c in range(1, t + 1):
        idx += 2  # 跳過 'N' 和 '='
        n = int(tokens[idx])
        idx += 1
        
        sz = n * n
        arr = [int(x) for x in tokens[idx : idx + sz]]
        idx += sz
        
        ok = True
        for i in range(sz):
            if arr[i] < 0 or arr[i] != arr[sz - 1 - i]:
                ok = False
                break
                
        print(f"Test #{c}: {'Symmetric.' if ok else 'Non-symmetric.'}")

if __name__ == "__main__":
    solve()

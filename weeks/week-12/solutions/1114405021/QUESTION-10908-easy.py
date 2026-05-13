#!/usr/bin/env python3
# 簡易版：繁體中文註解
# 對每個查詢從中心往外擴增，檢查方形區域是否都相同字元
import sys

def main():
    parts = sys.stdin.read().strip().split()
    if not parts:
        return
    t = int(parts[0]); i = 1
    out = []
    for _ in range(t):
        M = int(parts[i]); N = int(parts[i+1]); Q = int(parts[i+2]); i += 3
        grid = [list(parts[i + r]) for r in range(M)]
        i += M
        out.append(f"{M} {N} {Q}")
        for _ in range(Q):
            r = int(parts[i]); c = int(parts[i+1]); i += 2
            ch = grid[r][c]
            k = 0
            while True:
                if r-k < 0 or r+k >= M or c-k < 0 or c+k >= N:
                    break
                ok = True
                for rr in range(r-k, r+k+1):
                    for cc in range(c-k, c+k+1):
                        if grid[rr][cc] != ch:
                            ok = False; break
                    if not ok: break
                if not ok: break
                k += 1
            out.append(str(2*(k-1)+1 if k>0 else 1))
    print('\n'.join(out))

if __name__=='__main__':
    main()

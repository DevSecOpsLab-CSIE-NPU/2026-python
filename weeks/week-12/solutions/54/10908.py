"""
10908 — Largest Square (簡單版，含中文註解)
給定字元網格與查詢中心點，找出以該點為中心且全部字元相同的最大正方形邊長（奇數）。
"""
import sys

def solve(lines=None):
    if lines is None:
        data = sys.stdin.read().strip().split()
    else:
        data = "\n".join(lines).strip().split()
    if not data:
        return []
    it = iter(data)
    T = int(next(it))
    out = []
    for _ in range(T):
        M = int(next(it)); N = int(next(it)); Q = int(next(it))
        grid = []
        for _m in range(M):
            grid.append(list(next(it).strip()))
        out.append(f"{M} {N} {Q}")
        for _q in range(Q):
            r = int(next(it)); c = int(next(it))
            ch = grid[r][c]
            layer = 0
            while True:
                side = 2*layer+1
                top = r - layer
                left = c - layer
                bottom = r + layer
                right = c + layer
                if top < 0 or left < 0 or bottom >= M or right >= N:
                    break
                ok = True
                for i in range(top, bottom+1):
                    for j in range(left, right+1):
                        if grid[i][j] != ch:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    break
                layer += 1
            # 最後一次增加失敗，實際最大為 layer-1
            max_side = 2*(layer-1)+1
            out.append(str(max_side))
    return out

if __name__ == '__main__':
    for l in solve():
        print(l)

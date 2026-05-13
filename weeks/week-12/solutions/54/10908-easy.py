"""
10908-easy — 更簡單易記的寫法（含中文註解）
直接檢查每個可能的正方形範圍，依序找最大值，程式簡潔可讀。
"""
import sys

def solve(lines=None):
    if lines is None:
        data = sys.stdin.read().strip().split()
    else:
        data = "\n".join(lines).strip().split()
    it = iter(data)
    T = int(next(it))
    out = []
    for _ in range(T):
        M = int(next(it)); N = int(next(it)); Q = int(next(it))
        grid = [list(next(it)) for _ in range(M)]
        out.append(f"{M} {N} {Q}")
        for _ in range(Q):
            r = int(next(it)); c = int(next(it))
            ch = grid[r][c]
            best = 1
            # 最大可能半徑
            max_r = min(r, c, M-1-r, N-1-c)
            for layer in range(1, max_r+1):
                ok = True
                top = r - layer; bottom = r + layer
                left = c - layer; right = c + layer
                for i in range(top, bottom+1):
                    for j in range(left, right+1):
                        if grid[i][j] != ch:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    best = 2*layer+1
                else:
                    break
            out.append(str(best))
    return out

if __name__ == '__main__':
    for l in solve():
        print(l)

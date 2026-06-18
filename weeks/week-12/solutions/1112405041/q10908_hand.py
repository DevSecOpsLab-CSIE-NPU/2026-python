# 手打版: 10908
import sys

def solve():
    r = sys.stdin.read().split()
    if not r: return
    i = 0
    t = int(r[i]); i += 1
    for _ in range(t):
        m, n, q = int(r[i]), int(r[i+1]), int(r[i+2]); i += 3
        g = r[i:i+m]; i += m
        print(m, n, q)
        for _ in range(q):
            rc, cc = int(r[i]), int(r[i+1]); i += 2
            v = g[rc][cc]
            a = 1
            while True:
                s = (a+1)//2
                r1, r2, c1, c2 = rc-s, rc+s, cc-s, cc+s
                if r1<0 or r2>=m or c1<0 or c2>=n: break
                ok = True
                for y in range(r1, r2+1):
                    for x in range(c1, c2+1):
                        if g[y][x] != v: ok = False; break
                    if not ok: break
                if ok: a += 2
                else: break
            print(a)

if __name__ == "__main__":
    solve()

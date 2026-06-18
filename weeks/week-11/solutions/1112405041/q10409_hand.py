# 手打版: 10409
import sys

def solve():
    raw = sys.stdin.read().split()
    p = 0
    while p < len(raw):
        n = int(raw[p]); p += 1
        if n == 0: break
        t, nf, w, s, e, b = 1, 2, 3, 5, 4, 6
        for _ in range(n):
            c = raw[p]; p += 1
            if c == "north": t, nf, b, s = s, t, nf, b
            elif c == "south": t, s, b, nf = nf, t, s, b
            elif c == "east": t, e, b, w = w, t, e, b
            elif c == "west": t, w, b, e = e, t, w, b
        print(t)

if __name__ == "__main__":
    solve()

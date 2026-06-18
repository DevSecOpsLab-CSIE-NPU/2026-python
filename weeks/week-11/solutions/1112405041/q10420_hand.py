# 手打版: 10420
import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines: return
    d = {}
    for l in lines[1:]:
        parts = l.split()
        if not parts: continue
        c = parts[0]
        d[c] = d.get(c, 0) + 1
    for k in sorted(d):
        print(f"{k} {d[k]}")

if __name__ == "__main__":
    solve()

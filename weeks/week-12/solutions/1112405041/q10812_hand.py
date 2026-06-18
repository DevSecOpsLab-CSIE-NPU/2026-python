# 手打版: 10812
import sys

def solve():
    r = list(map(int, sys.stdin.read().split()))
    if not r: return
    for i in range(r[0]):
        s, d = r[1+i*2], r[2+i*2]
        if s < d or (s + d) % 2: print("impossible")
        else:
            x = (s + d) // 2
            y = (s - d) // 2
            print(x, y)

if __name__ == "__main__":
    solve()

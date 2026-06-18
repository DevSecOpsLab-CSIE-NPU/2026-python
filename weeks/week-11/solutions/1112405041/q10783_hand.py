# 手打版: 10783
import sys

def solve():
    r = list(map(int, sys.stdin.read().split()))
    if not r: return
    for i in range(r[0]):
        a, b = r[1+i*2], r[2+i*2]
        if a % 2 == 0: a += 1
        s = 0
        for x in range(a, b + 1, 2): s += x
        print(f"Case {i+1}: {s}")

if __name__ == "__main__":
    solve()

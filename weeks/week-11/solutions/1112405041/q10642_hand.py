# 手打版: 10642
import sys

def p(x, y):
    return (x+y)*(x+y+1)//2 + x

def solve():
    r = list(map(int, sys.stdin.read().split()))
    if not r: return
    for i in range(r[0]):
        v = r[1+i*4:5+i*4]
        print(f"Case {i+1}: {p(v[2], v[3]) - p(v[0], v[1])}")

if __name__ == "__main__":
    solve()

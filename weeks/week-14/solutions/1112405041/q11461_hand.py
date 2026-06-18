import math, sys
def solve():
    for l in sys.stdin:
        a, b = map(int, l.split())
        if a == 0 and b == 0: break
        print(int(math.isqrt(b)) - int(math.isqrt(a-1)))
if __name__ == '__main__': solve()

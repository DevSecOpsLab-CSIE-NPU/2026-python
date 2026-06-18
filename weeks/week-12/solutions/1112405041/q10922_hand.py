# 手打版: 10922
import sys

def solve():
    for l in sys.stdin:
        n = l.strip()
        if n == "0": break
        s, d = n, 0
        while True:
            v = sum(int(c) for c in s); d += 1
            if v == 9:
                print(f"{n} is a multiple of 9 and has 9-degree {d}.")
                break
            if v % 9:
                print(f"{n} is not a multiple of 9.")
                break
            s = str(v)

if __name__ == "__main__":
    solve()

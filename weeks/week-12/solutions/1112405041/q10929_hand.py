# 手打版: 10929
import sys

def solve():
    for l in sys.stdin:
        n = l.strip()
        if n == "0": break
        r = 0
        for c in n: r = (r * 10 + int(c)) % 11
        if r == 0: print(f"{n} is a multiple of 11.")
        else: print(f"{n} is not a multiple of 11.")

if __name__ == "__main__":
    solve()

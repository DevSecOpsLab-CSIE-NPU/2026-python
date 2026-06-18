# 手打版: 10931
import sys

def solve():
    for l in sys.stdin:
        line = l.strip()
        if not line: continue
        n = int(line)
        if n == 0: break
        b = bin(n)[2:]
        p = b.count('1')
        print(f"The parity of {b} is {p} (mod 2).")

if __name__ == "__main__":
    solve()

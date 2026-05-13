"""
10931 — 手寫版程式（供測試）
"""
import sys

def solve(lines=None):
    if lines is None:
        lines = sys.stdin.read().strip().split()
    out = []
    for token in lines:
        if not token:
            continue
        n = int(token)
        if n == 0:
            break
        b = format(n, 'b')
        ones = b.count('1')
        out.append(f"The parity of {b} is {ones} (mod 2).")
    return out

if __name__ == '__main__':
    for line in solve():
        print(line)

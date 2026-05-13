"""
10931 — Parity (簡單版，含中文註解)
題目：輸入整數 I，列出其二進位表示及其中 1 的個數。
"""
import sys

def solve(lines=None):
    if lines is None:
        data = sys.stdin.read().strip().split()
    else:
        data = [l.strip() for l in lines if l.strip()]
    out_lines = []
    for token in data:
        n = int(token)
        if n == 0:
            break
        b = bin(n)[2:]
        p = b.count('1')
        out_lines.append(f"The parity of {b} is {p} (mod 2).")
    return out_lines

if __name__ == '__main__':
    for l in solve():
        print(l)

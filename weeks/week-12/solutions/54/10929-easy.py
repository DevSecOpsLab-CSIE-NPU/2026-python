"""
10929-easy — 更容易記憶的寫法（含中文註解）
直接用交替累加法判斷是否為 11 的倍數。
"""
import sys

def solve(lines=None):
    if lines is None:
        lines = sys.stdin.read().strip().split()
    out = []
    for token in lines:
        if token == '0':
            break
        s = token.strip()
        total = 0
        for i,ch in enumerate(s):
            if i % 2 == 0:
                total += int(ch)
            else:
                total -= int(ch)
        if total % 11 == 0:
            out.append(f"{s} is a multiple of 11.")
        else:
            out.append(f"{s} is not a multiple of 11.")
    return out

if __name__ == '__main__':
    for l in solve():
        print(l)

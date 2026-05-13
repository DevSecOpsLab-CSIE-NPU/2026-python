"""
10922-easy — 更簡單的寫法（含中文註解）
使用字串與簡單迴圈，邏輯直觀易記。
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
        count = 0
        total = sum(int(ch) for ch in s)
        if total % 9 != 0:
            out.append(f"{s} is not a multiple of 9.")
            continue
        degree = 1
        while total > 9:
            total = sum(int(ch) for ch in str(total))
            degree += 1
        out.append(f"9-degree of {s} is {degree}.")
    return out

if __name__ == '__main__':
    for l in solve():
        print(l)

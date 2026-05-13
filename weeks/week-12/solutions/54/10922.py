"""
10922 — 2 the 9s (簡單版，含中文註解)
判斷一個數字是否為 9 的倍數，並計算其 9-degree。
"""
import sys

def sum_digits_str(s):
    return sum(int(ch) for ch in s)

def solve(lines=None):
    if lines is None:
        lines = sys.stdin.read().strip().split()
    out = []
    for token in lines:
        if token == '0':
            break
        s = token.strip()
        total = sum_digits_str(s)
        if total % 9 != 0:
            out.append(f"{s} is not a multiple of 9.")
        else:
            degree = 1
            while total > 9:
                total = sum_digits_str(str(total))
                degree += 1
            if total == 9:
                out.append(f"9-degree of {s} is {degree}.")
            else:
                out.append(f"{s} is not a multiple of 9.")
    return out

if __name__ == '__main__':
    for l in solve():
        print(l)

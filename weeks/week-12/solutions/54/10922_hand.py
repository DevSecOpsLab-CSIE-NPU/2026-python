"""
10922 — 手寫版（含中文註解）
實作 9 的遞迴求和並計算 degree。
"""
import sys

def digit_sum_str(s):
    return sum(int(c) for c in s)

def solve(lines=None):
    if lines is None:
        lines = sys.stdin.read().strip().split()
    res = []
    for token in lines:
        if token == '0':
            break
        s = token.strip()
        total = digit_sum_str(s)
        if total % 9 != 0:
            res.append(f"{s} is not a multiple of 9.")
            continue
        # 是 9 的倍數，計算 degree
        degree = 1
        while total > 9:
            total = digit_sum_str(str(total))
            degree += 1
        res.append(f"9-degree of {s} is {degree}.")
    return res

if __name__ == '__main__':
    for line in solve():
        print(line)

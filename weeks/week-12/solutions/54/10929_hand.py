"""
10929 — 手寫版（含中文註解）
使用交替相加相減的技巧計算是否為 11 的倍數。
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
        odd_sum = 0
        even_sum = 0
        # 從左到右，index 0 為偶數位置
        for i,ch in enumerate(s):
            if i % 2 == 0:
                even_sum += int(ch)
            else:
                odd_sum += int(ch)
        if (even_sum - odd_sum) % 11 == 0:
            out.append(f"{s} is a multiple of 11.")
        else:
            out.append(f"{s} is not a multiple of 11.")
    return out

if __name__ == '__main__':
    for l in solve():
        print(l)

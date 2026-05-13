"""
10812 — Beat the Spread! (簡單版，含中文註解)
題目：給定 S (和) 與 D (差)，求兩隊分數（較大先輸出），否則輸出 impossible。
"""
import sys

def solve(lines=None):
    if lines is None:
        data = sys.stdin.read().strip().split()
    else:
        data = "\n".join(lines).strip().split()
    if not data:
        return []
    t = int(data[0])
    out_lines = []
    idx = 1
    for _ in range(t):
        S = int(data[idx]); D = int(data[idx+1]); idx += 2
        # 公式：大分 = (S + D) / 2，小分 = (S - D) / 2
        # 檢查整數與非負
        if S < D or (S + D) % 2 != 0:
            out_lines.append('impossible')
        else:
            a = (S + D) // 2
            b = (S - D) // 2
            if a < 0 or b < 0:
                out_lines.append('impossible')
            else:
                out_lines.append(f"{a} {b}")
    return out_lines

if __name__ == '__main__':
    for line in solve():
        print(line)

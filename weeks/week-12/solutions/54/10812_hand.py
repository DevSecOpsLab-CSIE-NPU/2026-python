"""
10812 — 手寫版程式 (較可讀，供測試用)
此檔案實作同樣邏輯並提供可被測試的 `solve()`。
"""
import sys

def solve(lines=None):
    # 允許傳入 lines（list of str）以便測試
    if lines is None:
        tokens = sys.stdin.read().strip().split()
    else:
        tokens = "\n".join(lines).strip().split()
    if not tokens:
        return []
    t = int(tokens[0])
    res = []
    pos = 1
    for _ in range(t):
        S = int(tokens[pos]); D = int(tokens[pos+1]); pos += 2
        if S < D:
            res.append('impossible')
            continue
        if (S + D) % 2 != 0:
            res.append('impossible')
            continue
        high = (S + D) // 2
        low = (S - D) // 2
        if low < 0:
            res.append('impossible')
        else:
            res.append(f"{high} {low}")
    return res

if __name__ == '__main__':
    for line in solve():
        print(line)

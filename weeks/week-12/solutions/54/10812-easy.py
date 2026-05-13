"""
10812-easy — 更簡單且容易記憶的實作

說明（繁體中文詳細註解）:
- 題目給定 S (兩隊分數和) 與 D (兩隊分數差的絕對值)。
- 若存在整數解，則較大分數 = (S + D) / 2，較小分數 = (S - D) / 2。
- 條件檢查：S >= D、S + D 必須為偶數、且兩個解都非負。

此檔案為簡潔實作，易於記憶與閱讀。
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
    idx = 1
    out = []
    for _ in range(t):
        S = int(data[idx]); D = int(data[idx+1]); idx += 2
        # 快速檢查
        if S < D or (S + D) % 2:
            out.append('impossible')
            continue
        a = (S + D) // 2
        b = (S - D) // 2
        if b < 0:
            out.append('impossible')
        else:
            out.append(f"{a} {b}")
    return out

if __name__ == '__main__':
    for l in solve():
        print(l)

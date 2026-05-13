"""
10908 — 手寫版（含中文註解）
較可讀的實作，供測試使用。
"""
import sys

def solve(lines=None):
    if lines is None:
        tokens = sys.stdin.read().strip().split()
    else:
        tokens = "\n".join(lines).strip().split()
    if not tokens:
        return []
    idx = 0
    T = int(tokens[idx]); idx += 1
    results = []
    for _ in range(T):
        M = int(tokens[idx]); N = int(tokens[idx+1]); Q = int(tokens[idx+2]); idx += 3
        grid = []
        for _ in range(M):
            grid.append(list(tokens[idx])); idx += 1
        results.append(f"{M} {N} {Q}")
        for _ in range(Q):
            r = int(tokens[idx]); c = int(tokens[idx+1]); idx += 2
            center = grid[r][c]
            max_layer = 0
            # 從 layer = 0 開始嘗試，layer 對應邊長 = 2*layer+1
            layer = 0
            while True:
                top = r - layer
                left = c - layer
                bottom = r + layer
                right = c + layer
                # 若超出邊界，停止
                if top < 0 or left < 0 or bottom >= M or right >= N:
                    break
                ok = True
                for i in range(top, bottom+1):
                    for j in range(left, right+1):
                        if grid[i][j] != center:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    break
                max_layer = layer
                layer += 1
            side = 2*max_layer + 1
            results.append(str(side))
    return results

if __name__ == '__main__':
    for line in solve():
        print(line)

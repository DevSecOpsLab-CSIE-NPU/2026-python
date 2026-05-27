"""
UVA 10908 — Largest Square
標準版解法，包含詳細邊界檢查與說明。
"""

def solve(in_stream, out_stream):
    # 讀取測資組數
    T = int(in_stream.readline())
    for _ in range(T):
        # 每組：M, N, Q
        M, N, Q = map(int, in_stream.readline().split())
        grid = [in_stream.readline().strip() for _ in range(M)]
        queries = [tuple(map(int, in_stream.readline().split())) for _ in range(Q)]

        # 輸出每組測資開頭
        out_stream.write(f"{M} {N} {Q}\n")
        for r, c in queries:
            char = grid[r][c]  # 查詢中心字元
            max_radius = 0
            while True:
                # 正方形半徑 k，邊長 = 2 * k + 1
                top, bottom = r - max_radius, r + max_radius
                left, right = c - max_radius, c + max_radius
                # 檢查是否超出邊界
                if not (0 <= top and bottom < M and 0 <= left and right < N):
                    break
                # 邊界是否全為目標字元
                ok = True
                for i in range(left, right+1):
                    if grid[top][i] != char or grid[bottom][i] != char:
                        ok = False
                        break
                for i in range(top+1, bottom):
                    if grid[i][left] != char or grid[i][right] != char:
                        ok = False
                        break
                if not ok:
                    break
                max_radius += 1  # 可再擴大半徑
            out_stream.write(f"{2*max_radius-1}\n")

if __name__ == "__main__":
    import sys
    solve(sys.stdin, sys.stdout)

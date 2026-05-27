"""
UVA 10908 — Largest Square
直覺易懂版，附詳細註釋：
此題主要核心是「不斷嘗試把正方形往外擴張」，每次判斷是否越界或邊框有不同字元。
"""

def solve(in_stream, out_stream):
    # 讀取 Test Case 數量
    T = int(in_stream.readline())
    for _ in range(T):
        # 解析本組測資的矩陣高 M，寬 N，查詢數量 Q
        M, N, Q = map(int, in_stream.readline().split())
        # 讀入字元矩陣
        grid = [in_stream.readline().strip() for _ in range(M)]
        # 讀入所有查詢點（row,col）
        queries = [tuple(map(int, in_stream.readline().split())) for _ in range(Q)]

        # 先印出這組測資的開頭行：M N Q
        out_stream.write(f"{M} {N} {Q}\n")

        for r, c in queries:
            ch = grid[r][c]  # 紀錄中心字元
            d = 0  # d 代表正方形中心到邊的距離（半徑），起始只能是1x1
            while True:
                # 預計擴張一圈，計算新邊界值
                top, bot = r - d, r + d
                left, right = c - d, c + d
                # 若有一個方向超出邊界就結束（無法再擴張）
                if top < 0 or bot >= M or left < 0 or right >= N:
                    break
                # 上下邊都必須全為中心字元
                has_diff = False
                for j in range(left, right + 1):
                    if grid[top][j] != ch or grid[bot][j] != ch:
                        has_diff = True
                        break
                if has_diff:
                    break
                # 左右邊也要全為中心字元（注意不重疊 corners）
                for i in range(top + 1, bot):
                    if grid[i][left] != ch or grid[i][right] != ch:
                        has_diff = True
                        break
                if has_diff:
                    break
                # 若都沒遇到不一樣就嘗試更大一階
                d += 1
            # 最後最大邊長= 2d-1
            out_stream.write(f"{2*d-1}\n")

if __name__ == "__main__":
    import sys
    solve(sys.stdin, sys.stdout)

def solve(in_stream, out_stream):
    T = int(in_stream.readline())
    for _ in range(T):
        M, N, Q = map(int, in_stream.readline().split())
        grid = [in_stream.readline().strip() for _ in range(M)]
        queries = [tuple(map(int, in_stream.readline().split())) for _ in range(Q)]
        out_stream.write(f"{M} {N} {Q}\n")
        for r, c in queries:
            ch = grid[r][c]
            d = 0  # half size
            while True:
                top, bot = r - d, r + d
                left, right = c - d, c + d
                if top < 0 or bot >= M or left < 0 or right >= N:
                    break
                if any(grid[top][j] != ch or grid[bot][j] != ch for j in range(left, right+1)):
                    break
                if any(grid[i][left] != ch or grid[i][right] != ch for i in range(top+1, bot)):
                    break
                d += 1
            out_stream.write(f"{d*2-1}\n")

if __name__ == "__main__":
    import sys
    solve(sys.stdin, sys.stdout)

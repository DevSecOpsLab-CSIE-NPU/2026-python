import sys
def solve():
    data = sys.stdin.read().split()
    if not data: return
    idx = 1
    for _ in range(int(data[0])):
        m, n, q = map(int, data[idx:idx+3]); idx += 3
        grid = data[idx:idx+m]; idx += m
        print(f"{m} {n} {q}")
        for _ in range(q):
            r, c = map(int, data[idx:idx+2]); idx += 2
            char, side = grid[r][c], 1
            while True:
                k = (side + 1) // 2
                rs, re, cs, ce = r-k, r+k, c-k, c+k
                if rs<0 or re>=m or cs<0 or ce>=n: break
                if any(grid[rs][j]!=char or grid[re][j]!=char for j in range(cs, ce+1)) or \
                   any(grid[i][cs]!=char or grid[i][ce]!=char for i in range(rs, re+1)): break
                side += 2
            print(side)
if __name__ == "__main__":
    solve()

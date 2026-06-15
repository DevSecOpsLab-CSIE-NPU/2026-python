import sys

def solve():
    field_num = 1
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        m = int(input_data[idx+1])
        idx += 2

        if n == 0 and m == 0:
            break

        grid = []
        for _ in range(n):
            grid.append(list(input_data[idx]))
            idx += 1

        res = [[0 for _ in range(m)] for _ in range(n)]

        for r in range(n):
            for c in range(m):
                if grid[r][c] == '*':
                    res[r][c] = '*'
                else:
                    count = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0: continue
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '*':
                                count += 1
                    res[r][c] = str(count)

        if field_num > 1:
            print()
        print(f"Field #{field_num}:")
        for row in res:
            print("".join(row))
        field_num += 1

if __name__ == "__main__":
    solve()

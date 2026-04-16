case = 0

while True:
    line = input().split()
    n, m = int(line[0]), int(line[1])
    if n == 0 and m == 0:
        break

    grid = []
    for _ in range(n):
        grid.append(input())

    case += 1
    if case > 1:
        print()
    print(f"Field #{case}:")

    for i in range(n):
        row = ""
        for j in range(m):
            if grid[i][j] == '*':
                row += '*'
            else:
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '*':
                            count += 1
                row += str(count)
        print(row)

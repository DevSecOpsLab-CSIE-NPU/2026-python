import sys

def main():
    field_num = 1
    lines = sys.stdin.readlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        i += 1
        if not line:
            continue
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break
        grid = []
        for _ in range(n):
            row = list(lines[i].strip())
            grid.append(row)
            i += 1
        
        # Process the grid
        result = []
        for x in range(n):
            new_row = []
            for y in range(m):
                if grid[x][y] == '*':
                    new_row.append('*')
                else:
                    count = 0
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if di == 0 and dj == 0:
                                continue
                            ni, nj = x + di, y + dj
                            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '*':
                                count += 1
                    new_row.append(str(count))
            result.append(''.join(new_row))
        
        print(f"Field #{field_num}:")
        for row in result:
            print(row)
        print()
        field_num += 1

if __name__ == "__main__":
    main()
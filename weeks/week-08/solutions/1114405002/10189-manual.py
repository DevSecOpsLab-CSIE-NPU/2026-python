# 手打版 Minesweeper 程式
# 手動輸入處理

def main():
    field_num = 1
    while True:
        try:
            line = input().strip()
            if not line:
                continue
            n, m = map(int, line.split())
            if n == 0 and m == 0:
                break
            grid = []
            for _ in range(n):
                row = list(input().strip())
                grid.append(row)
            
            # 處理網格
            result = []
            for i in range(n):
                new_row = []
                for j in range(m):
                    if grid[i][j] == '*':
                        new_row.append('*')
                    else:
                        count = 0
                        for di in [-1, 0, 1]:
                            for dj in [-1, 0, 1]:
                                if di == 0 and dj == 0:
                                    continue
                                ni, nj = i + di, j + dj
                                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '*':
                                    count += 1
                        new_row.append(str(count))
                result.append(''.join(new_row))
            
            print(f"Field #{field_num}:")
            for row in result:
                print(row)
            print()
            field_num += 1
        except EOFError:
            break

if __name__ == "__main__":
    main()
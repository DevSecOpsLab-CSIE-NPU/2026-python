import sys

def solve(n, m, grid):
    padded_grid = ['.' * (m + 2)]
    for row in grid:
        padded_grid.append('.' + row + '.')
    padded_grid.append('.' * (m + 2))
    
    result = []
    for i in range(1, n + 1):
        row_result = ""
        for j in range(1, m + 1):
            if padded_grid[i][j] == '*':
                row_result += '*'
            else:
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if padded_grid[i+dx][j+dy] == '*':
                            count += 1
                row_result += str(count)
        result.append(row_result)
    return result

if __name__ == '__main__':
    data = sys.stdin.read().split()
    idx = 0; field_num = 1
    
    while idx < len(data):
        n, m = int(data[idx]), int(data[idx+1])
        idx += 2
        if n == 0 and m == 0: break
        grid = data[idx : idx+n]; idx += n
        if field_num > 1: print()
        print(f"Field #{field_num}:\n" + '\n'.join(solve(n, m, grid)))
        field_num += 1
import sys

def get_max_square(grid, m, n, r, c):
    char = grid[r][c]
    side = 1
    offset = 1
    
    while True:
        r1, r2 = r - offset, r + offset
        c1, c2 = c - offset, c + offset
        
        if r1 < 0 or r2 >= m or c1 < 0 or c2 >= n:
            break
            
        is_square = True
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if grid[i][j] != char:
                    is_square = False
                    break
            if not is_square:
                break
        
        if is_square:
            side = 2 * offset + 1
            offset += 1
        else:
            break
    return side

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    try:
        t = int(input_data[idx])
        idx += 1
    except (ValueError, IndexError):
        return
    
    for _ in range(t):
        try:
            m = int(input_data[idx])
            n = int(input_data[idx+1])
            q = int(input_data[idx+2])
            idx += 3
        except (ValueError, IndexError):
            break
        
        print(f"{m} {n} {q}")
        
        grid = []
        for i in range(m):
            grid.append(input_data[idx])
            idx += 1
            
        for i in range(q):
            try:
                r = int(input_data[idx])
                c = int(input_data[idx+1])
                idx += 2
                print(get_max_square(grid, m, n, r, c))
            except (ValueError, IndexError):
                break

if __name__ == "__main__":
    main()

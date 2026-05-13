import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        m = int(input_data[idx])
        n = int(input_data[idx+1])
        q = int(input_data[idx+2])
        idx += 3
        
        grid = []
        for i in range(m):
            grid.append(input_data[idx])
            idx += 1
            
        print(f"{m} {n} {q}")
        
        for _ in range(q):
            r = int(input_data[idx])
            c = int(input_data[idx+1])
            idx += 2
            
            char = grid[r][c]
            max_side = 1
            
            k = 1
            while True:
                # Check square with side length 2k + 1
                r_start, r_end = r - k, r + k
                c_start, c_end = c - k, c + k
                
                if r_start < 0 or r_end >= m or c_start < 0 or c_end >= n:
                    break
                
                possible = True
                # Check the boundary of the new square
                for i in range(r_start, r_end + 1):
                    if grid[i][c_start] != char or grid[i][c_end] != char:
                        possible = False
                        break
                if not possible: break
                
                for j in range(c_start, c_end + 1):
                    if grid[r_start][j] != char or grid[r_end][j] != char:
                        possible = False
                        break
                if not possible: break
                
                max_side = 2 * k + 1
                k += 1
            
            print(max_side)

if __name__ == "__main__":
    solve()

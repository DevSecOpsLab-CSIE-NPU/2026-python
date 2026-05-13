import sys

# 優化版：使用一維陣列或更簡潔的邊界檢查邏輯
def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        m, n, q = map(int, input_data[idx:idx+3])
        idx += 3
        grid = input_data[idx:idx+m]
        idx += m
        print(f"{m} {n} {q}")
        
        for _ in range(q):
            r, c = map(int, input_data[idx:idx+2])
            idx += 2
            char = grid[r][c]
            side = 1
            # 檢查下一層 (邊長 side + 2)
            while True:
                k = (side + 1) // 2
                rs, re = r - k, r + k
                cs, ce = c - k, c + k
                if rs < 0 or re >= m or cs < 0 or ce >= n: break
                
                # 檢查四條邊
                valid = True
                if any(grid[rs][j] != char or grid[re][j] != char for j in range(cs, ce + 1)):
                    valid = False
                if valid and any(grid[i][cs] != char or grid[i][ce] != char for i in range(rs, re + 1)):
                    valid = False
                
                if not valid: break
                side += 2
            print(side)

if __name__ == "__main__":
    solve()

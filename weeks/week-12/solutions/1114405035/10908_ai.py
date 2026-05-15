import sys

def solve():
    # 讀取測試案例數 T
    line = sys.stdin.readline()
    if not line:
        return
    try:
        t_cases = int(line.strip())
    except ValueError:
        return
    
    for _ in range(t_cases):
        # 讀取 M, N, Q
        line = sys.stdin.readline()
        while line and not line.strip():
            line = sys.stdin.readline()
        if not line:
            break
        m, n, q = map(int, line.split())
        
        # 輸出第一行 M N Q
        print(f"{m} {n} {q}")
        
        # 讀取字元網格
        grid = []
        for _ in range(m):
            grid.append(sys.stdin.readline().strip())
        
        # 處理 Q 個查詢
        for _ in range(q):
            line = sys.stdin.readline()
            if not line:
                break
            r, c = map(int, line.split())
            
            char = grid[r][c]
            max_side = 1
            
            # 從邊長 3 開始嘗試擴展 (k = 3, 5, 7...)
            # 偏移量 offset = (k - 1) // 2
            offset = 1
            while True:
                # 檢查邊界
                if r - offset < 0 or r + offset >= m or c - offset < 0 or c + offset >= n:
                    break
                
                # 檢查正方形內的所有字元是否相同
                is_valid = True
                for i in range(r - offset, r + offset + 1):
                    for j in range(c - offset, c + offset + 1):
                        if grid[i][j] != char:
                            is_valid = False
                            break
                    if not is_valid:
                        break
                
                if is_valid:
                    max_side = 2 * offset + 1
                    offset += 1
                else:
                    break
            
            print(max_side)

if __name__ == "__main__":
    solve()

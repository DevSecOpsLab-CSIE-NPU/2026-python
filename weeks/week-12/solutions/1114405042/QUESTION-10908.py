def get_largest_square(grid, M, N, r, c):
    """
    找出以 (r, c) 為中心，且所有字元相同的最大正方形邊長。
    
    :param grid: List[str]，字元網格
    :param M: int，網格行數
    :param N: int，網格列數
    :param r: int，中心點列座標 (row)
    :param c: int，中心點行座標 (column)
    :return: int，最大正方形的邊長
    """
    # 檢查中心點是否在合法範圍內
    if r < 0 or r >= M or c < 0 or c >= N:
        return 0
    
    center_char = grid[r][c]
    radius = 0  # 初始半徑為 0，此時邊長為 2*0 + 1 = 1
    
    # 不斷向外擴張一層，檢查新的一層（外框）是否與中心點字元相同
    while True:
        next_radius = radius + 1
        
        # 1. 檢查外擴一層後是否超出網格邊界
        if r - next_radius < 0 or r + next_radius >= M or c - next_radius < 0 or c + next_radius >= N:
            break
            
        is_same = True
        
        # 2. 檢查上下兩條水平邊框
        for j in range(c - next_radius, c + next_radius + 1):
            if grid[r - next_radius][j] != center_char or grid[r + next_radius][j] != center_char:
                is_same = False
                break
                
        # 3. 如果上下邊框符合，繼續檢查左右兩條垂直邊框
        if is_same:
            for i in range(r - next_radius, r + next_radius + 1):
                if grid[i][c - next_radius] != center_char or grid[i][c + next_radius] != center_char:
                    is_same = False
                    break
        
        # 4. 如果這一層外框所有字元都相同，則半徑增加
        if is_same:
            radius = next_radius
        else:
            break # 只要有不同字元，就停止擴張
            
    # 正方形邊長公式：2 * 半徑 + 1
    return 2 * radius + 1

def solve():
    import sys
    # 讀取所有標準輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    T = int(input_data[0])
    idx = 1
    
    for _ in range(T):
        M = int(input_data[idx])
        N = int(input_data[idx+1])
        Q = int(input_data[idx+2])
        idx += 3
        
        # 印出該測資的 M N Q
        print(f"{M} {N} {Q}")
        
        # 讀取網格資料
        grid = []
        for _ in range(M):
            grid.append(input_data[idx])
            idx += 1
            
        # 讀取並處理每個查詢
        for _ in range(Q):
            r = int(input_data[idx])
            c = int(input_data[idx+1])
            idx += 2
            
            # 計算並輸出最大邊長
            ans = get_largest_square(grid, M, N, r, c)
            print(ans)

if __name__ == '__main__':
    solve()

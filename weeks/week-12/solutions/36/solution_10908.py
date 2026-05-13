# UVA 10908 - Largest Square
# 解題思路：
# 1. 給定網格和 Q 個查詢點
# 2. 對每個查詢點，找以該點為中心的最大正方形
# 3. 正方形必須所有字符相同，且邊長必須為奇數
# 4. 使用「向外擴展」的方法：從中心開始，逐漸擴大範圍直到無法擴展

def find_largest_square(grid, r, c):
    """
    找以 (r, c) 為中心的最大正方形邊長
    返回邊長值
    """
    M = len(grid)
    N = len(grid[0]) if M > 0 else 0
    
    # 中心字符
    center_char = grid[r][c]
    max_side_length = 1  # 至少是中心點本身
    
    # 嘗試擴大正方形的「半徑 radius」
    # 邊長 = 2*radius + 1
    radius = 1
    
    while True:
        # 檢查四個邊界是否在網格內
        top = r - radius
        bottom = r + radius
        left = c - radius
        right = c + radius
        
        if top < 0 or bottom >= M or left < 0 or right >= N:
            break
        
        # 檢查四個邊界上的所有字符是否都相同
        valid = True
        
        # 檢查上下邊界
        for j in range(left, right + 1):
            if grid[top][j] != center_char or grid[bottom][j] != center_char:
                valid = False
                break
        
        # 檢查左右邊界
        if valid:
            for i in range(top, bottom + 1):
                if grid[i][left] != center_char or grid[i][right] != center_char:
                    valid = False
                    break
        
        if valid:
            max_side_length = 2 * radius + 1
            radius += 1
        else:
            break
    
    return max_side_length

def solve_largest_square():
    """
    求解 Largest Square 問題
    """
    T = int(input())
    
    for _ in range(T):
        M, N, Q = map(int, input().split())
        
        # 讀取網格
        grid = []
        for i in range(M):
            grid.append(input().strip())
        
        # 輸出結果頭
        print(M, N, Q)
        
        # 處理每個查詢
        for _ in range(Q):
            r, c = map(int, input().split())
            result = find_largest_square(grid, r, c)
            print(result)

if __name__ == "__main__":
    solve_largest_square()

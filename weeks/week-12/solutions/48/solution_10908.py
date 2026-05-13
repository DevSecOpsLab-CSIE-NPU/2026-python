"""
UVA 10908 — Largest Square 解決方案
給定字元網格和中心點，找以該點為中心、所有字元相同的最大正方形邊長

算法解析：
- 正方形邊長必須為奇數 (1, 3, 5, ...)，因為中心點在正方形中心
- 從邊長 1 開始逐步增加，檢查是否所有字元都相同
- 檢查範圍：row 從 (center_r - k) 到 (center_r + k)
           col 從 (center_c - k) 到 (center_c + k)
"""


def find_largest_square_size(grid, center_r, center_c):
    """
    找最大同色正方形的邊長
    
    參數：
        grid (list): 字元網格
        center_r (int): 中心點的行座標
        center_c (int): 中心點的列座標
    
    返回：
        int: 最大正方形邊長
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # 中心點的字元
    center_char = grid[center_r][center_c]
    
    # 從最小邊長開始逐步增加
    # 邊長 k 表示距離中心點 k 個單位
    max_size = 1
    k = 1
    
    while True:
        # 檢查邊界是否超出網格
        if (center_r - k < 0 or center_r + k >= rows or
            center_c - k < 0 or center_c + k >= cols):
            break
        
        # 檢查正方形四個邊界是否都是相同字元
        valid = True
        
        # 檢查上下邊界
        for col in range(center_c - k, center_c + k + 1):
            if grid[center_r - k][col] != center_char:
                valid = False
                break
            if grid[center_r + k][col] != center_char:
                valid = False
                break
        
        # 檢查左右邊界
        if valid:
            for row in range(center_r - k, center_r + k + 1):
                if grid[row][center_c - k] != center_char:
                    valid = False
                    break
                if grid[row][center_c + k] != center_char:
                    valid = False
                    break
        
        if valid:
            max_size = 2 * k + 1
            k += 1
        else:
            break
    
    return max_size


def main():
    """主程式：讀取輸入並輸出結果"""
    t = int(input())
    for _ in range(t):
        m, n, q = map(int, input().split())
        grid = []
        for _ in range(m):
            grid.append(input().strip())
        
        print(f"{m} {n} {q}")
        
        for _ in range(q):
            r, c = map(int, input().split())
            print(find_largest_square_size(grid, r, c))


if __name__ == "__main__":
    main()

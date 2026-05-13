"""
題目 10908 - Largest Square（最大正方形）

題目敘述：
給定一個 M 行 N 列的字元網格，以及 Q 個查詢。
對於每個查詢，給定一個中心點座標 (r, c)，找出以該點為中心，
且所有字元相同的最大正方形的邊長。

注意：
- 網格左上角座標為 (0, 0)，右下角為 (M-1, N-1)
- 正方形的邊長必須為奇數（1, 3, 5, ...）
- 中心點需要恰好落在正方形的中心格上

解法思路：
1. 對於每個查詢點 (r, c)，從邊長 1 開始檢查
2. 逐次增加邊長（1, 3, 5, 7, ...）
3. 檢查邊長內的所有字元是否相同
4. 返回最後一個有效的邊長
5. 如果超出邊界，停止檢查
"""


def is_valid_square(grid, r, c, side_length):
    """
    檢查以 (r, c) 為中心、邊長為 side_length 的正方形是否所有字元相同。
    
    參數：
        grid (list): 字元網格
        r (int): 中心點的行座標
        c (int): 中心點的列座標
        side_length (int): 正方形的邊長（必須為奇數）
    
    返回：
        bool: 如果所有字元相同且在邊界內，返回 True；否則返回 False
    """
    # 計算正方形的偏移量（距離中心的距離）
    # 例如邊長為 3 時，offset = 1；邊長為 5 時，offset = 2
    offset = side_length // 2
    
    # 檢查邊界
    if (r - offset < 0 or r + offset >= len(grid) or
        c - offset < 0 or c + offset >= len(grid[0])):
        return False
    
    # 取得中心點的字元
    center_char = grid[r][c]
    
    # 檢查正方形範圍內的所有字元
    for i in range(r - offset, r + offset + 1):
        for j in range(c - offset, c + offset + 1):
            if grid[i][j] != center_char:
                return False
    
    return True


def find_largest_square(grid, r, c):
    """
    找出以 (r, c) 為中心的最大同字元正方形的邊長。
    
    參數：
        grid (list): 字元網格
        r (int): 中心點的行座標
        c (int): 中心點的列座標
    
    返回：
        int: 最大正方形的邊長
    """
    # 取得網格的行數和列數
    m = len(grid)
    n = len(grid[0]) if m > 0 else 0
    
    # 計算可能的最大邊長
    # 邊長受限於與邊界的最小距離
    max_possible_side = 2 * min(r, c, m - 1 - r, n - 1 - c) + 1
    
    # 從最大邊長開始向下檢查，找到最大的有效邊長
    for side in range(max_possible_side, 0, -2):
        if is_valid_square(grid, r, c, side):
            return side
    
    return 1  # 最小邊長為 1


def solve_largest_square(m, n, q, grid, queries):
    """
    解決最大正方形問題。
    
    參數：
        m (int): 網格的行數
        n (int): 網格的列數
        q (int): 查詢的數量
        grid (list): 字元網格
        queries (list): 查詢列表，每個查詢是 (r, c) 座標
    
    返回：
        list: 每個查詢的最大正方形邊長
    """
    results = []
    for r, c in queries:
        largest = find_largest_square(grid, r, c)
        results.append(largest)
    return results


def main():
    """
    主程式：讀取輸入並輸出結果。
    """
    # 讀取測試資料組數
    t = int(input())
    
    for _ in range(t):
        # 讀取網格的行數、列數和查詢數
        m, n, q = map(int, input().split())
        
        # 讀取字元網格
        grid = []
        for i in range(m):
            row = input().strip()
            grid.append(row)
        
        # 讀取查詢
        queries = []
        for i in range(q):
            r, c = map(int, input().split())
            queries.append((r, c))
        
        # 解決問題
        results = solve_largest_square(m, n, q, grid, queries)
        
        # 輸出結果
        print(f"{m} {n} {q}")
        for result in results:
            print(result)


if __name__ == "__main__":
    main()

"""
題目 10908 - Largest Square（簡易版本）

簡化版程式：只用兩個函數，邏輯清晰易懂

這個版本的特點：
1. 代碼簡短（約 60 行）
2. 只需記住 2 個函數
3. 從小到大逐次增大邊長
4. 邏輯直觀，容易除錯
"""


def is_valid(grid, r, c, size):
    """
    檢查以 (r, c) 為中心、邊長 size 的正方形是否有效。
    
    有效表示：
    1. 正方形完全在網格範圍內
    2. 正方形內所有字元都與中心字元相同
    
    參數：
        grid (list): 字元網格
        r (int): 中心點行座標
        c (int): 中心點列座標
        size (int): 正方形邊長（奇數）
    
    返回：
        bool: 如果有效返回 True，否則返回 False
    
    範例：
        grid = [['a', 'a', 'a'],
                ['a', 'a', 'a'],
                ['a', 'a', 'a']]
        is_valid(grid, 1, 1, 3) -> True
        is_valid(grid, 1, 1, 5) -> False（超出邊界）
    """
    # 計算從中心到邊的距離
    offset = size // 2
    
    # 檢查四個邊界是否超出網格範圍
    if r - offset < 0 or r + offset >= len(grid):
        return False
    if c - offset < 0 or c + offset >= len(grid[0]):
        return False
    
    # 獲取中心字元
    center_char = grid[r][c]
    
    # 檢查正方形內所有字元是否都相同
    for i in range(r - offset, r + offset + 1):
        for j in range(c - offset, c + offset + 1):
            if grid[i][j] != center_char:
                return False
    
    return True


def find_square(grid, r, c):
    """
    找出以 (r, c) 為中心的最大正方形邊長。
    
    演算法：
    從邊長 1 開始，逐次增大邊長（1, 3, 5, 7, ...）
    直到不再有效，返回最後一個有效的邊長。
    
    參數：
        grid (list): 字元網格
        r (int): 中心點行座標
        c (int): 中心點列座標
    
    返回：
        int: 最大正方形的邊長
    
    時間複雜度：
        最壞情況 O(min(M,N)³)
        但實際上通常很快，因為大多數網格不會全部相同
    
    範例：
        假設中心是 'a'，且周圍都是 'a'
        • 檢查邊長 1：有效 → size = 1
        • 檢查邊長 3：有效 → size = 3
        • 檢查邊長 5：有效 → size = 5
        • 檢查邊長 7：無效 → 返回 5
    """
    size = 1  # 至少邊長為 1（中心點本身）
    
    # 一直增大邊長，直到下一個邊長不再有效
    while is_valid(grid, r, c, size + 2):
        size += 2  # 邊長 +2 保證奇數（1, 3, 5, 7, ...）
    
    return size


def main():
    """
    主程式：讀取輸入，處理查詢，輸出結果。
    
    輸入格式：
    - 第一行：測試資料組數 T
    - 對於每組測試資料：
      - 第一行：M N Q（行數 列數 查詢數）
      - 接下來 M 行：字元網格
      - 接下來 Q 行：查詢點座標 r c
    
    輸出格式：
    - 對於每組測試資料：
      - 第一行：M N Q
      - 接下來 Q 行：各查詢的答案（最大正方形邊長）
    """
    # 讀取測試資料組數
    T = int(input())
    
    # 處理每組測試資料
    for _ in range(T):
        # 讀取網格的行數、列數、查詢數
        m, n, q = map(int, input().split())
        
        # 讀取字元網格（每行是一個字元串）
        grid = []
        for _ in range(m):
            row = input().strip()  # 讀取並去除換行符
            grid.append(list(row))  # 轉換為字元列表
        
        # 輸出頭行（M N Q）
        print(m, n, q)
        
        # 處理每個查詢
        for _ in range(q):
            r, c = map(int, input().split())  # 讀取查詢點座標
            result = find_square(grid, r, c)  # 計算最大邊長
            print(result)  # 輸出結果


if __name__ == "__main__":
    main()

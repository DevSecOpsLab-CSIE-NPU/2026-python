# ============================================================
# UVA 10908 - Largest Square (簡單版本)
# 
# 【題目核心】
# 給定字元網格和查詢點，找以該點為中心的最大正方形
# 正方形：
#   - 中心必須在 (r, c)
#   - 所有字符必須相同
#   - 邊長必須為奇數（1, 3, 5, ...）
# 
# 【演算法思想】『向外擴展法』
# 1. 初始化邊長為 1（只有中心點）
# 2. 嘗試向外擴展，每次增加「半徑 radius」
# 3. 檢查 4 個邊界的所有字符是否都相同
# 4. 若相同則繼續擴展，若不同則停止
# 5. 邊長 = 2*radius + 1
# ============================================================

def find_max_square(grid, r, c):
    """
    【函數功能】找以 (r, c) 為中心的最大正方形邊長
    
    【參數說明】
    - grid: 字元網格（二維列表）
    - r: 查詢點行號（0-based）
    - c: 查詢點列號（0-based）
    
    【返回值】最大正方形邊長
    """
    
    # 獲取網格的行數和列數
    m, n = len(grid), len(grid[0])
    
    # 獲取中心點的字符
    ch = grid[r][c]
    
    # 初始化邊長為 1
    size = 1
    
    # 【擴展迴圈】嘗試逐漸增大正方形
    for radius in range(1, max(m, n)):
        # 計算四個邊界的座標
        t = r - radius      # 上邊界
        b = r + radius      # 下邊界
        l = c - radius      # 左邊界
        right = c + radius  # 右邊界
        
        # 【邊界檢查】檢查是否超出網格範圍
        if t < 0 or b >= m or l < 0 or right >= n:
            break
        
        # 【字符檢查】檢查上下邊界的所有字符
        ok = True
        for j in range(l, right + 1):
            if grid[t][j] != ch or grid[b][j] != ch:
                ok = False
        
        # 【字符檢查】檢查左右邊界的所有字符
        for i in range(t, b + 1):
            if grid[i][l] != ch or grid[i][right] != ch:
                ok = False
        
        # 【擴展決策】若所有邊界字符相同則繼續，否則停止
        if ok:
            size = 2 * radius + 1
        else:
            break
    
    return size


# ============================================================
# 【主程式】
# ============================================================

# 讀取測試資料組數
t = int(input())

# 處理每組測試資料
for _ in range(t):
    # 讀取網格行數、列數、查詢次數
    m, n, q = map(int, input().split())
    
    # 讀取 m 行網格資料
    grid = [input().strip() for _ in range(m)]
    
    # 輸出頭部資訊
    print(m, n, q)
    
    # 【查詢迴圈】處理每個查詢
    for _ in range(q):
        # 讀取查詢點座標
        r, c = map(int, input().split())
        
        # 計算並輸出結果
        print(find_max_square(grid, r, c))

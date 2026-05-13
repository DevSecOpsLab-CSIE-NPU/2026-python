"""
UVA 10908 — Largest Square 簡單版本
更簡單易記的寫法

核心思想：
- 從小到大逐步測試邊長
- 每次邊長加2（保證奇數）
- 檢查四個邊界是否都是相同字元
"""


def find_square_simple(grid, r, c):
    """
    最簡單的解法
    
    簡化概念：
    - size = 距離中心的格子數（0表示只有中心點）
    - 邊長 = 2 * size + 1
    """
    center_char = grid[r][c]
    rows = len(grid)
    cols = len(grid[0])
    
    # 逐步增加距離
    size = 0
    while True:
        # 檢查是否超出邊界
        if r - size - 1 < 0 or r + size + 1 >= rows:
            break
        if c - size - 1 < 0 or c + size + 1 >= cols:
            break
        
        size += 1
        
        # 檢查新的邊界是否都是相同字元
        valid = True
        # 上下邊
        for col in range(c - size, c + size + 1):
            if grid[r - size][col] != center_char or grid[r + size][col] != center_char:
                valid = False
                break
        # 左右邊
        if valid:
            for row in range(r - size, r + size + 1):
                if grid[row][c - size] != center_char or grid[row][c + size] != center_char:
                    valid = False
                    break
        
        if not valid:
            size -= 1
            break
    
    return 2 * size + 1


# 測試
if __name__ == "__main__":
    grid = [
        "abbbaaaaaa",
        "abbbaaaaaa",
        "abbbaaaaaa",
        "aaaaaaaaaa",
        "aaaaaaaaaa",
        "aaccaaaaaa",
        "aaccaaaaaa"
    ]
    print(find_square_simple(grid, 1, 2))  # 3
    print(find_square_simple(grid, 4, 6))  # 5

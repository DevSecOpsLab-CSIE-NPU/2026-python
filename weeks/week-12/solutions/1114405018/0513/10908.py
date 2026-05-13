"""
UVA 10908 — Largest Square

題意重點：
給定一個字元網格，以及多個查詢點。
每個查詢點都是正方形的中心，要求找出「以該點為中心」且「所有字元都相同」的最大奇數邊長正方形。

這題的核心想法很直接：
1. 先確認中心點本身是哪個字元。
2. 從邊長 1 開始往外擴張，每次多擴一圈就會得到邊長 +2 的正方形。
3. 只要新擴張的外框四邊都還是同一個字元，就可以繼續往外擴。
4. 一旦有任一格不同或超出邊界，就停止，前一個邊長就是答案。

因為 M、N 最大只有 100，Q 也不多，所以用這種逐層擴張的做法很簡單也夠快。
"""


def largest_square(grid, row, col):
    """
    計算以 (row, col) 為中心的最大相同字元正方形邊長。

    參數：
        grid: 二維字元陣列
        row: 查詢點列座標
        col: 查詢點行座標

    回傳：
        最大奇數邊長（至少為 1）
    """
    rows = len(grid)
    cols = len(grid[0])
    target = grid[row][col]

    # 邊長從 1 開始，代表只看中心點自己。
    size = 1

    # half 代表目前正方形往上下左右各延伸了幾格。
    # size = 2 * half + 1
    half = 1

    while True:
        top = row - half
        bottom = row + half
        left = col - half
        right = col + half

        # 只要超出邊界，就不能再擴張。
        if top < 0 or bottom >= rows or left < 0 or right >= cols:
            break

        # 檢查新擴出來的外框：上、下兩條邊。
        valid = True

        for current_col in range(left, right + 1):
            if grid[top][current_col] != target or grid[bottom][current_col] != target:
                valid = False
                break

        # 如果上下邊通過，再檢查左右兩條邊。
        if valid:
            for current_row in range(top, bottom + 1):
                if grid[current_row][left] != target or grid[current_row][right] != target:
                    valid = False
                    break

        # 若外框仍然全部相同，就把邊長更新成更大的奇數。
        if not valid:
            break

        size += 2
        half += 1

    return size


def main():
    """主程式：讀取多筆測資並輸出答案。"""
    test_cases = int(input())

    for _ in range(test_cases):
        rows, cols, queries = map(int, input().split())

        grid = []
        for _ in range(rows):
            grid.append(list(input().strip()))

        # 題目要求每組測資先輸出 M N Q。
        print(f"{rows} {cols} {queries}")

        for _ in range(queries):
            row, col = map(int, input().split())
            print(largest_square(grid, row, col))


if __name__ == "__main__":
    main()
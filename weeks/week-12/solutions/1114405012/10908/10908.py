import sys


def largest_square(grid: list[str], row: int, col: int) -> int:
    # 先把中心點的字元記起來，之後擴張時都要維持同一個字元。
    target = grid[row][col]
    radius = 0
    height = len(grid)
    width = len(grid[0])

    # 半徑 0 代表只看中心點本身，邊長是 1。
    while True:
        next_radius = radius + 1
        top = row - next_radius
        bottom = row + next_radius
        left = col - next_radius
        right = col + next_radius

        # 如果新正方形已經超出邊界，就不能再擴大。
        if top < 0 or left < 0 or bottom >= height or right >= width:
            break

        valid = True
        # 直接檢查新正方形中的所有格子，確定字元都一樣。
        for r in range(top, bottom + 1):
            for c in range(left, right + 1):
                if grid[r][c] != target:
                    valid = False
                    break
            if not valid:
                break

        if not valid:
            break

        radius = next_radius

    # 邊長一定是奇數，所以回傳 2 * radius + 1。
    return radius * 2 + 1


def solve() -> None:
    # 先把所有輸入切成 token，處理多組測資時會很方便。
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    index = 0
    test_count = int(data[index])
    index += 1
    answers = []

    for _ in range(test_count):
        # 每組測資先讀 M、N、Q。
        rows = int(data[index])
        cols = int(data[index + 1])
        query_count = int(data[index + 2])
        index += 3

        # 讀入字元網格，每一行都是一整串字元。
        grid = [data[index + i].decode() for i in range(rows)]
        index += rows

        # 先輸出題目要求的標頭列。
        answers.append(f"{rows} {cols} {query_count}")

        # 再逐一處理查詢座標。
        for _ in range(query_count):
            row = int(data[index])
            col = int(data[index + 1])
            index += 2
            answers.append(str(largest_square(grid, row, col)))

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    solve()
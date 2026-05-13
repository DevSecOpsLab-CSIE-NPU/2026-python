import sys


def can_make_square(grid, center_row, center_col, radius, target_char):
    # 先算出目前這個正方形的上下左右邊界。
    top = center_row - radius
    bottom = center_row + radius
    left = center_col - radius
    right = center_col + radius

    # 如果邊界超出矩陣，就不能再往外擴大。
    if top < 0 or left < 0 or bottom >= len(grid) or right >= len(grid[0]):
        return False

    # 逐格檢查這個正方形內的每一個字元是否都相同。
    for row_index in range(top, bottom + 1):
        row = grid[row_index]
        for col_index in range(left, right + 1):
            if row[col_index] != target_char:
                return False

    return True


def solve():
    # 題目資料量很小，直接把所有 token 讀進來最方便。
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    iterator = iter(tokens)
    test_count = int(next(iterator))
    output = []

    for _ in range(test_count):
        m = int(next(iterator))
        n = int(next(iterator))
        q = int(next(iterator))

        # 網格每一列都是一個字串，存起來之後查詢時直接取字元即可。
        grid = [next(iterator) for _ in range(m)]
        output.append(f"{m} {n} {q}")

        for _ in range(q):
            r = int(next(iterator))
            c = int(next(iterator))

            # 以查詢點為中心，從邊長 1 的正方形開始，一層一層往外擴大。
            target_char = grid[r][c]
            radius = 0

            while can_make_square(grid, r, c, radius, target_char):
                radius += 1

            # radius 會多加 1 次，所以真正的邊長要減回來。
            output.append(str(radius * 2 - 1))

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()
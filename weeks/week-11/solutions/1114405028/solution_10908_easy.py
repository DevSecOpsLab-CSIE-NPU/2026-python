"""UVA 10908 — Largest Square 簡單版本"""


def find_square_simple(grid, r, c):
    """最簡單的解法"""
    center_char = grid[r][c]
    rows = len(grid)
    cols = len(grid[0])

    size = 0
    while True:
        if r - size - 1 < 0 or r + size + 1 >= rows:
            break
        if c - size - 1 < 0 or c + size + 1 >= cols:
            break

        size += 1

        valid = True
        for col in range(c - size, c + size + 1):
            if grid[r - size][col] != center_char or grid[r + size][col] != center_char:
                valid = False
                break

        if valid:
            for row in range(r - size, r + size + 1):
                if grid[row][c - size] != center_char or grid[row][c + size] != center_char:
                    valid = False
                    break

        if not valid:
            size -= 1
            break

    return 2 * size + 1


if __name__ == "__main__":
    grid = [
        "abbbaaaaaa",
        "abbbaaaaaa",
        "abbbaaaaaa",
        "aaaaaaaaaa",
        "aaaaaaaaaa",
        "aaccaaaaaa",
        "aaccaaaaaa",
    ]
    print(find_square_simple(grid, 1, 2))  # 3
    print(find_square_simple(grid, 4, 6))  # 5

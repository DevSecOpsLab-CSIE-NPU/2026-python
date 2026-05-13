def largest_square(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    target = grid[row][col]

    answer = 1

    while True:
        top = row - half
        bottom = row + half
        left = col - half
        right = col + half

        if top < 0 or bottom >= rows or left < 0 or right >= cols:
            break

        ok = True

        for current_row in range(top, bottom + 1):
            for current_col in range(left, right + 1):
                if grid[current_row][current_col] != target:
                    ok = False
                    break
            if not ok:
                break

        if not ok:
            break

        answer += 2
        half += 1

    return answer
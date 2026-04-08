import sys


def valid_row_masks(m: int, terrain_mask: int) -> list[int]:
    masks: list[int] = []
    for mask in range(1 << m):
        if mask & terrain_mask != mask:
            continue
        if mask & (mask << 1):
            continue
        if mask & (mask << 2):
            continue
        masks.append(mask)
    return masks


def max_artillery(grid: list[str]) -> int:
    if not grid:
        return 0

    n = len(grid)
    m = len(grid[0])
    row_masks: list[list[int]] = []
    for row in grid:
        terrain_mask = 0
        for j, ch in enumerate(row):
            if ch == "P":
                terrain_mask |= 1 << j
        row_masks.append(valid_row_masks(m, terrain_mask))

    dp = {(0, 0): 0}
    for masks in row_masks:
        next_dp: dict[tuple[int, int], int] = {}
        for (prev_mask, prev2_mask), value in dp.items():
            for mask in masks:
                if mask & prev_mask:
                    continue
                if mask & prev2_mask:
                    continue
                key = (mask, prev_mask)
                candidate = value + mask.bit_count()
                if candidate > next_dp.get(key, 0):
                    next_dp[key] = candidate
        dp = next_dp

    return max(dp.values(), default=0)


def solve() -> int:
    data = sys.stdin.read().strip().split()
    if not data:
        return 0

    n = int(data[0])
    m = int(data[1])
    grid = data[2:2 + n]
    return max_artillery(grid)


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()

from __future__ import annotations

from collections import defaultdict
import sys


MOD = 1_000_000_007


def count_placements(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    left_bit = 1 << cols
    dp: dict[int, int] = {0: 1}

    for row in range(rows):
        current_row = grid[row]
        next_row = grid[row + 1] if row + 1 < rows else None

        for col in range(cols):
            next_dp: defaultdict[int, int] = defaultdict(int)
            cell_open = current_row[col] == 1
            can_extend_right = col + 1 < cols and current_row[col + 1] == 1
            can_extend_down = next_row is not None and next_row[col] == 1
            down_bit = 1 << col

            for state, ways in dp.items():
                up = (state >> col) & 1
                left = (state >> cols) & 1

                if not cell_open:
                    if up or left:
                        continue
                    cleared_state = state & ~left_bit
                    next_dp[cleared_state] = (next_dp[cleared_state] + ways) % MOD
                    continue

                for right in (0, 1):
                    if right and not can_extend_right:
                        continue
                    for down in (0, 1):
                        if down and not can_extend_down:
                            continue
                        if up + left + right + down != 2:
                            continue

                        new_state = state & ~left_bit & ~down_bit
                        if right:
                            new_state |= left_bit
                        if down:
                            new_state |= down_bit
                        next_dp[new_state] = (next_dp[new_state] + ways) % MOD

            dp = next_dp

        dp = {state: ways for state, ways in dp.items() if (state & left_bit) == 0}

    return dp.get(0, 0)


def solve(data: str) -> str:
    tokens = data.split()
    pointer = 0
    case_count = int(tokens[pointer])
    pointer += 1
    outputs: list[str] = []

    for case_index in range(1, case_count + 1):
        rows = int(tokens[pointer])
        cols = int(tokens[pointer + 1])
        pointer += 2

        grid = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                grid[row][col] = int(tokens[pointer])
                pointer += 1

        outputs.append(f"Case {case_index}: {count_placements(grid)}")

    return "\n".join(outputs)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
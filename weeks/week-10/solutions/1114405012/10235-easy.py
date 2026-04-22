from __future__ import annotations

import sys
from collections import defaultdict


MOD = 1_000_000_007


def normalize(state: tuple[int, ...], left: int) -> tuple[tuple[int, ...], int]:
    # 重新編號，讓同一個結構的狀態可以合併在一起。
    mapping: dict[int, int] = {}
    next_label = 1
    normalized_state = []

    for label in state:
        if label == 0:
            normalized_state.append(0)
            continue
        if label not in mapping:
            mapping[label] = next_label
            next_label += 1
        normalized_state.append(mapping[label])

    normalized_left = 0
    if left != 0:
        if left not in mapping:
            mapping[left] = next_label
            next_label += 1
        normalized_left = mapping[left]

    return tuple(normalized_state), normalized_left


def solve_case(grid: list[list[int]]) -> int:
    row_count = len(grid)
    column_count = len(grid[0])

    # state 代表每一欄往下延伸的線段標記。
    dp: dict[tuple[tuple[int, ...], int], int] = {((0,) * column_count, 0): 1}

    for row in range(row_count):
        for column in range(column_count):
            next_dp: dict[tuple[tuple[int, ...], int], int] = defaultdict(int)
            blocked = grid[row][column] == 0

            for (state, left), count in dp.items():
                up = state[column]

                # 插座格不能被佔據，所以左上兩邊都必須空。
                if blocked:
                    if up == 0 and left == 0:
                        next_state = list(state)
                        next_state[column] = 0
                        key = normalize(tuple(next_state), 0)
                        next_dp[key] = (next_dp[key] + count) % MOD
                    continue

                # 左、上都沒進來，這格就必須同時往右與往下延伸。
                if up == 0 and left == 0:
                    if row + 1 < row_count and column + 1 < column_count:
                        new_label = max(max(state), left) + 1
                        next_state = list(state)
                        next_state[column] = new_label
                        key = normalize(tuple(next_state), new_label)
                        next_dp[key] = (next_dp[key] + count) % MOD
                    continue

                # 只有上面有線，這格要接成一條直線，往右或往下都可以。
                if up != 0 and left == 0:
                    if row + 1 < row_count:
                        next_state = list(state)
                        next_state[column] = up
                        key = normalize(tuple(next_state), 0)
                        next_dp[key] = (next_dp[key] + count) % MOD
                    if column + 1 < column_count:
                        next_state = list(state)
                        next_state[column] = 0
                        key = normalize(tuple(next_state), up)
                        next_dp[key] = (next_dp[key] + count) % MOD
                    continue

                # 只有左邊有線，處理方式和上面類似。
                if up == 0 and left != 0:
                    if row + 1 < row_count:
                        next_state = list(state)
                        next_state[column] = left
                        key = normalize(tuple(next_state), 0)
                        next_dp[key] = (next_dp[key] + count) % MOD
                    if column + 1 < column_count:
                        next_state = list(state)
                        next_state[column] = 0
                        key = normalize(tuple(next_state), left)
                        next_dp[key] = (next_dp[key] + count) % MOD
                    continue

                # 左右上下都已經各有一條線，這格就負責把兩條線接起來。
                next_state = list(state)
                next_state[column] = 0
                if up != left:
                    keep = min(up, left)
                    drop = max(up, left)
                    next_state = [keep if label == drop else label for label in next_state]
                key = normalize(tuple(next_state), 0)
                next_dp[key] = (next_dp[key] + count) % MOD

            dp = next_dp

        cleaned: dict[tuple[tuple[int, ...], int], int] = defaultdict(int)
        for (state, left), count in dp.items():
            if left != 0:
                continue
            key = normalize(state, 0)
            cleaned[key] = (cleaned[key] + count) % MOD
        dp = cleaned

    return dp.get(((0,) * column_count, 0), 0) % MOD


def main() -> None:
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    index = 0
    outputs: list[str] = []
    while index < len(tokens):
        test_case_count = tokens[index]
        index += 1
        if test_case_count == 0:
            break
        for case_index in range(test_case_count):
            row_count = tokens[index]
            column_count = tokens[index + 1]
            index += 2
            grid = []
            for _ in range(row_count):
                row = tokens[index:index + column_count]
                index += column_count
                grid.append(row)
            outputs.append(f"Case {case_index + 1}: {solve_case(grid)}")
        break
    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()
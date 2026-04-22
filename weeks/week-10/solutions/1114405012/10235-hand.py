from __future__ import annotations

import sys
from collections import defaultdict


MOD = 1_000_000_007


def normalize(state: tuple[int, ...], left: int) -> tuple[tuple[int, ...], int]:
    # 重新編號，讓同構狀態能合併。
    mapping: dict[int, int] = {}
    nxt = 1
    new_state = []

    for label in state:
        if label == 0:
            new_state.append(0)
            continue
        if label not in mapping:
            mapping[label] = nxt
            nxt += 1
        new_state.append(mapping[label])

    new_left = 0
    if left != 0:
        if left not in mapping:
            mapping[left] = nxt
        new_left = mapping[left]

    return tuple(new_state), new_left


def solve_case(grid: list[list[int]]) -> int:
    r = len(grid)
    c = len(grid[0])

    # 狀態 = 每欄向下連接標記 + 當前格左邊連接標記。
    dp: dict[tuple[tuple[int, ...], int], int] = {((0,) * c, 0): 1}

    for i in range(r):
        for j in range(c):
            nxt_dp: dict[tuple[tuple[int, ...], int], int] = defaultdict(int)
            blocked = grid[i][j] == 0

            for (state, left), ways in dp.items():
                up = state[j]

                if blocked:
                    if up == 0 and left == 0:
                        arr = list(state)
                        arr[j] = 0
                        key = normalize(tuple(arr), 0)
                        nxt_dp[key] = (nxt_dp[key] + ways) % MOD
                    continue

                if up == 0 and left == 0:
                    if i + 1 < r and j + 1 < c:
                        new_label = max(max(state), left) + 1
                        arr = list(state)
                        arr[j] = new_label
                        key = normalize(tuple(arr), new_label)
                        nxt_dp[key] = (nxt_dp[key] + ways) % MOD
                    continue

                if up != 0 and left == 0:
                    if i + 1 < r:
                        arr = list(state)
                        arr[j] = up
                        key = normalize(tuple(arr), 0)
                        nxt_dp[key] = (nxt_dp[key] + ways) % MOD
                    if j + 1 < c:
                        arr = list(state)
                        arr[j] = 0
                        key = normalize(tuple(arr), up)
                        nxt_dp[key] = (nxt_dp[key] + ways) % MOD
                    continue

                if up == 0 and left != 0:
                    if i + 1 < r:
                        arr = list(state)
                        arr[j] = left
                        key = normalize(tuple(arr), 0)
                        nxt_dp[key] = (nxt_dp[key] + ways) % MOD
                    if j + 1 < c:
                        arr = list(state)
                        arr[j] = 0
                        key = normalize(tuple(arr), left)
                        nxt_dp[key] = (nxt_dp[key] + ways) % MOD
                    continue

                # up 與 left 都存在，這格負責合併兩條鏈。
                arr = list(state)
                arr[j] = 0
                if up != left:
                    keep = min(up, left)
                    drop = max(up, left)
                    arr = [keep if x == drop else x for x in arr]
                key = normalize(tuple(arr), 0)
                nxt_dp[key] = (nxt_dp[key] + ways) % MOD

            dp = nxt_dp

        # 每列結束後，left 必須回到 0。
        cleaned: dict[tuple[tuple[int, ...], int], int] = defaultdict(int)
        for (state, left), ways in dp.items():
            if left != 0:
                continue
            key = normalize(state, 0)
            cleaned[key] = (cleaned[key] + ways) % MOD
        dp = cleaned

    return dp.get(((0,) * c, 0), 0) % MOD


def main() -> None:
    nums = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    out: list[str] = []
    while idx < len(nums):
        t = nums[idx]
        idx += 1
        if t == 0:
            break

        for case_no in range(1, t + 1):
            r = nums[idx]
            c = nums[idx + 1]
            idx += 2
            grid = []
            for _ in range(r):
                row = nums[idx:idx + c]
                idx += c
                grid.append(row)
            out.append(f"Case {case_no}: {solve_case(grid)}")
        break

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
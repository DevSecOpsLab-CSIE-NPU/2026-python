"""UVA 10235：限制蛇的擺法，簡單版。

這份程式保留同樣的核心想法，但把變數命名與流程寫得更直接：
1. 先把每一列的插座位置轉成 bitmask。
2. 再用遞迴去掃描該列每一格。
3. 最後累積成下一列的狀態。
"""

from __future__ import annotations

from functools import lru_cache
import sys

MOD = 1_000_000_007


def solve(data: str) -> str:
    """讀入整份測資，回傳答案字串。"""
    it = iter(map(int, data.split()))
    test_count = next(it)

    outputs: list[str] = []

    for case_index in range(1, test_count + 1):
        row_count = next(it)
        column_count = next(it)

        # blocked_rows 的第 i 位是 1，代表那個格子有插座，不能放蛇。
        blocked_rows: list[int] = []
        for _ in range(row_count):
            row_mask = 0
            for col in range(column_count):
                if next(it) == 0:
                    row_mask |= 1 << col
            blocked_rows.append(row_mask)

        @lru_cache(maxsize=None)
        def transition(row_mask: int, upper_mask: int, can_go_down: bool) -> dict[int, int]:
            """處理整列資料，回傳這一列可以轉出的所有下一列狀態。"""

            @lru_cache(maxsize=None)
            def scan(col: int, left_edge: int) -> dict[int, int]:
                if col == column_count:
                    return {0: 1} if left_edge == 0 else {}

                upper_edge = (upper_mask >> col) & 1
                has_socket = (row_mask >> col) & 1
                result: dict[int, int] = {}

                if has_socket:
                    if upper_edge == 0 and left_edge == 0:
                        for suffix_mask, count in scan(col + 1, 0).items():
                            key = suffix_mask << 1
                            result[key] = (result.get(key, 0) + count) % MOD
                    return result

                used = upper_edge + left_edge
                if used > 2:
                    return result

                need = 2 - used
                if can_go_down:
                    if need == 0:
                        choices = ((0, 0),)
                    elif need == 1:
                        choices = ((1, 0), (0, 1))
                    else:
                        choices = ((1, 1),)
                else:
                    if need == 0:
                        choices = ((0, 0),)
                    elif need == 1:
                        choices = ((1, 0),)
                    else:
                        return result

                # 迴圈中避免重複呼叫 scan 並把常用變數設為局部，提高效能
                for right_edge, down_edge in choices:
                    suffix = scan(col + 1, right_edge)
                    if not suffix:
                        continue
                    for suffix_mask, count in suffix.items():
                        next_mask = (suffix_mask << 1) | down_edge
                        result[next_mask] = (result.get(next_mask, 0) + count) % MOD

                return result

            return scan(0, 0)

        dp: dict[int, int] = {0: 1}
        for row_index, row_mask in enumerate(blocked_rows):
            can_go_down = row_index + 1 < row_count
            next_dp: dict[int, int] = {}

            for upper_mask, ways in dp.items():
                trans = transition(row_mask, upper_mask, can_go_down)
                if not trans:
                    continue
                for out_mask, count in trans.items():
                    next_dp[out_mask] = (next_dp.get(out_mask, 0) + ways * count) % MOD

            dp = next_dp

        outputs.append(f"Case {case_index}: {dp.get(0, 0) % MOD}")

    return "\n".join(outputs)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
"""
UVA 10093 / ZeroJudge a086 單元測試

題目重點：
在 N x M 地圖（P 可放、H 不可放）上放最多炮兵，且任兩支炮兵不能互相攻擊。
攻擊限制：
1. 同一列左右距離 1 或 2 不可同時放。
2. 同一欄上下距離 1 或 2 不可同時放。

測試策略：
1. 被測函式使用 bitmask + DP（可對應原題大範圍）。
2. 對照函式使用暴力列舉子集合（僅小尺寸測資）。
3. 以固定案例與隨機案例驗證 fast 與 oracle 一致。
"""

from __future__ import annotations

import random
import unittest


def solve_fast(grid: list[str]) -> int:
    """
    快速解（bitmask + DP）：
    dp_prev[(prev_state, prev2_state)] = 目前最大可放數量。

    每列狀態需同時滿足：
    1. 只放在 P 上。
    2. 列內無距離 1 與 2 的衝突。
    3. 與前一列、前二列在同欄不重疊。
    """
    n = len(grid)
    if n == 0:
        return 0
    m = len(grid[0])

    # 每列可放置位置（P）轉成 bitmask
    row_plain_masks: list[int] = []
    for row in grid:
        mask = 0
        for c, ch in enumerate(row):
            if ch == "P":
                mask |= 1 << c
        row_plain_masks.append(mask)

    valid_states: list[int] = []
    state_count: dict[int, int] = {}

    for state in range(1 << m):
        # 同列相鄰不能同時放
        if (state & (state << 1)) != 0:
            continue
        # 同列間隔一格（距離2）也不能同時放
        if (state & (state << 2)) != 0:
            continue
        valid_states.append(state)
        state_count[state] = state.bit_count()

    dp_prev: dict[tuple[int, int], int] = {(0, 0): 0}

    for r in range(n):
        allowed = row_plain_masks[r]
        dp_curr: dict[tuple[int, int], int] = {}

        for cur in valid_states:
            # 只能放在 P 上
            if (cur & ~allowed) != 0:
                continue

            cur_cnt = state_count[cur]

            for (prev, prev2), best in dp_prev.items():
                # 同欄上下距離 1 或 2 不可衝突
                if (cur & prev) != 0:
                    continue
                if (cur & prev2) != 0:
                    continue

                key = (cur, prev)
                val = best + cur_cnt

                old = dp_curr.get(key, -1)
                if val > old:
                    dp_curr[key] = val

        dp_prev = dp_curr

    return max(dp_prev.values(), default=0)


def solve_oracle(grid: list[str]) -> int:
    """
    暴力對照解：
    枚舉所有可放位置的子集合，檢查是否互不攻擊。
    僅適合小圖。
    """
    n = len(grid)
    if n == 0:
        return 0
    m = len(grid[0])

    cells: list[tuple[int, int]] = []
    for r in range(n):
        for c in range(m):
            if grid[r][c] == "P":
                cells.append((r, c))

    k = len(cells)

    def conflict(a: tuple[int, int], b: tuple[int, int]) -> bool:
        r1, c1 = a
        r2, c2 = b

        if r1 == r2 and 1 <= abs(c1 - c2) <= 2:
            return True
        if c1 == c2 and 1 <= abs(r1 - r2) <= 2:
            return True
        return False

    best = 0
    for mask in range(1 << k):
        chosen = mask.bit_count()
        if chosen <= best:
            continue

        ok = True
        for i in range(k):
            if not (mask & (1 << i)):
                continue
            for j in range(i + 1, k):
                if not (mask & (1 << j)):
                    continue
                if conflict(cells[i], cells[j]):
                    ok = False
                    break
            if not ok:
                break

        if ok:
            best = chosen

    return best


class TestQuestion10093(unittest.TestCase):
    """UVA 10093 測試集合。"""

    def test_single_cell(self) -> None:
        self.assertEqual(solve_fast(["P"]), 1)
        self.assertEqual(solve_fast(["H"]), 0)

    def test_one_row(self) -> None:
        # PPPPP 單列最多可放 2 支（例如位置 0 和 3）
        self.assertEqual(solve_fast(["PPPPP"]), 2)

    def test_all_blocked(self) -> None:
        grid = [
            "HHH",
            "HHH",
            "HHH",
        ]
        self.assertEqual(solve_fast(grid), 0)

    def test_handcrafted_compare(self) -> None:
        grid = [
            "PHP",
            "PPP",
            "HPH",
        ]
        self.assertEqual(solve_fast(grid), solve_oracle(grid))

    def test_random_compare_oracle(self) -> None:
        # 隨機小圖比對對照解，確保轉移邏輯正確
        random.seed(1009301)

        for _ in range(80):
            n = random.randint(1, 4)
            m = random.randint(1, 4)

            rows: list[str] = []
            for _r in range(n):
                chars = []
                for _c in range(m):
                    chars.append("P" if random.random() < 0.7 else "H")
                rows.append("".join(chars))

            fast = solve_fast(rows)
            oracle = solve_oracle(rows)
            self.assertEqual(fast, oracle)


if __name__ == "__main__":
    unittest.main()

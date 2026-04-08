"""
UVA 10093 / ZeroJudge a086 單元測試（-easy 版）

題意（好記版）：
- 地圖是 N x M，H 不能放、P 可以放。
- 炮兵會攻擊「同一列左右 1~2 格」與「同一欄上下 1~2 格」。
- 任何兩支炮兵不能互打，問最多放幾支。

這份檔案做兩件事：
1) 提供一個適合正式資料範圍的快速解（bitmask + DP）。
2) 提供小資料可用的暴力 oracle，拿來做單元測試對照。

為什麼這樣最容易記：
- 橫向限制只跟「同一列」有關，可先預算每列合法狀態。
- 縱向限制只看「同一欄前 1 列與前 2 列」，所以 DP 記三列關係即可。
"""

from __future__ import annotations

import random
import unittest


# =========================
# 一、被測試邏輯（快速版）
# =========================


def solve_fast(grid: list[str]) -> int:
    """
    bitmask + DP 解法。

    狀態定義（記憶口訣）：
    - dp_prev[(prev_state, prev2_state)] = 前 i-1 列處理完的最大值
    - 轉移到第 i 列時，枚舉 current_state
    - 需滿足：
      1) current_state 與地形相容（不能壓到 H）
      2) current_state 橫向不衝突（同列不能距離 1 或 2）
      3) current_state 與 prev_state / prev2_state 在同欄不能同時為 1
    """
    n = len(grid)
    if n == 0:
        return 0
    m = len(grid[0])

    # 把每一列可放置位置轉成 bitmask：P=1, H=0
    row_plain_masks: list[int] = []
    for row in grid:
        mask = 0
        for c, ch in enumerate(row):
            if ch == "P":
                mask |= 1 << c
        row_plain_masks.append(mask)

    # 先列舉所有「單列內部合法」狀態
    # 合法條件：不允許相鄰（距離1）與隔一格（距離2）同時放炮兵
    valid_states: list[int] = []
    popcount: dict[int, int] = {}
    for state in range(1 << m):
        if (state & (state << 1)) != 0:
            continue
        if (state & (state << 2)) != 0:
            continue
        valid_states.append(state)
        popcount[state] = state.bit_count()

    # 初始：還沒處理任何列，等價於前兩列狀態都為 0，分數是 0
    dp_prev: dict[tuple[int, int], int] = {(0, 0): 0}

    for r in range(n):
        allowed = row_plain_masks[r]
        dp_curr: dict[tuple[int, int], int] = {}

        for cur in valid_states:
            # cur 必須只放在 P 上
            if (cur & ~allowed) != 0:
                continue

            cur_cnt = popcount[cur]

            for (prev, prev2), best_val in dp_prev.items():
                # 縱向衝突：同欄上下 1 或 2 列不能同時放
                if (cur & prev) != 0:
                    continue
                if (cur & prev2) != 0:
                    continue

                new_key = (cur, prev)
                new_val = best_val + cur_cnt

                old_val = dp_curr.get(new_key, -1)
                if new_val > old_val:
                    dp_curr[new_key] = new_val

        dp_prev = dp_curr

    return max(dp_prev.values(), default=0)


# =========================
# 二、暴力 oracle（小資料）
# =========================


def solve_oracle_bruteforce(grid: list[str]) -> int:
    """
    暴力法：
    - 先收集所有可放位置（P）。
    - 枚舉所有子集合，檢查是否互不攻擊。

    只適用小尺寸（例如 P 格不超過 14 左右）。
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

        # 同一列，距離 1 或 2
        if r1 == r2 and 1 <= abs(c1 - c2) <= 2:
            return True

        # 同一欄，距離 1 或 2
        if c1 == c2 and 1 <= abs(r1 - r2) <= 2:
            return True

        return False

    best = 0
    for mask in range(1 << k):
        selected_count = mask.bit_count()
        if selected_count <= best:
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
            best = selected_count

    return best


# =========================
# 三、單元測試
# =========================


class TestQuestion10093Easy(unittest.TestCase):
    """UVA 10093（a086）-easy 測試。"""

    def test_single_cell(self) -> None:
        self.assertEqual(solve_fast(["P"]), 1)
        self.assertEqual(solve_fast(["H"]), 0)

    def test_one_row_basic(self) -> None:
        # 單列 PPPPP：由於同列距離 1,2 都不能並存，最多可放在位置 0 和 3，共 2 支
        self.assertEqual(solve_fast(["PPPPP"]), 2)

    def test_one_column_basic(self) -> None:
        # 單欄 5 列都可放：同欄距離 1,2 不能並存，最多可放 2 支（例如第 0 列與第 3 列）
        grid = ["P", "P", "P", "P", "P"]
        self.assertEqual(solve_fast(grid), 2)

    def test_all_blocked(self) -> None:
        grid = [
            "HHH",
            "HHH",
            "HHH",
        ]
        self.assertEqual(solve_fast(grid), 0)

    def test_small_handcrafted(self) -> None:
        grid = [
            "PHP",
            "PPP",
            "HPH",
        ]
        self.assertEqual(solve_fast(grid), solve_oracle_bruteforce(grid))

    def test_random_compare_with_oracle(self) -> None:
        # 小尺寸隨機圖，拿暴力解做黃金標準
        random.seed(10093)

        for _ in range(80):
            n = random.randint(1, 4)
            m = random.randint(1, 4)

            rows: list[str] = []
            for _r in range(n):
                row_chars = []
                for _c in range(m):
                    row_chars.append("P" if random.random() < 0.7 else "H")
                rows.append("".join(row_chars))

            fast = solve_fast(rows)
            oracle = solve_oracle_bruteforce(rows)
            self.assertEqual(fast, oracle)


if __name__ == "__main__":
    unittest.main()

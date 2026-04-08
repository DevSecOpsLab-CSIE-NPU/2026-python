"""
UVA 10093 / ZeroJudge a086
手打解題版（可直接提交 OJ）

題意：在 N x M 地圖中（P 可放、H 不可放），
放最多炮兵，且任兩支炮兵不可在同列/同欄距離 1 或 2 互相攻擊。

解法：bitmask + DP
- 先列舉每列所有合法狀態（同列不可距離 1、2 同時放）。
- DP 記錄三列關係：目前列、前一列、前二列。
- 轉移時檢查與地形、前兩列是否衝突。
"""

from __future__ import annotations

from datetime import datetime
import sys


def solve(grid: list[str]) -> int:
    n = len(grid)
    if n == 0:
        return 0
    m = len(grid[0])

    row_plain_masks: list[int] = []
    for row in grid:
        mask = 0
        for c, ch in enumerate(row):
            if ch == "P":
                mask |= 1 << c
        row_plain_masks.append(mask)

    valid_states: list[int] = []
    popcount: dict[int, int] = {}
    for state in range(1 << m):
        if (state & (state << 1)) != 0:
            continue
        if (state & (state << 2)) != 0:
            continue
        valid_states.append(state)
        popcount[state] = state.bit_count()

    dp_prev: dict[tuple[int, int], int] = {(0, 0): 0}

    for r in range(n):
        allowed = row_plain_masks[r]
        dp_curr: dict[tuple[int, int], int] = {}

        for cur in valid_states:
            if (cur & ~allowed) != 0:
                continue

            cur_cnt = popcount[cur]
            for (prev, prev2), best_val in dp_prev.items():
                if (cur & prev) != 0:
                    continue
                if (cur & prev2) != 0:
                    continue

                key = (cur, prev)
                val = best_val + cur_cnt
                if val > dp_curr.get(key, -1):
                    dp_curr[key] = val

        dp_prev = dp_curr

    return max(dp_prev.values(), default=0)


def run_selftest_and_log() -> int:
    """執行內建小測試並輸出 LOG 檔，回傳失敗數量。"""
    cases = [
        (["P"], 1),
        (["H"], 0),
        (["PPPPP"], 2),
        (["HHH", "HHH", "HHH"], 0),
    ]

    fail = 0
    lines: list[str] = []
    lines.append(f"[{datetime.now().isoformat(timespec='seconds')}] selftest start")

    for idx, (grid, expected) in enumerate(cases, start=1):
        got = solve(grid)
        ok = got == expected
        if not ok:
            fail += 1
        lines.append(f"case {idx}: grid={grid}, expected={expected}, got={got}, ok={ok}")

    lines.append(f"summary: total={len(cases)}, failed={fail}, passed={len(cases) - fail}")

    log_path = __file__.replace(".py", "_test.log")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    return fail


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    rows = data[2 : 2 + n]

    # 保守檢查：確保每列長度符合輸入 M
    rows = [row[:m] for row in rows]

    print(solve(rows))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "selftest":
        failed = run_selftest_and_log()
        print(f"selftest finished, failed={failed}")
    else:
        main()

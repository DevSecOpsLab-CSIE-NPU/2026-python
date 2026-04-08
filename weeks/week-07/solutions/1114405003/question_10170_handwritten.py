"""
UVA 10170 / ZeroJudge a163
手打解題版（可直接提交 OJ）

題意：每組輸入 (S, D) 要找第 D 天住的是幾人團。
輸入多組直到 EOF。
"""

from __future__ import annotations

from datetime import datetime
import sys


def days_sum(s: int, x: int) -> int:
    # sum(s..x)
    return (s + x) * (x - s + 1) // 2


def solve_one(s: int, d: int) -> int:
    # 二分找最小 x，使 sum(s..x) >= d
    left = s
    right = s

    while days_sum(s, right) < d:
        right *= 2

    while left < right:
        mid = (left + right) // 2
        if days_sum(s, mid) >= d:
            right = mid
        else:
            left = mid + 1

    return left


def run_selftest_and_log() -> int:
    """執行內建小測試並輸出 LOG 檔，回傳失敗數量。"""
    cases = [
        ((4, 1), 4),
        ((4, 5), 5),
        ((7, 24), 9),
        ((7, 25), 10),
    ]

    fail = 0
    lines: list[str] = []
    lines.append(f"[{datetime.now().isoformat(timespec='seconds')}] selftest start")

    for idx, ((s, d), expected) in enumerate(cases, start=1):
        got = solve_one(s, d)
        ok = got == expected
        if not ok:
            fail += 1
        lines.append(f"case {idx}: s={s}, d={d}, expected={expected}, got={got}, ok={ok}")

    lines.append(f"summary: total={len(cases)}, failed={fail}, passed={len(cases) - fail}")

    log_path = __file__.replace(".py", "_test.log")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    return fail


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    nums = list(map(int, data))
    out: list[str] = []

    # 每兩個數字是一組 (S, D)
    for i in range(0, len(nums) - 1, 2):
        s = nums[i]
        d = nums[i + 1]
        out.append(str(solve_one(s, d)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "selftest":
        failed = run_selftest_and_log()
        print(f"selftest finished, failed={failed}")
    else:
        main()

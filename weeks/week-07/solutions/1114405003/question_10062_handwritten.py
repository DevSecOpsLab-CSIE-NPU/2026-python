"""
UVA 10062 / ZeroJudge a055
手打解題版（可直接上傳 OJ）

題意重點：
已知每個位置前面有幾個「比自己小」的編號，還原整個排列。

解法：Fenwick Tree（BIT）+ 倒序還原
- 從最後一個位置往前填。
- 第 i 個位置要拿的是「目前可用編號中的第 a[i]+1 小」。
- 用 BIT 維護哪些編號還可用（可用=1，不可用=0）。
- 透過二分搜尋找第 k 小編號。
"""

from __future__ import annotations

from datetime import datetime
import sys


def solve(n: int, smaller_counts: list[int]) -> list[int]:
    # 轉成 1-based，a[1] 固定為 0（第一個位置前面沒有牛）
    a = [0] * (n + 1)
    for i in range(2, n + 1):
        a[i] = smaller_counts[i - 2]

    bit = [0] * (n + 1)

    def add(idx: int, delta: int) -> None:
        while idx <= n:
            bit[idx] += delta
            idx += idx & -idx

    def prefix_sum(idx: int) -> int:
        total = 0
        while idx > 0:
            total += bit[idx]
            idx -= idx & -idx
        return total

    # 初始 1..n 都可用
    for x in range(1, n + 1):
        add(x, 1)

    ans = [0] * (n + 1)

    # 倒序還原：每次取第 k 小可用編號
    for i in range(n, 0, -1):
        k = a[i] + 1

        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if prefix_sum(mid) >= k:
                right = mid
            else:
                left = mid + 1

        pick = left
        ans[i] = pick

        # 移除已使用編號
        add(pick, -1)

    return ans[1:]


def run_selftest_and_log() -> int:
    """執行內建小測試並輸出 LOG 檔，回傳失敗數量。"""
    cases = [
        (2, [0], [2, 1]),
        (2, [1], [1, 2]),
        (4, [0, 2, 1], [3, 1, 4, 2]),
    ]

    fail = 0
    lines: list[str] = []
    lines.append(f"[{datetime.now().isoformat(timespec='seconds')}] selftest start")

    for idx, (n, sc, expected) in enumerate(cases, start=1):
        got = solve(n, sc)
        ok = got == expected
        if not ok:
            fail += 1
        lines.append(
            f"case {idx}: n={n}, smaller_counts={sc}, expected={expected}, got={got}, ok={ok}"
        )

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
    smaller_counts = [int(x) for x in data[1:]]

    result = solve(n, smaller_counts)
    sys.stdout.write("\n".join(map(str, result)))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "selftest":
        failed = run_selftest_and_log()
        print(f"selftest finished, failed={failed}")
    else:
        main()

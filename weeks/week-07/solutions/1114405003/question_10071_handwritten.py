"""
UVA 10071 / ZeroJudge a064
手打解題版（可直接提交 OJ）

題意：計算有序六元組數量，滿足 a+b+c+d+e=f，且 a~f 皆來自集合 S（可重複使用）。

解法：
- 先統計所有 a+b+c 的出現次數 count3。
- 再枚舉 d,e,f，累加 count3[f-d-e]。
- 複雜度 O(N^3)，適合 N<=100。
"""

from __future__ import annotations

from datetime import datetime
import sys
from collections import Counter


def solve(values: list[int]) -> int:
    count3: Counter[int] = Counter()

    for a in values:
        for b in values:
            for c in values:
                count3[a + b + c] += 1

    ans = 0
    for d in values:
        for e in values:
            for f in values:
                ans += count3[f - d - e]

    return ans


def run_selftest_and_log() -> int:
    """執行內建小測試並輸出 LOG 檔，回傳失敗數量。"""
    cases = [
        ([0], 1),
        ([1], 0),
        ([-1, 0, 1], 141),
    ]

    fail = 0
    lines: list[str] = []
    lines.append(f"[{datetime.now().isoformat(timespec='seconds')}] selftest start")

    for idx, (values, expected) in enumerate(cases, start=1):
        got = solve(values)
        ok = got == expected
        if not ok:
            fail += 1
        lines.append(f"case {idx}: values={values}, expected={expected}, got={got}, ok={ok}")

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
    values = [int(x) for x in data[1 : 1 + n]]

    print(solve(values))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "selftest":
        failed = run_selftest_and_log()
        print(f"selftest finished, failed={failed}")
    else:
        main()

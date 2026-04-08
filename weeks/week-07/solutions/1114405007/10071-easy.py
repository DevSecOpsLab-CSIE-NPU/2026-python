from __future__ import annotations

import sys
from collections import defaultdict


def solve(data: str) -> str:
    numbers = [int(x) for x in data.split()]
    if not numbers:
        return ""

    n = numbers[0]
    s = numbers[1 : 1 + n]

    # 先算 a+b 的所有可能（有順序、可重複取），記錄每個和出現幾次。
    sum2: dict[int, int] = defaultdict(int)
    for a in s:
        for b in s:
            sum2[a + b] += 1

    # 再由 (a+b)+c 擴充成三數和，得到 c+d+e 的等價統計表。
    sum3: dict[int, int] = defaultdict(int)
    for partial, cnt in sum2.items():
        for c in s:
            sum3[partial + c] += cnt

    # 對每個 f，計算 a+b+c+d+e=f 的五數和組合數，最後把所有 f 加總。
    total_sextuples = 0
    for f in s:
        ways_for_this_f = 0
        for ab, cnt_ab in sum2.items():
            need = f - ab
            ways_for_this_f += cnt_ab * sum3.get(need, 0)
        total_sextuples += ways_for_this_f

    return str(total_sextuples)


def main() -> None:
    data = sys.stdin.read()
    output = solve(data)
    if output:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()

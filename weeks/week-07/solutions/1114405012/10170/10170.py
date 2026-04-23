"""UVA 10170 - The Hotel with Infinite Rooms。

對每筆 (S, D)：找最小 k >= S，使得
S + (S+1) + ... + k >= D。

以 while 逐步累加即可，因為每筆最多增加到約 sqrt(2D)。
"""

from __future__ import annotations

import sys


def solve(input_data: str) -> str:
    nums = [int(x) for x in input_data.split()]
    out = []
    for i in range(0, len(nums), 2):
        if i + 1 >= len(nums):
            break
        s = nums[i]
        d = nums[i + 1]

        cur = s
        acc = s
        while acc < d:
            cur += 1
            acc += cur

        out.append(str(cur))
    return "\n".join(out)


def main() -> None:
    data = sys.stdin.read()
    out = solve(data)
    if out:
        sys.stdout.write(out + "\n")


if __name__ == "__main__":
    main()

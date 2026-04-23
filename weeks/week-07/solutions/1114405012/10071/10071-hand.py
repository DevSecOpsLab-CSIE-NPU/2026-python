"""10071 easy 手打版。"""

import sys
from collections import defaultdict


def solve(input_data: str) -> str:
    nums = [int(x) for x in input_data.split()]
    if not nums:
        return ""

    n = nums[0]
    s = nums[1 : 1 + n]

    two = defaultdict(int)
    for d in s:
        for e in s:
            two[d + e] += 1

    three = defaultdict(int)
    for a in s:
        for b in s:
            for c in s:
                three[a + b + c] += 1

    ans = 0
    for f in s:
        for t, cnt in three.items():
            ans += cnt * two.get(f - t, 0)

    return str(ans)


def main() -> None:
    data = sys.stdin.read()
    out = solve(data)
    if out:
        print(out)


if __name__ == "__main__":
    main()

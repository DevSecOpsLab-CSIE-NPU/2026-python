"""UVA 10170 簡單版（easy）。

逐日累加到第 D 天即可，程式最直觀。
"""

from __future__ import annotations

import sys


def solve(input_data: str) -> str:
    vals = [int(x) for x in input_data.split()]
    ans = []
    p = 0
    while p + 1 < len(vals):
        s = vals[p]
        d = vals[p + 1]
        p += 2

        people = s
        days = s
        while days < d:
            people += 1
            days += people

        ans.append(str(people))

    return "\n".join(ans)


def main() -> None:
    data = sys.stdin.read()
    out = solve(data)
    if out:
        sys.stdout.write(out + "\n")


if __name__ == "__main__":
    main()

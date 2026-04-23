"""10062 easy 手打版。"""

import sys


def solve(input_data: str) -> str:
    nums = [int(x) for x in input_data.split()]
    if not nums:
        return ""

    n = nums[0]
    a = [0] * (n + 1)
    for i in range(2, n + 1):
        a[i] = nums[i - 1]

    available = list(range(1, n + 1))
    ans = [0] * (n + 1)

    for i in range(n, 0, -1):
        ans[i] = available.pop(a[i])

    return "\n".join(str(x) for x in ans[1:])


def main() -> None:
    data = sys.stdin.read()
    out = solve(data)
    if out:
        print(out)


if __name__ == "__main__":
    main()

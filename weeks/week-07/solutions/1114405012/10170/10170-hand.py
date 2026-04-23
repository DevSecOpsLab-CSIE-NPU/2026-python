"""10170 easy 手打版。"""

import sys


def solve(input_data: str) -> str:
    nums = [int(x) for x in input_data.split()]
    out = []

    i = 0
    while i + 1 < len(nums):
        s = nums[i]
        d = nums[i + 1]
        i += 2

        people = s
        days = s
        while days < d:
            people += 1
            days += people

        out.append(str(people))

    return "\n".join(out)


def main() -> None:
    data = sys.stdin.read()
    out = solve(data)
    if out:
        print(out)


if __name__ == "__main__":
    main()

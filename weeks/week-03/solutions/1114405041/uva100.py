"""UVA 100 - The 3n + 1 problem."""

import sys

memo = {1: 1}


def cycle_length(n: int) -> int:
    """Return cycle length of n with memoization."""
    if n in memo:
        return memo[n]

    path = []
    cur = n
    while cur not in memo:
        path.append(cur)
        if cur % 2 == 1:
            cur = 3 * cur + 1
        else:
            cur //= 2

    length = memo[cur]
    for value in reversed(path):
        length += 1
        memo[value] = length

    return memo[n]


def max_cycle(i: int, j: int) -> int:
    left, right = (i, j) if i <= j else (j, i)
    best = 0
    for value in range(left, right + 1):
        best = max(best, cycle_length(value))
    return best


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        i, j = map(int, line.split())
        print(i, j, max_cycle(i, j))


if __name__ == "__main__":
    main()

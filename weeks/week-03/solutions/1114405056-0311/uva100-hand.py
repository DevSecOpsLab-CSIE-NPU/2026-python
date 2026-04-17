import sys

memo = {1: 1}


def cycle_length(n: int) -> int:
    start = n
    path = []
    while n not in memo:
        path.append(n)
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n //= 2
    length = memo[n]
    for value in reversed(path):
        length += 1
        memo[value] = length
    return memo[start]


def max_cycle(i: int, j: int) -> int:
    left = min(i, j)
    right = max(i, j)
    best = 0
    for n in range(left, right + 1):
        best = max(best, cycle_length(n))
    return best


def solve(data: str) -> str:
    out = []
    for raw in data.splitlines():
        line = raw.strip()
        if not line:
            continue
        i, j = map(int, line.split())
        out.append(f"{i} {j} {max_cycle(i, j)}")
    return "\n".join(out)


def main() -> None:
    text = sys.stdin.read()
    ans = solve(text)
    if ans:
        print(ans)


if __name__ == "__main__":
    main()

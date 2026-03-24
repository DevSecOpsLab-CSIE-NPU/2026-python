import sys


def cycle_length(n, memo):
    original = n
    steps = 0

    while n not in memo:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n //= 2
        steps += 1

    memo[original] = steps + memo[n]
    return memo[original]


def main():
    memo = {1: 1}

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        i, j = map(int, line.split())
        left = min(i, j)
        right = max(i, j)

        best = 0
        for n in range(left, right + 1):
            best = max(best, cycle_length(n, memo))

        print(i, j, best)


if __name__ == "__main__":
    main()

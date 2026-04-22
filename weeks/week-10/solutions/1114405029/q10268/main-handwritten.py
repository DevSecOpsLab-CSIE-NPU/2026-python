import sys


LIMIT = 63
TOO_MANY = "More than 63 trials needed."


def min_trials(k, n):
    dp = [0] * (k + 1)

    for trials in range(1, LIMIT + 1):
        for eggs in range(k, 0, -1):
            dp[eggs] = dp[eggs] + dp[eggs - 1] + 1

        if dp[k] >= n:
            return str(trials)

    return TOO_MANY


def main():
    outputs = []

    for line in sys.stdin:
        line = line.strip()

        if not line:
            continue

        k, n = map(int, line.split())

        if k == 0 and n == 0:
            break

        outputs.append(min_trials(k, n))

    print("\n".join(outputs))


if __name__ == "__main__":
    main()
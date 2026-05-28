import math
import sys


def gcd_sum(n: int) -> int:
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += math.gcd(i, j)
    return total


def solve(data: str) -> str:
    answers = []
    for token in data.split():
        n = int(token)
        if n == 0:
            break
        answers.append(str(gcd_sum(n)))
    return "\n".join(answers)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

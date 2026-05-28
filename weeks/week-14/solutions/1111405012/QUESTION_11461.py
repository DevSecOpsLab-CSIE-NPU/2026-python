import math
import sys


def count_square_numbers(a: int, b: int) -> int:
    return math.isqrt(b) - math.isqrt(a - 1)


def solve(data: str) -> str:
    numbers = list(map(int, data.split()))
    answers = []

    for index in range(0, len(numbers), 2):
        a, b = numbers[index], numbers[index + 1]
        if a == 0 and b == 0:
            break
        answers.append(str(count_square_numbers(a, b)))

    return "\n".join(answers)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

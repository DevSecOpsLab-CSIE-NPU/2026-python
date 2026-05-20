from __future__ import annotations


def root(number: int) -> int:
    while number >= 10:
        total = 0
        for digit in str(number):
            total += int(digit)
        number = total
    return number


def solve(data: str) -> str:
    answers: list[str] = []
    for token in data.split():
        number = int(token)
        if number == 0:
            break
        answers.append(str(root(number)))
    return "\n".join(answers)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

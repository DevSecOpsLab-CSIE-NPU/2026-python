from __future__ import annotations


def drink_all(start: int) -> int:
    return start + start // 2


def solve(data: str) -> str:
    answers = [str(drink_all(int(token))) for token in data.split()]
    return "\n".join(answers)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

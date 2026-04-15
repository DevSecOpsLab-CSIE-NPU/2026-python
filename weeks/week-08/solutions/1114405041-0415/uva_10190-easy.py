from __future__ import annotations

import sys


def build_sequence(n: int, m: int) -> str:
    """
    簡單版規則：
    - 只要 n 可以一直整除 m，直到最後變成 1，就把過程列出來。
    - 途中只要不能整除，或 m <= 1，答案就是 Boring!
    """
    if n <= 1 or m <= 1:
        return "Boring!"

    numbers = [n]

    while n > 1:
        if n % m != 0:
            return "Boring!"
        n //= m
        numbers.append(n)

    return " ".join(str(value) for value in numbers)


def solve(data: str) -> str:
    outputs: list[str] = []

    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue

        n, m = map(int, line.split())
        outputs.append(build_sequence(n, m))

    return "\n".join(outputs)


def main() -> None:
    raw_data = sys.stdin.read()
    sys.stdout.write(solve(raw_data))


if __name__ == "__main__":
    main()

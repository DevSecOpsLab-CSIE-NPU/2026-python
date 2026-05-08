#!/usr/bin/env python3


def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    results = []
    for line in lines:
        tokens = [int(x) for x in line.split()]
        n = tokens[0]
        sequence = tokens[1:n + 1]
        differences = set()
        for i in range(1, n):
            diff = abs(sequence[i] - sequence[i - 1])
            if diff == 0 or diff > n - 1:
                results.append('Not jolly')
                break
            differences.add(diff)
        else:
            if len(differences) == n - 1 and differences == set(range(1, n)):
                results.append('Jolly')
            else:
                results.append('Not jolly')
    return '\n'.join(results)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
from typing import List


def is_jolly_sequence(numbers: List[int]) -> bool:
    n = len(numbers)
    if n <= 1:
        return True

    diffs = set(abs(numbers[i] - numbers[i - 1]) for i in range(1, n))
    return diffs == set(range(1, n))


def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.splitlines() if line.strip()]
    results = []
    for line in lines:
        parts = [int(x) for x in line.split()]
        if not parts:
            continue
        n = parts[0]
        numbers = parts[1:1 + n]
        if is_jolly_sequence(numbers):
            results.append('Jolly')
        else:
            results.append('Not jolly')
    return '\n'.join(results)


def main() -> None:
    import sys
    print(process_input(sys.stdin.read()), end='')


if __name__ == '__main__':
    main()

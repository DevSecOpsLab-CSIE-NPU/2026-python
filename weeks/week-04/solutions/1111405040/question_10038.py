"""
UVA 10038 - Jolly Jumpers
"""

from __future__ import annotations


def is_jolly(sequence: list[int]) -> bool:
    """判斷序列是否為 Jolly Jumper。"""
    length = len(sequence)
    if length <= 1:
        return True

    differences = {abs(current - previous) for previous, current in zip(sequence, sequence[1:])}
    return differences == set(range(1, length))


def solve(text: str) -> str:
    """逐行判斷每筆資料是否為 Jolly Jumper。"""
    results: list[str] = []
    for line in text.splitlines():
        if not line.strip():
            continue
        numbers = [int(value) for value in line.split()]
        count = numbers[0]
        sequence = numbers[1 : 1 + count]
        results.append("Jolly" if is_jolly(sequence) else "Not jolly")
    return "\n".join(results)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

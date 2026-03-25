"""
UVA 10057 - A mid-summer night's dream
"""

from __future__ import annotations


def analyze_numbers(numbers: list[int]) -> tuple[int, int, int]:
    """回傳最小中位數、符合值的數量，以及可行整數範圍大小。"""
    sorted_numbers = sorted(numbers)
    low = sorted_numbers[(len(sorted_numbers) - 1) // 2]
    high = sorted_numbers[len(sorted_numbers) // 2]
    count = sum(low <= number <= high for number in sorted_numbers)
    return low, count, high - low + 1


def solve(text: str) -> str:
    """讀到 EOF 為止，逐組輸出答案。"""
    tokens = [int(token) for token in text.split()]
    index = 0
    results: list[str] = []

    while index < len(tokens):
        number_count = tokens[index]
        index += 1
        numbers = tokens[index : index + number_count]
        index += number_count
        low, count, range_size = analyze_numbers(numbers)
        results.append(f"{low} {count} {range_size}")

    return "\n".join(results)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

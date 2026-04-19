from __future__ import annotations

from typing import Iterable, List


def dedupe_preserve_order(numbers: Iterable[int]) -> List[int]:
    seen = set()
    deduped: List[int] = []
    for number in numbers:
        if number in seen:
            continue
        seen.add(number)
        deduped.append(number)
    return deduped


def sort_ascending(numbers: Iterable[int]) -> List[int]:
    return sorted(numbers)


def sort_descending(numbers: Iterable[int]) -> List[int]:
    return sorted(numbers, reverse=True)


def filter_evens(numbers: Iterable[int]) -> List[int]:
    return [number for number in numbers if number % 2 == 0]


def format_sequence_output(numbers: Iterable[int]) -> str:
    original_numbers = list(numbers)
    lines = [
        f"dedupe: {' '.join(map(str, dedupe_preserve_order(original_numbers)))}",
        f"asc: {' '.join(map(str, sort_ascending(original_numbers)))}",
        f"desc: {' '.join(map(str, sort_descending(original_numbers)))}",
        f"evens: {' '.join(map(str, filter_evens(original_numbers)))}",
    ]
    return "\n".join(lines)


def solve(text: str) -> str:
    stripped = text.strip()
    if not stripped:
        return format_sequence_output([])
    numbers = [int(token) for token in stripped.split()]
    return format_sequence_output(numbers)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
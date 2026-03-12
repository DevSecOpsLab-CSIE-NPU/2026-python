import sys
from typing import Dict, List


def parse_numbers(raw: str) -> List[int]:
    text = raw.strip()
    if not text:
        return []
    return [int(part) for part in text.split()]


def dedupe_preserve_order(numbers: List[int]) -> List[int]:
    seen = set()
    deduped = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            deduped.append(number)
    return deduped


def build_views(numbers: List[int]) -> Dict[str, List[int]]:
    return {
        "dedupe": dedupe_preserve_order(numbers),
        "asc": sorted(numbers),
        "desc": sorted(numbers, reverse=True),
        "evens": [number for number in numbers if number % 2 == 0],
    }


def format_line(label: str, numbers: List[int]) -> str:
    joined = " ".join(str(number) for number in numbers)
    if not joined:
        return f"{label}:"
    return f"{label}: {joined}"


def solve(raw: str) -> str:
    numbers = parse_numbers(raw)
    views = build_views(numbers)
    return "\n".join(
        [
            format_line("dedupe", views["dedupe"]),
            format_line("asc", views["asc"]),
            format_line("desc", views["desc"]),
            format_line("evens", views["evens"]),
        ]
    )


def main() -> None:
    raw = sys.stdin.read()
    print(solve(raw))


if __name__ == "__main__":
    main()

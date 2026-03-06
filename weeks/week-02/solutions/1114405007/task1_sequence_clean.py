from __future__ import annotations

from typing import Dict, List


def dedupe_preserve_order(numbers: List[int]) -> List[int]:
    seen = set()
    deduped: List[int] = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            deduped.append(number)
    return deduped


def clean_sequence(numbers: List[int]) -> Dict[str, List[int]]:
    return {
        "dedupe": dedupe_preserve_order(numbers),
        "asc": sorted(numbers),
        "desc": sorted(numbers, reverse=True),
        "evens": [n for n in numbers if n % 2 == 0],
    }


def format_output(result: Dict[str, List[int]]) -> str:
    lines = []
    for key in ("dedupe", "asc", "desc", "evens"):
        values = " ".join(str(n) for n in result[key])
        lines.append(f"{key}: {values}".rstrip())
    return "\n".join(lines)


def main() -> None:
    raw = input().strip()
    numbers = [int(token) for token in raw.split()] if raw else []
    print(format_output(clean_sequence(numbers)))


if __name__ == "__main__":
    main()

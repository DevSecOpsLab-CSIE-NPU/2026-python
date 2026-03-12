"""Task 1: Sequence Clean

This module provides a small pipeline for parsing a single line of whitespace-separated
integers and producing:

1. Deduplicated list (keep first occurrence)
2. Sorted ascending list
3. Sorted descending list
4. Even numbers in original order

The module is written to be testable and the `main()` function is friendly for CLI use.
"""

from __future__ import annotations

from typing import Iterable, List, Tuple


def parse_integers(line: str) -> List[int]:
    """Parse a whitespace-separated line into integers.

    Empty lines and extra whitespace are ignored.
    """
    return [int(tok) for tok in line.strip().split() if tok]


def dedupe_keep_first(items: Iterable[int]) -> List[int]:
    """Return items with duplicates removed while keeping first occurrence order."""
    seen = set()
    out: List[int] = []
    for x in items:
        if x in seen:
            continue
        seen.add(x)
        out.append(x)
    return out


def sequence_clean(line: str) -> Tuple[List[int], List[int], List[int], List[int]]:
    """Run the sequence clean pipeline.

    Returns a tuple of (deduped, asc, desc, evens).
    """
    nums = parse_integers(line)
    deduped = dedupe_keep_first(nums)
    asc = sorted(nums)
    desc = sorted(nums, reverse=True)
    evens = [x for x in nums if x % 2 == 0]
    return deduped, asc, desc, evens


def format_sequence_clean(
    deduped: List[int], asc: List[int], desc: List[int], evens: List[int]
) -> str:
    """Format the result for human-readable output."""
    return "\n".join(
        [
            "dedupe: " + " ".join(str(x) for x in deduped),
            "asc: " + " ".join(str(x) for x in asc),
            "desc: " + " ".join(str(x) for x in desc),
            "evens: " + " ".join(str(x) for x in evens),
        ]
    )


def main() -> None:
    import sys

    data = sys.stdin.read()
    if not data.strip():
        return
    deduped, asc, desc, evens = sequence_clean(data)
    print(format_sequence_clean(deduped, asc, desc, evens))


if __name__ == "__main__":
    main()

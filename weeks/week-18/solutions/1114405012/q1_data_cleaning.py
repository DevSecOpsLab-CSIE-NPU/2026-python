"""Week 18 Q1: Data cleaning.

Usage:
    python q1_data_cleaning.py < input.txt

For student ID 1114405012, the divisor parameter is D = 4.
"""

from __future__ import annotations

import sys
from typing import Iterable, List


D = 4


def clean_numbers(numbers: Iterable[int], divisor: int = D) -> List[int]:
    """Remove duplicates, keep numbers divisible by divisor, then sort ascending."""

    seen = set()
    filtered = []
    for number in numbers:
        if number in seen:
            continue
        seen.add(number)
        if number % divisor == 0:
            filtered.append(number)
    return sorted(filtered)


def parse_input(tokens: Iterable[str]) -> List[List[int]]:
    """Parse the full input stream into batches."""

    iterator = iter(tokens)
    datasets: List[List[int]] = []
    while True:
        try:
            n = int(next(iterator))
        except StopIteration:
            break
        if n == 0:
            break
        numbers = [int(next(iterator)) for _ in range(n)]
        datasets.append(numbers)
    return datasets


def solve(data: str) -> str:
    tokens = data.split()
    datasets = parse_input(tokens)
    outputs = []
    for numbers in datasets:
        cleaned = clean_numbers(numbers)
        outputs.append("NONE" if not cleaned else " ".join(str(x) for x in cleaned))
    return "\n".join(outputs)


if __name__ == "__main__":
    output = solve(sys.stdin.read())
    if output:
        sys.stdout.write(output + "\n")
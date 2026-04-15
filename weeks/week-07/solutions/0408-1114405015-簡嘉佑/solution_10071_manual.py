"""
UVA 10071 manual solution.

Problem:
Given a set S of integers, count how many 6-tuples (a,b,c,d,e,f)
satisfy a+b+c+d+e = f where all elements are from S (with repetition allowed).

Algorithm:
1. Pre-compute all 4-sums a+b+c+d with Counter to track frequency.
2. For each pair (e,f), add count of (f-e) in the pre-computed sums.

Time: O(N^4 + N^2) = O(N^4)
Space: O(N^4) in worst case
"""

from __future__ import annotations

from collections import Counter
from typing import List


def count_tuples(values: List[int]) -> int:
    """Count 6-tuples (a,b,c,d,e,f) from values where a+b+c+d+e=f."""
    sum4_count = Counter()

    for a in values:
        for b in values:
            for c in values:
                for d in values:
                    sum4_count[a + b + c + d] += 1

    total = 0
    for e in values:
        for f in values:
            total += sum4_count.get(f - e, 0)

    return total


def main() -> None:
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    values = [int(x) for x in data[1:1 + n]]
    result = count_tuples(values)
    sys.stdout.write(str(result))


if __name__ == "__main__":
    main()

"""
Manual solution for UVA 10170 - The Hotel with Infinite Rooms.

Given S (size of the first group) and D (day index, 1-based),
find the group size staying on day D.

Groups are S, S+1, S+2, ... and each group of size x stays x days.
"""

from __future__ import annotations


def total_days_from_s_to_x(s: int, x: int) -> int:
    """Return sum(s..x). If x < s, return 0."""
    if x < s:
        return 0
    return x * (x + 1) // 2 - (s - 1) * s // 2


def solve_hotel(s: int, d: int) -> int:
    """Return the group size that stays on day d."""
    left = s
    right = s

    # Expand right bound until it covers day d.
    while total_days_from_s_to_x(s, right) < d:
        right *= 2

    # Binary search the smallest x with total_days_from_s_to_x(s, x) >= d.
    while left < right:
        mid = (left + right) // 2
        if total_days_from_s_to_x(s, mid) >= d:
            right = mid
        else:
            left = mid + 1

    return left


def main() -> None:
    import sys

    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        s_str, d_str = line.split()
        out.append(str(solve_hotel(int(s_str), int(d_str))))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

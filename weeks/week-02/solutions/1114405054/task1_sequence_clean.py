from __future__ import annotations

import sys


def parse_numbers(line: str) -> list[int]:
    line = line.strip()
    if not line:
        return []
    return [int(token) for token in line.split()]


def dedupe_keep_order(nums: list[int]) -> list[int]:
    seen: set[int] = set()
    result: list[int] = []
    for n in nums:
        if n in seen:
            continue
        seen.add(n)
        result.append(n)
    return result


def format_line(label: str, nums: list[int]) -> str:
    if not nums:
        return f"{label}:"
    return f"{label}: {' '.join(map(str, nums))}"


def solve(data: str) -> str:
    first_line = data.splitlines()[0] if data.splitlines() else ""
    nums = parse_numbers(first_line)

    lines = [
        format_line("dedupe", dedupe_keep_order(nums)),
        format_line("asc", sorted(nums)),
        format_line("desc", sorted(nums, reverse=True)),
        format_line("evens", [n for n in nums if n % 2 == 0]),
    ]
    return "\n".join(lines)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
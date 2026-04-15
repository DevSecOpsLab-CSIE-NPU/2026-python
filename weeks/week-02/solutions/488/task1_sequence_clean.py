"""Task 1: Sequence Clean."""


def parse_numbers(line: str) -> list[int]:
    """Parse a whitespace-separated integer line into a list."""
    stripped = line.strip()
    if not stripped:
        return []
    return [int(token) for token in stripped.split()]


def dedupe_preserve_order(numbers: list[int]) -> list[int]:
    """Remove duplicates while preserving first-seen order."""
    seen = set()
    result: list[int] = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


def build_outputs(numbers: list[int]) -> dict[str, list[int]]:
    """Build all required result sequences."""
    return {
        "dedupe": dedupe_preserve_order(numbers),
        "asc": sorted(numbers),
        "desc": sorted(numbers, reverse=True),
        "evens": [num for num in numbers if num % 2 == 0],
    }


def format_numbers(numbers: list[int]) -> str:
    """Format list of numbers for output lines."""
    return " ".join(str(num) for num in numbers)


def solve(line: str) -> list[str]:
    """Solve Task 1 and return output lines."""
    numbers = parse_numbers(line)
    outputs = build_outputs(numbers)
    return [
        f"dedupe: {format_numbers(outputs['dedupe'])}",
        f"asc: {format_numbers(outputs['asc'])}",
        f"desc: {format_numbers(outputs['desc'])}",
        f"evens: {format_numbers(outputs['evens'])}",
    ]


def main() -> None:
    line = input().rstrip("\n")
    for output_line in solve(line):
        print(output_line)


if __name__ == "__main__":
    main()

"""Task 1: sequence cleaning and sorting."""


def parse_numbers_line(line: str) -> list[int]:
    line = line.strip()
    if not line:
        return []
    return [int(token) for token in line.split()]


def dedupe_keep_order(numbers: list[int]) -> list[int]:
    seen = set()
    result = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result


def build_report(numbers: list[int]) -> dict[str, list[int]]:
    return {
        "dedupe": dedupe_keep_order(numbers),
        "asc": sorted(numbers),
        "desc": sorted(numbers, reverse=True),
        "evens": [n for n in numbers if n % 2 == 0],
    }


def _join_numbers(numbers: list[int]) -> str:
    return " ".join(str(n) for n in numbers)


def format_report(report: dict[str, list[int]]) -> str:
    return "\n".join(
        [
            f"dedupe: {_join_numbers(report['dedupe'])}",
            f"asc: {_join_numbers(report['asc'])}",
            f"desc: {_join_numbers(report['desc'])}",
            f"evens: {_join_numbers(report['evens'])}",
        ]
    )


def main() -> None:
    numbers = parse_numbers_line(input())
    report = build_report(numbers)
    print(format_report(report))


if __name__ == "__main__":
    main()

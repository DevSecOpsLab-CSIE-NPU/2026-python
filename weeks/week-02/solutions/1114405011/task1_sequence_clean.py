def process_numbers(numbers: list[int]) -> dict[str, list[int]]:
    seen = set()
    dedupe = []
    for n in numbers:
        if n not in seen:
            seen.add(n)
            dedupe.append(n)

    return {
        "dedupe": dedupe,
        "asc": sorted(numbers),
        "desc": sorted(numbers, reverse=True),
        "evens": [n for n in numbers if n % 2 == 0],
    }


def format_output(result: dict[str, list[int]]) -> str:
    return "\n".join(
        [
            "dedupe: " + " ".join(str(x) for x in result["dedupe"]),
            "asc: " + " ".join(str(x) for x in result["asc"]),
            "desc: " + " ".join(str(x) for x in result["desc"]),
            "evens: " + " ".join(str(x) for x in result["evens"]),
        ]
    )


def parse_input(raw: str) -> list[int]:
    raw = raw.strip()
    if raw == "":
        return []
    return [int(x) for x in raw.split()]


def main() -> None:
    raw = input()
    nums = parse_input(raw)
    out = process_numbers(nums)
    print(format_output(out))


if __name__ == "__main__":
    main()

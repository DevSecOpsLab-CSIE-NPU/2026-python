from __future__ import annotations

import sys


def median_summary(numbers: list[int]) -> tuple[int, int, int]:
    # Sort first so the median positions are easy to locate.
    numbers.sort()
    length = len(numbers)

    # For odd length, both median positions point to the same value.
    # For even length, every integer between the two medians is optimal.
    lower_median = numbers[(length - 1) // 2]
    upper_median = numbers[length // 2]

    # The second output is not the number of possible answers.
    # It is the count of input values inside the optimal range.
    match_count = 0
    for value in numbers:
        if lower_median <= value <= upper_median:
            match_count += 1

    # If both medians are the same, there is only one optimal answer.
    # Otherwise, every integer between them is valid.
    possible_count = upper_median - lower_median + 1

    # UVA requires the first output to be the smaller median.
    return lower_median, match_count, possible_count


def solve(data: str) -> str:
    parts = data.split()
    index = 0
    outputs: list[str] = []

    while index < len(parts):
        count = int(parts[index])
        index += 1

        numbers: list[int] = []
        for _ in range(count):
            numbers.append(int(parts[index]))
            index += 1

        median_value, match_count, possible_count = median_summary(numbers)
        outputs.append(f"{median_value} {match_count} {possible_count}")

    return "\n".join(outputs)


def main() -> None:
    raw_data = sys.stdin.read()
    sys.stdout.write(solve(raw_data))


if __name__ == "__main__":
    main()
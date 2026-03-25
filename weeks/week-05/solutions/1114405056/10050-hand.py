from __future__ import annotations

import sys


def count_lost_workdays(total_days: int, hartal_parameters: list[int]) -> int:
    # Use a set to store lost workdays.
    # If multiple parties strike on the same day, it is still counted once.
    lost_days: set[int] = set()

    for interval in hartal_parameters:
        # This party calls a strike every interval days.
        for day in range(interval, total_days + 1, interval):
            # Day 1 is Sunday.
            # day % 7 == 6 means Friday, and day % 7 == 0 means Saturday.
            # Those are weekends, so they are not counted as lost workdays.
            if day % 7 == 6 or day % 7 == 0:
                continue

            lost_days.add(day)

    return len(lost_days)


def solve(data: str) -> str:
    parts = data.split()
    if not parts:
        return ""

    case_count = int(parts[0])
    index = 1
    outputs: list[str] = []

    for _ in range(case_count):
        total_days = int(parts[index])
        index += 1

        party_count = int(parts[index])
        index += 1

        hartal_parameters: list[int] = []
        for _ in range(party_count):
            hartal_parameters.append(int(parts[index]))
            index += 1

        outputs.append(str(count_lost_workdays(total_days, hartal_parameters)))

    return "\n".join(outputs)


def main() -> None:
    raw_data = sys.stdin.read()
    sys.stdout.write(solve(raw_data))


if __name__ == "__main__":
    main()
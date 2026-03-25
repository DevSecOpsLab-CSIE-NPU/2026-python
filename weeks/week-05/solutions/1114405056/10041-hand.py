from __future__ import annotations

import sys


def minimum_total_distance(addresses: list[int]) -> int:
    # The key idea is to place the house at the median address.
    # That position minimizes the total walking distance to all relatives.
    addresses.sort()

    # The middle address after sorting is the best location.
    middle_index = len(addresses) // 2
    best_address = addresses[middle_index]

    # Sum the distances from the chosen address to every relative.
    total_distance = 0
    for address in addresses:
        total_distance += abs(address - best_address)

    return total_distance


def solve(data: str) -> str:
    # Split the whole input into tokens and read them in order.
    parts = data.split()
    if not parts:
        return ""

    case_count = int(parts[0])
    index = 1
    outputs: list[str] = []

    for _ in range(case_count):
        # Each case starts with the number of relatives, followed by addresses.
        count = int(parts[index])
        index += 1

        addresses: list[int] = []
        for _ in range(count):
            addresses.append(int(parts[index]))
            index += 1

        outputs.append(str(minimum_total_distance(addresses)))

    return "\n".join(outputs)


def main() -> None:
    # Read from standard input and print the result.
    raw_data = sys.stdin.read()
    sys.stdout.write(solve(raw_data))


if __name__ == "__main__":
    main()
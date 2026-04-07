import sys
from typing import List


def best_meeting_distance(houses: List[int]) -> int:
    houses = sorted(houses)
    median = houses[len(houses) // 2]
    total = 0
    for house in houses:
        total += abs(house - median)
    return total


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    t = int(next(it))
    output_lines = []
    for _ in range(t):
        r = int(next(it))
        houses = [int(next(it)) for _ in range(r)]
        output_lines.append(str(best_meeting_distance(houses)))

    sys.stdout.write("\n".join(output_lines))


if __name__ == "__main__":
    main()

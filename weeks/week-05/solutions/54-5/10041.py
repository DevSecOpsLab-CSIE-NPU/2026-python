import sys
from typing import List


def best_meeting_distance(houses: List[int]) -> int:
    sorted_houses = sorted(houses)
    median = sorted_houses[len(sorted_houses) // 2]
    return sum(abs(x - median) for x in sorted_houses)


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    t = int(next(it))
    results = []
    for _ in range(t):
        r = int(next(it))
        houses = [int(next(it)) for _ in range(r)]
        results.append(str(best_meeting_distance(houses)))

    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    main()

import sys
from typing import List


def hartal_lost_days(n: int, parameters: List[int]) -> int:
    lost_days = set()
    for h in parameters:
        day = h
        while day <= n:
            if day % 7 != 6 and day % 7 != 0:
                lost_days.add(day)
            day += h
    return len(lost_days)


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    t = int(next(it))
    results = []
    for _ in range(t):
        n = int(next(it))
        p = int(next(it))
        parameters = [int(next(it)) for _ in range(p)]
        results.append(str(hartal_lost_days(n, parameters)))

    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    main()

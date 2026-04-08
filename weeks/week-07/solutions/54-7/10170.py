import sys


def cumulative_days(start: int, current: int) -> int:
    return current * (current + 1) // 2 - (start - 1) * start // 2


def group_size_on_day(start: int, day: int) -> int:
    low = start
    high = start
    while cumulative_days(start, high) < day:
        high *= 2

    while low < high:
        mid = (low + high) // 2
        if cumulative_days(start, mid) >= day:
            high = mid
        else:
            low = mid + 1

    return low


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 2:
            continue
        start, day = map(int, parts)
        print(group_size_on_day(start, day))


if __name__ == "__main__":
    main()

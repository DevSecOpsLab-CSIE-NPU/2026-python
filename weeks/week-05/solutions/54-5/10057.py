import sys
from typing import List, Tuple


def median_password(values: List[int]) -> Tuple[int, int, int]:
    sorted_values = sorted(values)
    n = len(sorted_values)
    if n == 0:
        return 0, 0, 0

    if n % 2 == 1:
        a = sorted_values[n // 2]
        count = sorted_values.count(a)
        ways = 1
    else:
        low = sorted_values[n // 2 - 1]
        high = sorted_values[n // 2]
        a = low
        count = sorted_values.count(a)
        ways = high - low + 1

    return a, count, ways


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    out_lines: List[str] = []
    while True:
        try:
            n = int(next(it))
        except StopIteration:
            break
        if n == 0:
            break
        values = [int(next(it)) for _ in range(n)]
        a, count, ways = median_password(values)
        out_lines.append(f"{a} {count} {ways}")

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()

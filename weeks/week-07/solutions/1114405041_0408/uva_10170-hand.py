import sys


def hotel_group_size(start_size: int, target_day: int) -> int:
    base_days = start_size * (start_size - 1) // 2
    goal = target_day + base_days

    left = start_size
    right = start_size
    while right * (right + 1) // 2 < goal:
        right *= 2

    while left < right:
        middle = (left + right) // 2
        if middle * (middle + 1) // 2 >= goal:
            right = middle
        else:
            left = middle + 1

    return left


def solve(data: str) -> str:
    lines = []

    for line in data.splitlines():
        text = line.strip()
        if not text:
            continue
        s, d = map(int, text.split())
        lines.append(str(hotel_group_size(s, d)))

    return "\n".join(lines)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
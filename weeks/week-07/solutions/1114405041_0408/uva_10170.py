import math
import sys


def find_group_size(start_size: int, target_day: int) -> int:
    """
    找最小的 n，使得 start_size + (start_size + 1) + ... + n >= target_day。

    令 T(n) = 1 + 2 + ... + n，則需求為：
    T(n) - T(start_size - 1) >= target_day
    => T(n) >= target_day + T(start_size - 1)
    """
    required_total = target_day + start_size * (start_size - 1) // 2
    estimate = (math.isqrt(1 + 8 * required_total) - 1) // 2

    while estimate * (estimate + 1) // 2 < required_total:
        estimate += 1

    return estimate


def solve(data: str) -> str:
    outputs = []

    for line in data.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        start_size, target_day = map(int, stripped.split())
        outputs.append(str(find_group_size(start_size, target_day)))

    return "\n".join(outputs)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
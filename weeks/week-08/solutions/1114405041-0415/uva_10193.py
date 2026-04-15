from __future__ import annotations

import math
import sys


def solve(data: str) -> str:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    total_cases = int(lines[0])
    index = 1
    outputs: list[str] = []

    for case_no in range(1, total_cases + 1):
        first = int(lines[index], 2)
        second = int(lines[index + 1], 2)
        index += 2

        if math.gcd(first, second) > 1:
            message = "All you need is love!"
        else:
            message = "Love is not all you need!"

        outputs.append(f"Pair #{case_no}: {message}")

    return "\n".join(outputs)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

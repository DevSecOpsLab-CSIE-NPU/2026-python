from __future__ import annotations

import math
import sys


def solve(data: str) -> str:
    """
    這題其實很直覺：
    1. 先把二進位字串轉成十進位整數。
    2. 用 gcd 找最大公因數。
    3. 如果 gcd > 1，代表兩人很有愛；否則就沒有。
    """
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    total_cases = int(lines[0])
    index = 1
    outputs: list[str] = []

    for case_no in range(1, total_cases + 1):
        first_number = int(lines[index], 2)
        second_number = int(lines[index + 1], 2)
        index += 2

        if math.gcd(first_number, second_number) > 1:
            result_text = "All you need is love!"
        else:
            result_text = "Love is not all you need!"

        outputs.append(f"Pair #{case_no}: {result_text}")

    return "\n".join(outputs)


def main() -> None:
    raw_data = sys.stdin.read()
    sys.stdout.write(solve(raw_data))


if __name__ == "__main__":
    main()

"""
UVA 10193: All You Need Is Love
"""

from __future__ import annotations

from math import gcd
import sys


def has_common_factor(binary_a: str, binary_b: str) -> bool:
    """判斷兩個二進位數字轉成整數後，是否有大於 1 的公因數。"""
    number_a = int(binary_a, 2)
    number_b = int(binary_b, 2)
    return gcd(number_a, number_b) > 1


def solve(text: str) -> str:
    """依題目格式輸出每組 Pair 的判斷結果。"""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return ""

    case_count = int(lines[0])
    outputs: list[str] = []
    index = 1

    for case_number in range(1, case_count + 1):
        binary_a = lines[index]
        binary_b = lines[index + 1]
        index += 2

        if has_common_factor(binary_a, binary_b):
            outputs.append(f"Pair #{case_number}: All you need is love!")
        else:
            outputs.append(f"Pair #{case_number}: Love is not all you need!")

    return "\n".join(outputs)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

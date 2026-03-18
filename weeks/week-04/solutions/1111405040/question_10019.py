"""
UVA 10019 - Funny Encryption Method
"""

from __future__ import annotations


def popcount(value: int) -> int:
    """計算整數二進位中 1 的個數。"""
    return bin(value).count("1")


def count_bits(decimal_value: int) -> tuple[int, int]:
    """回傳十進位與十六進位解讀後的 bit count。"""
    decimal_bits = popcount(decimal_value)
    hex_bits = popcount(int(str(decimal_value), 16))
    return decimal_bits, hex_bits


def solve(text: str) -> str:
    """依題目格式輸出每筆資料的兩個 bit count。"""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return ""

    case_count = int(lines[0])
    values = [int(line) for line in lines[1 : 1 + case_count]]
    return "\n".join(f"{first} {second}" for first, second in (count_bits(value) for value in values))


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

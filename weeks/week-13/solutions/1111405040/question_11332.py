"""
UVA 11332 Summing Digits。
"""

from __future__ import annotations


def digital_root(number: int) -> int:
    """反覆把各位數字相加，直到只剩一位數。"""
    current = number
    while current >= 10:
        current = sum(int(digit) for digit in str(current))
    return current


def solve(data: str) -> str:
    """處理多筆輸入，遇到 0 結束。"""
    outputs: list[str] = []
    for token in data.split():
        number = int(token)
        if number == 0:
            break
        outputs.append(str(digital_root(number)))
    return "\n".join(outputs)


def main() -> None:
    """讀取標準輸入並輸出答案。"""
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

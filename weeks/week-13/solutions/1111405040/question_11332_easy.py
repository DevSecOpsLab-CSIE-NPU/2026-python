"""
UVA 11332 Summing Digits 簡單版。
"""

from __future__ import annotations


def root(number: int) -> int:
    """用 while 反覆把數字壓成一位數。"""
    while number >= 10:
        total = 0
        for digit in str(number):
            total += int(digit)
        number = total
    return number


def solve(data: str) -> str:
    """讀取到 0 為止。"""
    answers: list[str] = []
    for token in data.split():
        number = int(token)
        if number == 0:
            break
        answers.append(str(root(number)))
    return "\n".join(answers)


def main() -> None:
    """讀取標準輸入並輸出答案。"""
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

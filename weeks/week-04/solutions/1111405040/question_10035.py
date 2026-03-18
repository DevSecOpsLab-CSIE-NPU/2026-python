"""
UVA 10035 - Primary Arithmetic
"""

from __future__ import annotations


def count_carries(first: int, second: int) -> int:
    """計算兩個非負整數相加時的進位次數。"""
    carries = 0
    carry = 0

    while first > 0 or second > 0:
        digit_sum = first % 10 + second % 10 + carry
        if digit_sum >= 10:
            carries += 1
            carry = 1
        else:
            carry = 0
        first //= 10
        second //= 10

    return carries


def format_carry_result(carries: int) -> str:
    """依題目要求輸出進位次數描述。"""
    if carries == 0:
        return "No carry operation."
    if carries == 1:
        return "1 carry operation."
    return f"{carries} carry operations."


def solve(text: str) -> str:
    """處理直到 0 0 為止的多筆輸入。"""
    results: list[str] = []
    for line in text.splitlines():
        if not line.strip():
            continue
        first_text, second_text = line.split()
        first = int(first_text)
        second = int(second_text)
        if first == 0 and second == 0:
            break
        results.append(format_carry_result(count_carries(first, second)))
    return "\n".join(results)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

"""
UVA 10922 - 2 the 9s

判斷大數字字串是否為 9 的倍數，若是則計算 9-degree。
"""

from __future__ import annotations


def digit_sum(num_str: str) -> int:
    """回傳字串各位數字總和。"""
    return sum(ord(ch) - ord("0") for ch in num_str)


def get_9_degree(num_str: str) -> int:
    """若為 9 的倍數，回傳 9-degree；否則回傳 0。"""
    first_sum = digit_sum(num_str)
    if first_sum % 9 != 0:
        return 0

    degree = 1
    current = first_sum

    # 反覆做位數和，直到變成單位數 9。
    while current != 9:
        current = digit_sum(str(current))
        degree += 1

    return degree


def solve_line(num_str: str) -> str:
    degree = get_9_degree(num_str)
    if degree == 0:
        return f"{num_str} is not a multiple of 9."
    return f"9-degree of {num_str} is {degree}."


def solve_io(data: str) -> str:
    out: list[str] = []
    for line in data.splitlines():
        s = line.strip()
        if not s:
            continue
        if s == "0":
            break
        out.append(solve_line(s))
    return "\n".join(out)


def main() -> None:
    import sys

    sys.stdout.write(solve_io(sys.stdin.read()))


if __name__ == "__main__":
    main()

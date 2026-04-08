"""
UVA 10101: Bangla Numbers
"""

from __future__ import annotations

import sys


def bangla_parts(number: int) -> list[str]:
    """把數字拆成 Bangla 單位片段。"""
    if number >= 10_000_000:
        parts = bangla_parts(number // 10_000_000)
        parts.append("kuti")
        remainder = number % 10_000_000
        if remainder:
            parts.extend(bangla_parts(remainder))
        return parts

    parts: list[str] = []
    units = (
        (100_000, "lakh"),
        (1_000, "hajar"),
        (100, "shata"),
    )

    for unit_value, unit_name in units:
        count = number // unit_value
        if count:
            parts.append(str(count))
            parts.append(unit_name)
            number %= unit_value

    if number:
        parts.append(str(number))

    return parts


def format_bangla(number: int) -> str:
    """把整數轉成題目要求的 Bangla 格式。"""
    if number == 0:
        return "0"
    return " ".join(bangla_parts(number))


def solve(text: str) -> str:
    """逐行處理數字並加上題目要求的案例編號。"""
    answers: list[str] = []

    case_number = 1
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        number = int(line)
        answers.append(f"{case_number:>4}. {format_bangla(number)}")
        case_number += 1

    return "\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

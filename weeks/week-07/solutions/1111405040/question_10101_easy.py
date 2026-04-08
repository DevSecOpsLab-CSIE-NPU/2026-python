"""
UVA 10101: Bangla Numbers（簡單版）
"""

from __future__ import annotations

import sys


def format_number(number: int) -> str:
    """用遞迴處理重複出現的 kuti。"""
    if number == 0:
        return "0"

    def build(value: int) -> list[str]:
        if value >= 10_000_000:
            left = build(value // 10_000_000)
            left.append("kuti")
            remain = value % 10_000_000
            if remain:
                left.extend(build(remain))
            return left

        parts: list[str] = []
        for unit, name in ((100_000, "lakh"), (1_000, "hajar"), (100, "shata")):
            count = value // unit
            if count:
                parts.append(str(count))
                parts.append(name)
                value %= unit

        if value:
            parts.append(str(value))
        return parts

    return " ".join(build(number))


def solve(text: str) -> str:
    """輸出帶案例編號的 Bangla 數字。"""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    output: list[str] = []

    for index, line in enumerate(lines, start=1):
        output.append(f"{index:>4}. {format_number(int(line))}")

    return "\n".join(output)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

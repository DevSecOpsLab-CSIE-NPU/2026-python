"""UVA 10035 - Primary Arithmetic

逐行讀入兩個整數，計算相加時的進位次數。
遇到 0 0 結束。
"""

from __future__ import annotations

import sys


def carry_count(a: int, b: int) -> int:
    carry = 0
    cnt = 0

    while a > 0 or b > 0:
        da = a % 10
        db = b % 10

        if da + db + carry >= 10:
            cnt += 1
            carry = 1
        else:
            carry = 0

        a //= 10
        b //= 10

    return cnt


def to_text(cnt: int) -> str:
    if cnt == 0:
        return "No carry operation."
    if cnt == 1:
        return "1 carry operation."
    return f"{cnt} carry operations."


def solve(data: str) -> str:
    out = []

    for raw in data.splitlines():
        line = raw.strip()
        if not line:
            continue

        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break

        out.append(to_text(carry_count(a, b)))

    return "\n".join(out)


def main() -> None:
    result = solve(sys.stdin.read())
    if result:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()

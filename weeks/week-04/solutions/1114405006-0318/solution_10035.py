"""UVA 10035 Primary Arithmetic 解答。"""

from __future__ import annotations

import sys


def count_carry(a: str, b: str) -> int:
    """計算兩個非負整數字串相加時產生的進位次數。"""
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    count = 0

    while i >= 0 or j >= 0:
        da = ord(a[i]) - ord("0") if i >= 0 else 0
        db = ord(b[j]) - ord("0") if j >= 0 else 0

        s = da + db + carry
        if s >= 10:
            carry = 1
            count += 1
        else:
            carry = 0

        i -= 1
        j -= 1

    return count


def format_output(c: int) -> str:
    """依題目格式回傳 carry 敘述字串。"""
    if c == 0:
        return "No carry operation."
    if c == 1:
        return "1 carry operation."
    return f"{c} carry operations."


def solve(data: str) -> str:
    """
    讀取多組兩整數資料，直到 `0 0`。
    每組輸出一行 carry 結果。
    """
    outputs: list[str] = []

    for raw in data.splitlines():
        line = raw.strip()
        if not line:
            continue

        a, b = line.split()
        if a == "0" and b == "0":
            break

        outputs.append(format_output(count_carry(a, b)))

    if not outputs:
        return ""

    return "\n".join(outputs) + "\n"


def main() -> None:
    """標準輸入輸出入口。"""
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

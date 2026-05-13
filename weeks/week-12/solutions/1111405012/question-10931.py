"""UVA 10931 - Parity"""

from __future__ import annotations

import sys


def format_binary_parity(number: int) -> tuple[str, int]:
    """回傳二進位字串與其中 1 的個數。"""

    binary_text = format(number, "b")
    return binary_text, binary_text.count("1")


def describe_number(number: int) -> str:
    """把單筆結果轉為題目輸出格式。"""

    binary_text, count = format_binary_parity(number)
    return f"The parity of {binary_text} is {count} (mod 2)."


def solve() -> None:
    """讀取整數直到 0，並輸出每筆結果。"""

    outputs: list[str] = []
    for token in sys.stdin.read().split():
        number = int(token)
        if number == 0:
            break
        outputs.append(describe_number(number))
    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    solve()

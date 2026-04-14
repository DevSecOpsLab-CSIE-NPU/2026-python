"""
UVA 10222: Decode the Mad man
"""

from __future__ import annotations

import sys


KEYBOARD = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
DECODE_MAP = {KEYBOARD[index]: KEYBOARD[index - 2] for index in range(2, len(KEYBOARD))}


def decode_text(text: str) -> str:
    """依鍵盤位置向左移兩格解碼。"""
    decoded: list[str] = []

    for char in text:
        lower_char = char.lower()
        decoded.append(DECODE_MAP.get(lower_char, char))

    return "".join(decoded)


def solve(text: str) -> str:
    """保留換行與空白，只轉換可解碼字元。"""
    return decode_text(text)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

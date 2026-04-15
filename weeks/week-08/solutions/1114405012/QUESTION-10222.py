"""UVA 10222 - Decode the Mad man

正式版：把輸入字元映射到鍵盤同一列左邊 1 鍵。
"""

from __future__ import annotations

import sys

ROWS = [
    "`1234567890-=",
    "qwertyuiop[]\\",
    "asdfghjkl;'",
    "zxcvbnm,./",
]


def decode_char(ch: str) -> str:
    """將單一字元解碼；不在鍵盤表內的字元原樣輸出。"""
    is_upper = ch.isalpha() and ch.isupper()
    target = ch.lower() if is_upper else ch

    for row in ROWS:
        pos = row.find(target)
        if pos != -1:
            if pos == 0:
                decoded = row[0]
            else:
                decoded = row[pos - 1]
            return decoded.upper() if is_upper else decoded

    return ch


def solve(raw_input: str) -> str:
    return "".join(decode_char(ch) for ch in raw_input)


def main() -> None:
    data = sys.stdin.read()
    if not data:
        return
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()

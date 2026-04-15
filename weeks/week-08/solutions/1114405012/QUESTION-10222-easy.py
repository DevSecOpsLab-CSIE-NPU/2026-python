"""UVA 10222 - Decode the Mad man（easy 版）

直覺版：
- 先準備每一排鍵盤字串。
- 對每個字元，找到它在該排的位置，改成左邊 1 格。
- 找不到就原樣輸出（例如空白、換行）。
"""

from __future__ import annotations

import sys

KEYBOARD_ROWS = [
    "`1234567890-=",
    "qwertyuiop[]\\",
    "asdfghjkl;'",
    "zxcvbnm,./",
]


def decode_one(ch: str) -> str:
    """解碼一個字元。"""
    upper = ch.isalpha() and ch.isupper()
    x = ch.lower() if upper else ch

    for row in KEYBOARD_ROWS:
        idx = row.find(x)
        if idx != -1:
            # 最左邊沒有更左的鍵，保留自身。
            y = row[idx - 1] if idx > 0 else row[idx]
            return y.upper() if upper else y

    return ch


def solve(raw_input: str) -> str:
    return "".join(decode_one(ch) for ch in raw_input)


def main() -> None:
    data = sys.stdin.read()
    if not data:
        return
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()

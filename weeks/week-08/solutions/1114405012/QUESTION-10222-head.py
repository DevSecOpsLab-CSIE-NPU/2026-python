"""UVA 10222 - Decode the Mad man（手打版）

題意是把輸入字元映射回鍵盤左邊一格。
這題最直覺就是「每排找位置，再往左取」。
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
    """解碼單一字元。"""
    is_upper = ch.isalpha() and ch.isupper()
    target = ch.lower() if is_upper else ch

    for row in ROWS:
        idx = row.find(target)
        if idx != -1:
            # 在最左邊時沒有左鍵，保留原鍵。
            decoded = row[idx - 1] if idx > 0 else row[idx]
            return decoded.upper() if is_upper else decoded

    # 不是鍵盤字元（例如空白、換行）原樣輸出。
    return ch


def solve(data: str) -> str:
    return "".join(decode_char(ch) for ch in data)


def main() -> None:
    raw = sys.stdin.read()
    if not raw:
        return
    sys.stdout.write(solve(raw))


if __name__ == "__main__":
    main()

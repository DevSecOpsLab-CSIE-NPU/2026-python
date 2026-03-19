#!/usr/bin/env python3
"""UVA 272 - TEX Quotes.

將一般雙引號 \\" 依序替換成 `` 與 ''。
"""

from __future__ import annotations

import sys


def main() -> None:
    text = sys.stdin.read()
    use_left_quote = True
    output_chars: list[str] = []

    for ch in text:
        if ch == '"':
            if use_left_quote:
                output_chars.append("``")
            else:
                output_chars.append("''")
            use_left_quote = not use_left_quote
        else:
            output_chars.append(ch)

    sys.stdout.write("".join(output_chars))


if __name__ == "__main__":
    main()

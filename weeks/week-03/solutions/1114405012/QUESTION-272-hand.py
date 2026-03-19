#!/usr/bin/env python3
"""UVA 272 手打版。

把一般雙引號依序替換成 `` 與 ''。
"""

import sys


def main() -> None:
    text = sys.stdin.read()

    open_quote = True
    out: list[str] = []

    for ch in text:
        if ch == '"':
            if open_quote:
                out.append("``")
            else:
                out.append("''")
            open_quote = not open_quote
        else:
            out.append(ch)

    sys.stdout.write("".join(out))


if __name__ == "__main__":
    main()

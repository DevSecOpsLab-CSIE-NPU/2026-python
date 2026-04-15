"""
UVA 272 - TEX Quotes (manual version)

Replace every double quote character (") alternately with:
  1st, 3rd, 5th... -> ``
  2nd, 4th, 6th... -> ''
All other characters must remain unchanged.
"""

from __future__ import annotations

import sys


def convert_tex_quotes(text: str, is_open: bool = True) -> tuple[str, bool]:
    out: list[str] = []

    for ch in text:
        if ch == '"':
            if is_open:
                out.append("``")
            else:
                out.append("''")
            is_open = not is_open
        else:
            out.append(ch)

    return "".join(out), is_open


def convert_lines(lines: list[str]) -> list[str]:
    is_open = True
    result: list[str] = []

    for line in lines:
        converted, is_open = convert_tex_quotes(line, is_open)
        result.append(converted)

    return result


def main() -> None:
    is_open = True

    for raw_line in sys.stdin:
        line = raw_line.rstrip("\n")
        converted, is_open = convert_tex_quotes(line, is_open)
        print(converted)


if __name__ == "__main__":
    main()

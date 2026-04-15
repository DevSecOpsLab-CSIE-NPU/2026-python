"""UVA 272 - TeX Quotes, easy version with Chinese comments."""

from __future__ import annotations

import sys


def solve(input_text: str) -> str:
    # 第一個雙引號要換成 ``，第二個要換成 ''，所以用開關切換
    open_quote = True
    output_parts: list[str] = []

    for char in input_text:
        if char == '"':
            output_parts.append("``" if open_quote else "''")
            open_quote = not open_quote
        else:
            output_parts.append(char)

    return "".join(output_parts)


def main() -> None:
    data = sys.stdin.read()
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()
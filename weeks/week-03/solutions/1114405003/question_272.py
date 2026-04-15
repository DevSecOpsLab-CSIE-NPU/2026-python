from __future__ import annotations

import sys


def solve(input_text: str) -> str:
    open_quote = True
    parts: list[str] = []
    for char in input_text:
        if char == '"':
            parts.append("``" if open_quote else "''")
            open_quote = not open_quote
        else:
            parts.append(char)
    return "".join(parts)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
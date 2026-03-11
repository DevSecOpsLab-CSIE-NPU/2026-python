"""UVA 272 - TEX Quotes"""

import sys


def solve(text: str) -> str:
    is_open_quote = True
    result = []

    for ch in text:
        if ch != '"':
            result.append(ch)
            continue

        if is_open_quote:
            result.append("``")
        else:
            result.append("''")
        is_open_quote = not is_open_quote

    return "".join(result)


if __name__ == "__main__":
    print(solve(sys.stdin.read()), end="")

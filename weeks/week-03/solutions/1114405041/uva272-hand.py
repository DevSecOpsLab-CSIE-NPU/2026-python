"""UVA 272 - TEX Quotes."""

import sys


def main() -> None:
    text = sys.stdin.read()
    open_quote = True
    out = []

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

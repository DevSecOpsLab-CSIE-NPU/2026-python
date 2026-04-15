"""
UVA 10222 - Decode the Mad man
手打版本
"""

import sys


def make_table() -> dict[str, str]:
    lines = [
        "`1234567890-=",
        "qwertyuiop[]\\",
        "asdfghjkl;'",
        "zxcvbnm,./",
    ]

    table: dict[str, str] = {}

    for row in lines:
        for i in range(1, len(row)):
            a = row[i]
            b = row[i - 1]
            table[a] = b
            table[a.upper()] = b.upper()

    return table


def run(text: str) -> str:
    table = make_table()
    ret = []

    for ch in text:
        ret.append(table.get(ch, ch))

    return "".join(ret)


def main() -> None:
    text = sys.stdin.read()
    print(run(text), end="")


if __name__ == "__main__":
    main()

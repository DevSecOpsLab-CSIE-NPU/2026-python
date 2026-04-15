"""UVA 10222 - 手打版本。"""

import sys


def build_table():
    keys = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
    table = {}
    for i in range(1, len(keys)):
        table[keys[i]] = keys[i - 1]
    return table


TRANS = build_table()


def solve(data: str) -> str:
    out = []
    for ch in data:
        low = ch.lower()
        if low in TRANS:
            mapped = TRANS[low]
            out.append(mapped.upper() if ch.isupper() else mapped)
        else:
            out.append(ch)
    return "".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()), end="")

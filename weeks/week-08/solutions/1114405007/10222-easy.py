"""UVA 10222 - easy 版本（含中文註解）。"""

import sys

KEYBOARD = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
MAP_LOWER = {KEYBOARD[i]: KEYBOARD[i - 1] for i in range(1, len(KEYBOARD))}


def decode_char(ch: str) -> str:
    lower = ch.lower()
    if lower not in MAP_LOWER:
        return ch

    decoded = MAP_LOWER[lower]
    if ch.isupper():
        return decoded.upper()
    return decoded


def solve(data: str) -> str:
    return "".join(decode_char(ch) for ch in data)


if __name__ == "__main__":
    print(solve(sys.stdin.read()), end="")

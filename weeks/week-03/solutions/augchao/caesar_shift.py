"""Letter shift cipher for line-by-line input.

Set SHIFT to your student ID last digit before submitting, or pass it as the
first command-line argument.
"""

from __future__ import annotations

import sys


def shift_char(ch: str, shift: int) -> str:
    """Shift one alphabetic character, preserving case."""
    if "A" <= ch <= "Z":
        base = ord("A")
        return chr((ord(ch) - base + shift) % 26 + base)
    if "a" <= ch <= "z":
        base = ord("a")
        return chr((ord(ch) - base + shift) % 26 + base)
    return ch


def encrypt_line(text: str, shift: int) -> str:
    """Encrypt one line by shifting only English letters."""
    return "".join(shift_char(ch, shift) for ch in text)


def main() -> None:
    shift = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    for line in sys.stdin:
        print(encrypt_line(line.rstrip("\n"), shift))


if __name__ == "__main__":
    main()
"""Week 18 Q2: Caesar cipher.

Shift every English letter forward by the student-specific shift.
Non-letters stay unchanged.
"""

from __future__ import annotations

import sys


SHIFT = 3


def caesar_cipher(text: str, shift: int) -> str:
    """Encrypt text with a Caesar shift."""

    result = []
    shift %= 26
    for char in text:
        if "a" <= char <= "z":
            offset = (ord(char) - ord("a") + shift) % 26
            result.append(chr(ord("a") + offset))
        elif "A" <= char <= "Z":
            offset = (ord(char) - ord("A") + shift) % 26
            result.append(chr(ord("A") + offset))
        else:
            result.append(char)
    return "".join(result)


def solve(data: str) -> str:
    return "\n".join(caesar_cipher(line, SHIFT) for line in data.splitlines())


def main() -> None:
    output = solve(sys.stdin.read())
    if output:
        sys.stdout.write(output + "\n")


if __name__ == "__main__":
    main()
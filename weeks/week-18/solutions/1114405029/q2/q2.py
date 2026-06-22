"""Q2 Caesar Cipher."""

import sys


def shift_char(ch, shift):
    """位移單一英文字母，非英文字母原樣回傳。"""
    shift %= 26
    if "A" <= ch <= "Z":
        return chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
    if "a" <= ch <= "z":
        return chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
    return ch


def caesar_line(line, shift):
    """處理一整行 Caesar cipher。"""
    return "".join(shift_char(ch, shift) for ch in line)


def solve(input_text, shift=10):
    """逐行處理直到 EOF。"""
    return "\n".join(caesar_line(line, shift) for line in input_text.splitlines())


if __name__ == "__main__":
    print(solve(sys.stdin.read()))

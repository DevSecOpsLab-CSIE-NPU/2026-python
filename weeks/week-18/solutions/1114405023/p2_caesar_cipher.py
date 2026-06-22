"""
第二題：凱撒密碼 Caesar Cipher
學號後兩碼 23，個位數 u = 3，所以 SHIFT = 4。

需求：
1. 讀取多行文字直到 EOF。
2. 大寫 A-Z 依 SHIFT 位移並循環。
3. 小寫 a-z 依 SHIFT 位移並循環。
4. 非英文字母保持不變。
"""

import sys

SHIFT = 4


def shift_char(ch, shift=SHIFT):
    """位移單一字元；非英文字母保持不變。"""
    if "A" <= ch <= "Z":
        return chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))

    if "a" <= ch <= "z":
        return chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))

    return ch


def caesar_cipher(text, shift=SHIFT):
    """對整段文字套用凱撒位移。"""
    return "".join(shift_char(ch, shift) for ch in text)


def solve(input_text):
    """處理 EOF 前所有輸入。"""
    return caesar_cipher(input_text)


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

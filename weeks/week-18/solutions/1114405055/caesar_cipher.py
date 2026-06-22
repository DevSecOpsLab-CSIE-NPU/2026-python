# -*- coding: utf-8 -*-
"""
凱撒密碼（Caesar Cipher）
學號 1114405055 的參數：SHIFT = 6
輸入：多行字串，讀到 EOF 為止
輸出：每行對應的加密結果
"""
import sys

SHIFT = 6


def shift_char(ch: str, shift: int) -> str:
    """單一字元位移：大寫在 A-Z、小寫在 a-z 內循環，非英文字母原樣回傳"""
    if 'a' <= ch <= 'z':
        return chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    if 'A' <= ch <= 'Z':
        return chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    return ch


def encrypt_line(line: str, shift: int) -> str:
    """對整行逐字元套用 shift_char 後組回字串"""
    return ''.join(shift_char(ch, shift) for ch in line)


def main() -> None:
    """讀 stdin 直到 EOF，每行加密後印出"""
    for line in sys.stdin:
        print(encrypt_line(line.rstrip('\n'), SHIFT))


if __name__ == '__main__':
    main()

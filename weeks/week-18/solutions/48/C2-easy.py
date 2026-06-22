"""
凱撒密碼 (Caesar Cipher) — AI 詳細註解版

功能：
    將每行字串中的英文字母向後位移 SHIFT=9 位。
    大寫在 A-Z 內循環，小寫在 a-z 內循環。
    非英文字元（空白、數字、標點）原樣保留。

時間複雜度：O(N)，N 為所有字元總數
空間複雜度：O(N)，儲存輸出字串
"""

import sys

SHIFT = 9  # 我的專屬位移量（學號末碼計算得來）


def encrypt_char(ch: str) -> str:
    """將單一字元加密：大寫/小寫字母位移，其餘不動。"""
    if 'A' <= ch <= 'Z':
        # 大寫：計算相對 A 的偏移，加 SHIFT，對 26 取模，再加回 A
        return chr((ord(ch) - ord('A') + SHIFT) % 26 + ord('A'))
    if 'a' <= ch <= 'z':
        # 小寫：同理，用 a 為基準
        return chr((ord(ch) - ord('a') + SHIFT) % 26 + ord('a'))
    # 非英文字元：直接保留
    return ch


def main():
    """讀取 stdin 所有行，逐行加密並輸出。"""
    lines = sys.stdin.read().splitlines()  # 保留空行，不 trim
    for line in lines:
        encrypted = ''.join(encrypt_char(c) for c in line)
        print(encrypted)


if __name__ == "__main__":
    main()

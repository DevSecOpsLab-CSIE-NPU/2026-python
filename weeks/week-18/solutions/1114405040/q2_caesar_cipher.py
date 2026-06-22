"""Question 2: Caesar Cipher.

學號末兩碼為 40，個位數 u = 0，
所以 SHIFT = u % 25 + 1 = 1。
"""

SHIFT = 1


def caesar_cipher(line):
    """將一行文字中的英文字母向右位移 SHIFT，其他字元保持原樣。"""
    result = []

    for char in line:
        if "A" <= char <= "Z":
            # 大寫字母以 A 為起點，超過 Z 時用 % 26 循環回 A。
            base = ord("A")
            shifted = (ord(char) - base + SHIFT) % 26 + base
            result.append(chr(shifted))
        elif "a" <= char <= "z":
            # 小寫字母以 a 為起點，超過 z 時用 % 26 循環回 a。
            base = ord("a")
            shifted = (ord(char) - base + SHIFT) % 26 + base
            result.append(chr(shifted))
        else:
            # 空白、數字、標點符號與換行都不改變。
            result.append(char)

    return "".join(result)


def main():
    import sys

    # 逐行讀取直到 EOF，不輸出任何提示文字。
    for line in sys.stdin:
        sys.stdout.write(caesar_cipher(line))


if __name__ == "__main__":
    main()

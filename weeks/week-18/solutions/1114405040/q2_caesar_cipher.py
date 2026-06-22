"""Question 2: Caesar Cipher.

學號末兩碼為 40，個位數 u = 0，
所以 SHIFT = u % 25 + 1 = 1。
"""

SHIFT = 1

SAMPLE_INPUT = """Hello, NPU!
abc XYZ
Zz 123!?
"""


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

    # 右上角直接執行時沒有測資輸入，使用範例資料避免程式一直等待。
    # 正式測試或線上評測用重新導向輸入時，仍逐行讀取標準輸入。
    if sys.stdin.isatty():
        lines = SAMPLE_INPUT.splitlines(keepends=True)
    else:
        lines = sys.stdin

    for line in lines:
        sys.stdout.write(caesar_cipher(line))


if __name__ == "__main__":
    main()

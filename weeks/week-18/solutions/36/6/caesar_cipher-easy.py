"""
簡易版凱薩密碼（Caesar Cipher）

說明：本版本使用 7 位元移位，並保留所有非英文字元。

輸入：可讀取多行標準輸入，逐行輸出加密結果。

使用方式：
    python caesar_cipher-easy.py < input.txt
"""


def shift_char_easy(ch: str, shift: int = 7) -> str:
    """將單一字元按照凱薩加密規則轉換。

    - 大寫字母 A-Z 向後移動 shift 位；超過 Z 則從 A 循環。
    - 小寫字母 a-z 同理。
    - 其他字元（數字、標點、空白）保持原樣。
    """
    if 'A' <= ch <= 'Z':
        base = ord('A')
        new_char = chr((ord(ch) - base + shift) % 26 + base)
        return new_char
    if 'a' <= ch <= 'z':
        base = ord('a')
        new_char = chr((ord(ch) - base + shift) % 26 + base)
        return new_char
    return ch


def encrypt_line_easy(line: str) -> str:
    """將一行文字中的每個字元進行加密並回傳結果。"""
    result = ''
    for ch in line:
        result += shift_char_easy(ch)
    return result


def main() -> None:
    """從標準輸入讀取多行，逐行輸出加密後結果。"""
    try:
        while True:
            line = input()
            print(encrypt_line_easy(line))
    except EOFError:
        pass


if __name__ == '__main__':
    main()

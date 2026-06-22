"""
簡易版凱薩密碼程式

這個版本使用固定的 7 位移量，適合用來理解基本的字母輪轉邏輯。
"""

def shift_char_easy(ch: str, shift: int = 7) -> str:
    """將單一字元按照凱薩移位加密。"""
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

    result = ''
    for ch in line:
        result += shift_char_easy(ch)
    return result


def main() -> None:

    try:
        while True:
            line = input()
            print(encrypt_line_easy(line))
    except EOFError:
        pass


if __name__ == '__main__':
    main()

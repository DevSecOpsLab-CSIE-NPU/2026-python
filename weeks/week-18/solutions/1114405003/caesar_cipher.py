"""
第二題 凱撒密碼 (Caesar Cipher)
學號: 1114405003
SHIFT = 4 (個位 3 % 25 + 1 = 4)

規則：
- 大寫在 A-Z 內循環
- 小寫在 a-z 內循環
- 非英文字母字元原樣保留
"""


def caesar_cipher(text: str, shift: int) -> str:
    """
    凱撒密碼加密函式

    Args:
        text: 要加密的字串
        shift: 位移量

    Returns:
        加密後的字串
    """
    result = []

    for char in text:
        if 'A' <= char <= 'Z':
            # 大寫字元：A=0, B=1, ..., Z=25
            original = ord(char) - ord('A')
            shifted = (original + shift) % 26
            result.append(chr(shifted + ord('A')))
        elif 'a' <= char <= 'z':
            # 小寫字元：a=0, b=1, ..., z=25
            original = ord(char) - ord('a')
            shifted = (original + shift) % 26
            result.append(chr(shifted + ord('a')))
        else:
            # 非字母字元：原樣保留
            result.append(char)

    return ''.join(result)


def main():
    """主程式：讀取多行輸入並輸出加密結果"""
    SHIFT = 4  # 學號 1114405003, 個位 3 % 25 + 1 = 4

    results = []

    try:
        while True:
            line = input()
            encrypted = caesar_cipher(line, SHIFT)
            results.append(encrypted)
    except EOFError:
        pass

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

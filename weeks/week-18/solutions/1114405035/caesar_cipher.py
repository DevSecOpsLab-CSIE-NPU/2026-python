import sys

def caesar_cipher_encrypt(text: str, shift: int) -> str:
    """
    手打版本 - 凱撒密碼加密：
    大寫 A-Z、小寫 a-z 依位移量進行循環位移，其餘字元原樣輸出。
    """
    shift = shift % 26
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - 97 + shift) % 26 + 97))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - 65 + shift) % 26 + 65))
        else:
            result.append(char)
    return "".join(result)

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        stripped_line = line.rstrip('\r\n')
        encrypted_line = caesar_cipher_encrypt(stripped_line, 6)
        print(encrypted_line)

if __name__ == '__main__':
    main()

import sys

SHIFT = 2


def shift_char(ch, shift):
    # 大寫字母在 A-Z 之間循環位移
    if "A" <= ch <= "Z":
        return chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))

    # 小寫字母在 a-z 之間循環位移
    if "a" <= ch <= "z":
        return chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))

    # 其他字元原樣保留
    return ch


def encrypt_line(text):
    result = []
    for ch in text:
        result.append(shift_char(ch, SHIFT))
    return "".join(result)


def main():
    for line in sys.stdin:
        print(encrypt_line(line.rstrip("\n")))


if __name__ == "__main__":
    main()
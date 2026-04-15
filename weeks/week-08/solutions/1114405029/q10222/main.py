import sys


def build_mapping():
    # 依照題目給的 QWERTY 鍵盤排列建立映射表
    rows = [
        "`1234567890-=",
        "qwertyuiop[]\\",
        "asdfghjkl;'",
        "zxcvbnm,./"
    ]

    mapping = {}

    for row in rows:
        for i in range(1, len(row)):
            mapping[row[i]] = row[i - 1]

    return mapping


def decode_text(text, mapping):
    # 題目常見資料以小寫為主，先統一轉成小寫處理較穩定
    text = text.lower()

    result = []

    for ch in text:
        if ch == " ":
            result.append(" ")
        else:
            result.append(mapping.get(ch, ch))

    return "".join(result)


def main():
    mapping = build_mapping()
    lines = sys.stdin.read().splitlines()

    outputs = [decode_text(line, mapping) for line in lines]
    print("\n".join(outputs))


if __name__ == "__main__":
    main()
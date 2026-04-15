import sys


def build_mapping():
    # 把鍵盤每一排照原本順序寫出來
    rows = [
        "`1234567890-=",
        "qwertyuiop[]\\",
        "asdfghjkl;'",
        "zxcvbnm,./"
    ]

    # 用字典記錄「某個字元解碼後會變成什麼」
    mapping = {}

    # 例如在同一排中：
    # row[i] 會對應到 row[i - 1]
    # 因為題目是手偏右，所以解碼時要往左找
    for row in rows:
        for i in range(1, len(row)):
            mapping[row[i]] = row[i - 1]

    return mapping


def decode_text(text, mapping):
    # 為了穩定處理，先轉成小寫
    text = text.lower()

    result = []

    # 逐字元解碼
    for ch in text:
        # 空白直接保留
        if ch == " ":
            result.append(" ")
        else:
            # 其他字元就查表
            # 如果剛好不在表裡，就原樣保留
            result.append(mapping.get(ch, ch))

    return "".join(result)


def main():
    mapping = build_mapping()

    # 這題可能有多行輸入，所以要全部讀進來
    lines = sys.stdin.read().splitlines()

    outputs = []

    for line in lines:
        outputs.append(decode_text(line, mapping))

    print("\n".join(outputs))


if __name__ == "__main__":
    main()
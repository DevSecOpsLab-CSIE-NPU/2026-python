import sys


def main():
    # 依照題目的 QWERTY 鍵盤排列建立對照表
    rows = [
        "`1234567890-=",
        "qwertyuiop[]\\",
        "asdfghjkl;'",
        "zxcvbnm,./",
    ]

    decode = {}
    for row in rows:
        # 每個字元都對應到左邊一格
        for index in range(1, len(row)):
            decode[row[index]] = row[index - 1]

    # 直接整段讀進來，保留所有空白與換行
    text = sys.stdin.read()
    result = []

    for ch in text:
        # 空白和換行都要保留
        result.append(decode.get(ch, ch))

    sys.stdout.write(''.join(result))


if __name__ == '__main__':
    main()

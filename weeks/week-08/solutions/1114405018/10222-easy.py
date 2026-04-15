import sys


def build_map():
    """建立鍵盤字元對照表：每個字元對應到左邊三格的位置。"""

    # 題目給的 QWERTY 鍵盤排列
    rows = [
        "`1234567890-=",
        "qwertyuiop[]\\",
        "asdfghjkl;'",
        "zxcvbnm,./",
    ]

    table = {" ": " "}

    # 這題的規則其實就是「看到哪個字元，就換成它左邊的字元」
    for row in rows:
        for i in range(1, len(row)):
            table[row[i]] = row[i - 1]

    return table


def solve(text):
    """把輸入文字逐字解碼後輸出。"""

    table = build_map()
    out = []

    # 題目輸入是一整行或多行文字，直接逐行處理最簡單
    for line in text.splitlines():
        out.append("".join(table.get(ch, ch) for ch in line))

    return "\n".join(out)


def main():
    """競賽模式入口：讀標準輸入，印出答案。"""

    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
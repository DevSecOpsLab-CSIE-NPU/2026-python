"""UVA 490 - 好記版本（-easy）。

簡化記法：
1. 找最長行長 max_len
2. 針對每個欄位 c，從最後一行往前拿字元
3. 沒字元就補空白
"""


def main() -> None:
    import sys

    # 只拿掉換行，不動行內空白與符號。
    arr = [line.rstrip("\n") for line in sys.stdin]
    if not arr:
        return

    max_len = max(len(s) for s in arr)

    for c in range(max_len):
        out = []
        for r in range(len(arr) - 1, -1, -1):
            if c < len(arr[r]):
                out.append(arr[r][c])
            else:
                out.append(" ")

        # 詳細註解：
        # 旋轉後每列右側若只剩補齊用空白，不影響矩陣結構，
        # 但會讓輸出檢視不直覺，所以把尾端空白去掉。
        print("".join(out).rstrip())


if __name__ == "__main__":
    main()

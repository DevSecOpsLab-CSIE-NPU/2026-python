"""UVA 490 簡單版本（含繁體中文註解）。"""

import sys


def solve(text):
    # 如果完全沒有輸入，直接回傳空字串
    if text == "":
        return ""

    # 把輸入切成多行，不保留每行結尾的換行符號
    lines = text.splitlines()

    # 如果沒有任何資料，也回傳空字串
    if not lines:
        return ""

    # 找出最長那一行的長度
    max_len = max(len(line) for line in lines)

    # 將每一行補空白到同樣長度
    padded = []
    for line in lines:
        padded.append(line.ljust(max_len))

    result = []

    # 一欄一欄往下讀，並從最後一行往上組成新的一行
    for col in range(max_len):
        row = ""
        for r in range(len(padded) - 1, -1, -1):
            row += padded[r][col]
        result.append(row)

    # 用換行連接所有結果，最後補一個換行
    return "\n".join(result) + "\n"


if __name__ == "__main__":
    data = sys.stdin.read()
    sys.stdout.write(solve(data))
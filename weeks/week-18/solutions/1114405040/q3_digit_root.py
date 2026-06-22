"""Question 3: Digit Root in Base 2.

學號末兩碼為 40，個位數 u = 0，
依照題目表格，本題 base = 2。
"""

BASE = 2

SAMPLE_INPUT = """63
0
1000000000
1
2
3
"""


def digit_sum_in_base(x, base):
    """將 x 轉成 base 進位後，回傳所有位數字的總和。"""
    if x == 0:
        return 0

    total = 0

    # 用除以 base 取餘數的方式取得每一位數字，不需要外部套件。
    while x > 0:
        total += x % base
        x //= base

    return total


def digit_root_base(x, base):
    """重複計算 base 進位的位數和，直到結果小於 base。"""
    while x >= base:
        x = digit_sum_in_base(x, base)

    return x


def main():
    import sys

    output_lines = []

    # 右上角直接執行時沒有測資輸入，使用範例資料避免程式一直等待。
    # 正式測試或線上評測用重新導向輸入時，仍逐行讀取標準輸入。
    if sys.stdin.isatty():
        lines = SAMPLE_INPUT.splitlines()
    else:
        lines = sys.stdin

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        x = int(line)
        output_lines.append(str(digit_root_base(x, BASE)))

    sys.stdout.write("\n".join(output_lines))


if __name__ == "__main__":
    main()

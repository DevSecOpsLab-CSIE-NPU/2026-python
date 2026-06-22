"""Question 3: Digit Root in Base 2.

學號末兩碼為 40，個位數 u = 0，
依照題目表格，本題 base = 2。
"""

BASE = 2


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

    # 逐行讀取直到 EOF，每行視為一個非負整數。
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            continue

        x = int(line)
        output_lines.append(str(digit_root_base(x, BASE)))

    sys.stdout.write("\n".join(output_lines))


if __name__ == "__main__":
    main()

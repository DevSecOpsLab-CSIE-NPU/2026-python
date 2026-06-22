"""
第三題：任意進位的數字根

學號後兩碼 23，所以本題 base = 3。

需求：
1. 每行輸入一個十進位非負整數，直到 EOF。
2. 將數字視為 base 進位下的數字，計算各位數字總和。
3. 重複相加，直到結果小於 base。
4. 輸出最後的數字根。
"""

import sys

BASE = 3


def sum_digits_in_base(value, base=BASE):
    """
    計算 value 在指定 base 下的各位數字總和。

    例如：
    value = 8, base = 3
    8 的三進位是 22
    所以回傳 2 + 2 = 4
    """
    if value < 0:
        raise ValueError("value must be non-negative")

    if value == 0:
        return 0

    total = 0

    while value > 0:
        total += value % base
        value //= base

    return total


def digit_root(value, base=BASE):
    """
    計算任意進位的數字根。

    Args:
        value: 十進位非負整數。
        base: 進位基底，本題固定為 3。

    Returns:
        int: 最後小於 base 的數字根。

    Raises:
        ValueError: value 為負數時拋出。
    """
    if value < 0:
        raise ValueError("value must be non-negative")

    while value >= base:
        value = sum_digits_in_base(value, base)

    return value


def solve(input_text):
    """
    處理多行輸入直到 EOF。

    空行會略過。
    每一行輸出一個數字根。
    """
    outputs = []

    for line in input_text.splitlines():
        line = line.strip()

        if line == "":
            continue

        value = int(line)
        outputs.append(str(digit_root(value)))

    return "\n".join(outputs)


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
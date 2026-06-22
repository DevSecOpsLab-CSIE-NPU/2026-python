"""
第一題：資料清理 Data Cleaning
學號後兩碼 23，個位數 u = 3，所以 D = 5。

需求：
1. 讀取多組整數序列。
2. 每組先去除重複值，保留第一次出現順序。
3. 只保留可以被 D 整除的數字。
4. 將結果由小到大排序後輸出。
5. 若結果為空，輸出 NONE。
"""

import sys

D = 5


def clean_numbers(numbers, divisor=D):
    """去除重複、保留可被 divisor 整除的數字，最後排序。"""
    seen = set()
    unique_numbers = []

    for value in numbers:
        if value not in seen:
            seen.add(value)
            unique_numbers.append(value)

    filtered = [value for value in unique_numbers if value % divisor == 0]
    return sorted(filtered)


def solve(input_text):
    """處理題目的多組輸入格式。"""
    tokens = input_text.split()
    index = 0
    outputs = []

    while index < len(tokens):
        n = int(tokens[index])
        index += 1

        if n == 0:
            break

        numbers = [int(tokens[index + i]) for i in range(n)]
        index += n

        result = clean_numbers(numbers)

        if result:
            outputs.append(" ".join(str(value) for value in result))
        else:
            outputs.append("NONE")

    return "\n".join(outputs)


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

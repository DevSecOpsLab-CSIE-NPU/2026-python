"""Question 1: Data Cleaning.

學號末兩碼為 40，個位數 u = 0，
所以 D = u % 4 + 2 = 2。
"""

D = 2


def data_cleaning(nums):
    """去除重複數字、保留可被 D 整除的數字，並依升冪排序。"""
    seen = set()
    unique_nums = []

    # 依照原本出現順序檢查，重複的數字只保留第一次出現。
    for num in nums:
        if num not in seen:
            seen.add(num)
            unique_nums.append(num)

    # 只保留可被 D 整除的數字，本題 D 固定為 2。
    filtered = []
    for num in unique_nums:
        if num % D == 0:
            filtered.append(num)

    # 題目要求最後輸出時由小到大排序。
    return sorted(filtered)


def main():
    import sys

    data = sys.stdin.buffer.read().split()
    index = 0
    output_lines = []

    # 支援多組測資與 EOF；遇到 n = 0 時結束。
    while index < len(data):
        n = int(data[index])
        index += 1

        if n == 0:
            break

        nums = []
        for _ in range(n):
            if index >= len(data):
                break
            nums.append(int(data[index]))
            index += 1

        result = data_cleaning(nums)

        if result:
            output_lines.append(" ".join(str(num) for num in result))
        else:
            output_lines.append("NONE")

    sys.stdout.write("\n".join(output_lines))


if __name__ == "__main__":
    main()

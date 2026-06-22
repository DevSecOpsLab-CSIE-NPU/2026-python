"""Q1 Data Cleaning.

依序去重、篩選可整除數字，最後排序輸出。
"""

import sys


def dedupe_keep_order(nums):
    """移除重複值，保留第一次出現的順序。"""
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


def filter_divisible(nums, d):
    """保留能被 d 整除的整數。"""
    if d == 0:
        raise ValueError("d must not be zero")
    return [num for num in nums if num % d == 0]


def clean_numbers(nums, d):
    """完成去重、篩選、遞增排序。"""
    unique_nums = dedupe_keep_order(nums)
    divisible_nums = filter_divisible(unique_nums, d)
    return sorted(divisible_nums)


def solve(input_text, d=3):
    """處理多組測資，n=0 結束。"""
    lines = input_text.splitlines()
    output_lines = []
    index = 0

    while index < len(lines):
        line = lines[index].strip()
        index += 1
        if not line:
            continue

        n = int(line)
        if n == 0:
            break
        if n < 0:
            raise ValueError("n must be non-negative")
        if index >= len(lines):
            raise ValueError("missing number line")

        nums = [int(part) for part in lines[index].split()]
        index += 1
        if len(nums) != n:
            raise ValueError("number count does not match n")

        cleaned = clean_numbers(nums, d)
        if cleaned:
            output_lines.append(" ".join(str(num) for num in cleaned))
        else:
            output_lines.append("NONE")

    return "\n".join(output_lines)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))

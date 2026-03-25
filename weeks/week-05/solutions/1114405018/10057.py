from typing import List, Tuple


def solve_case(numbers: List[int]) -> Tuple[int, int, int]:
    """
    對於一組數字，找到使絕對距離和最小的整數 A。
    
    返回：
    - A: 能使距離和最小的整數
    - count_equal_a: 有多少個數字等於 A
    - count_min_a: 有多少個不同的 A 能達到同樣最小值
    """
    if not numbers:
        return 0, 0, 0

    n = len(numbers)
    sorted_nums = sorted(numbers)

    # 中位數：奇數個取中間，偶數個取左中位數
    if n % 2 == 1:
        a = sorted_nums[n // 2]
    else:
        a = sorted_nums[n // 2 - 1]

    # 計算等於 A 的數字個數
    count_equal_a = sum(1 for x in sorted_nums if x == a)

    # 計算能達最小值的不同 A 個數
    if n % 2 == 1:
        # 奇數時只有中位數能達最小值
        count_min_a = 1
    else:
        # 偶數時，左中位數到右中位數之間所有整數都能達最小值
        left_median = sorted_nums[n // 2 - 1]
        right_median = sorted_nums[n // 2]
        count_min_a = right_median - left_median + 1

    return a, count_equal_a, count_min_a


def solve(data: str) -> str:
    """解析題目輸入並輸出每組答案。"""
    lines = data.strip().split("\n")
    idx = 0
    out: List[str] = []

    while idx < len(lines):
        n = int(lines[idx].strip())
        idx += 1

        if n == 0:
            break

        if n > 0:
            numbers = list(map(int, lines[idx].split()))
            idx += 1
        else:
            numbers = []

        a, cnt_eq, cnt_min = solve_case(numbers)
        out.append(f"{a} {cnt_eq} {cnt_min}")

    return "\n".join(out)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()))

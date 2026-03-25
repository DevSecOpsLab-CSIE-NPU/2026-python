from __future__ import annotations

import sys


def median_summary(numbers: list[int]) -> tuple[int, int, int]:
    # 先排序，這樣中位數的位置就會很清楚。
    numbers.sort()
    length = len(numbers)

    # 奇數個數字時，兩個中位位置會是同一個值。
    # 偶數個數字時，這兩個值之間的所有整數都能讓總距離最小。
    lower_median = numbers[(length - 1) // 2]
    upper_median = numbers[length // 2]

    # 題目要的第二個值不是「可能答案有幾個」，
    # 而是輸入資料中有幾個數字落在最佳答案區間內。
    match_count = 0
    for value in numbers:
        if lower_median <= value <= upper_median:
            match_count += 1

    # 若 lower_median == upper_median，代表只有一種最佳答案。
    # 否則是兩者之間所有整數都可以。
    possible_count = upper_median - lower_median + 1

    # UVA 的輸出要求第一個值使用較小的那個中位數。
    return lower_median, match_count, possible_count


def solve(data: str) -> str:
    parts = data.split()
    index = 0
    outputs: list[str] = []

    while index < len(parts):
        count = int(parts[index])
        index += 1

        numbers: list[int] = []
        for _ in range(count):
            numbers.append(int(parts[index]))
            index += 1

        median_value, match_count, possible_count = median_summary(numbers)
        outputs.append(f"{median_value} {match_count} {possible_count}")

    return "\n".join(outputs)


def main() -> None:
    raw_data = sys.stdin.read()
    sys.stdout.write(solve(raw_data))


if __name__ == "__main__":
    main()
from __future__ import annotations

import sys


def median_summary(numbers: list[int]) -> tuple[int, int, int]:
    # 將數字排序後，中間區段就是所有能讓總距離最小的答案範圍。
    sorted_numbers = sorted(numbers)
    lower_median = sorted_numbers[(len(sorted_numbers) - 1) // 2]
    upper_median = sorted_numbers[len(sorted_numbers) // 2]

    match_count = sum(lower_median <= value <= upper_median for value in sorted_numbers)
    possible_count = upper_median - lower_median + 1
    return lower_median, match_count, possible_count


def solve(data: str) -> str:
    tokens = data.split()
    index = 0
    answers: list[str] = []

    while index < len(tokens):
        number_count = int(tokens[index])
        index += 1
        numbers = [int(tokens[index + offset]) for offset in range(number_count)]
        index += number_count

        median_value, match_count, possible_count = median_summary(numbers)
        answers.append(f"{median_value} {match_count} {possible_count}")

    return "\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
from bisect import bisect_left, bisect_right
from sys import stdin


# 排序後找中位數範圍，統計可得到最小總距離的 A 與對應數量。
def analyze_numbers(numbers):
    numbers.sort()
    length = len(numbers)
    lower_median = numbers[(length - 1) // 2]
    upper_median = numbers[length // 2]

    count_in_best_range = bisect_right(numbers, upper_median) - bisect_left(numbers, lower_median)
    possible_values = upper_median - lower_median + 1

    return lower_median, count_in_best_range, possible_values


# 這題有多組資料直到 EOF，逐組輸出三個整數結果。
def solve(tokens):
    index = 0
    results = []

    while index < len(tokens):
        count = int(tokens[index])
        index += 1
        numbers = list(map(int, tokens[index:index + count]))
        index += count
        answer = analyze_numbers(numbers)
        results.append(f"{answer[0]} {answer[1]} {answer[2]}")

    return "\n".join(results)


def main():
    tokens = stdin.read().split()
    if not tokens:
        return
    print(solve(tokens))


if __name__ == "__main__":
    main()
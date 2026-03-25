import bisect
import sys


def solve_case(values):
    values.sort()
    n = len(values)

    if n % 2 == 1:
        # 奇數個元素時，唯一最佳解是中位數
        a = values[n // 2]
        count = bisect.bisect_right(values, a) - bisect.bisect_left(values, a)
        ways = 1
        return a, count, ways

    # 偶數個元素時，區間 [low, high] 內皆為最佳解
    low = values[n // 2 - 1]
    high = values[n // 2]
    left = bisect.bisect_left(values, low)
    right = bisect.bisect_right(values, high)
    count = right - left
    ways = high - low + 1
    return low, count, ways


def main():
    # UVA 10057 常見輸入格式：多組測資直到 EOF
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    idx = 0
    answers = []

    while idx < len(data):
        n = data[idx]
        idx += 1

        values = data[idx:idx + n]
        idx += n

        a, count, ways = solve_case(values)
        answers.append(f"{a} {count} {ways}")

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()

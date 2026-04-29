import sys

"""
優化說明：
- 將曼哈頓距離中位數解法封裝成單一測資函式。
- 分離測資求解與輸入解析，提升可測試性。
"""


def solve_case(points):
    xs = sorted(x for x, _ in points)
    ys = sorted(y for _, y in points)
    count = len(points)

    median_x = xs[(count - 1) // 2]
    median_y = ys[(count - 1) // 2]
    distance = sum(abs(value - median_x) for value in xs) + sum(abs(value - median_y) for value in ys)

    if count % 2 == 1:
        ways = 1
    else:
        ways = (xs[count // 2] - xs[count // 2 - 1] + 1) * (ys[count // 2] - ys[count // 2 - 1] + 1)

    return f"{distance} {ways}"


def solve(reader):
    test_count = int(reader.readline())
    answers = []

    for _ in range(test_count):
        point_count = int(reader.readline())
        points = [tuple(map(int, reader.readline().split())) for _ in range(point_count)]
        answers.append(solve_case(points))

    return "\n".join(answers)


def main():
    sys.stdout.write(solve(sys.stdin))


if __name__ == "__main__":
    main()
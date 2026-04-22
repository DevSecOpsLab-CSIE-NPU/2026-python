import sys


def solve_case(points):
    # 分別取出所有 x 與 y 座標
    xs = [x for x, _ in points]
    ys = [y for _, y in points]

    xs.sort()
    ys.sort()

    n = len(points)

    # 取一個合法中位數來計算最小距離和
    mx = xs[n // 2]
    my = ys[n // 2]

    min_sum = 0

    # 曼哈頓距離可拆成 x 與 y 分別加總
    for x in xs:
        min_sum += abs(x - mx)
    for y in ys:
        min_sum += abs(y - my)

    # 計算最佳解個數
    if n % 2 == 1:
        count_x = 1
        count_y = 1
    else:
        count_x = xs[n // 2] - xs[n // 2 - 1] + 1
        count_y = ys[n // 2] - ys[n // 2 - 1] + 1

    ways = count_x * count_y

    return min_sum, ways


def main():
    input = sys.stdin.readline

    t = int(input().strip())
    outputs = []

    for _ in range(t):
        n = int(input().strip())
        points = []

        for _ in range(n):
            x, y = map(int, input().split())
            points.append((x, y))

        ans_sum, ans_count = solve_case(points)
        outputs.append(f"{ans_sum} {ans_count}")

    print("\n".join(outputs))


if __name__ == "__main__":
    main()
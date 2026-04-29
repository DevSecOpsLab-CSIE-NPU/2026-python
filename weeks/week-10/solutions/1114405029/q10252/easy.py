import sys


def solve_case(points):
    """
    給定一堆點，找一個點 (mx, my)，
    使得所有點到它的曼哈頓距離總和最小，
    並計算有幾個這樣的最佳點。
    """

    n = len(points)

    # 拆成 x 與 y 兩個陣列
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    xs.sort()
    ys.sort()

    # 取中位數
    mid = n // 2
    mx = xs[mid]
    my = ys[mid]

    # 計算最小距離
    # 曼哈頓距離可以拆開算
    min_sum = 0

    for x in xs:
        min_sum += abs(x - mx)

    for y in ys:
        min_sum += abs(y - my)

    # 計算最佳解數量
    if n % 2 == 1:
        # 奇數 → 中位數唯一
        count_x = 1
        count_y = 1
    else:
        # 偶數 → 中位數區間
        count_x = xs[mid] - xs[mid - 1] + 1
        count_y = ys[mid] - ys[mid - 1] + 1

    ways = count_x * count_y

    return min_sum, ways


def main():
    input = sys.stdin.readline

    t = int(input().strip())
    outputs = []

    for _ in range(t):
        n = int(input().strip())

        # 直接用 list comprehension 讀入，速度更快
        points = [tuple(map(int, input().split())) for _ in range(n)]

        ans_sum, ans_count = solve_case(points)

        outputs.append(f"{ans_sum} {ans_count}")

    # 使用 sys.stdout.write 比 print 更精準
    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()
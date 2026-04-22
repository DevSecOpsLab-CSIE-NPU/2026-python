import sys


def solve_case(points):
    # 把所有點的 x 座標和 y 座標分開存
    xs = [x for x, _ in points]
    ys = [y for _, y in points]

    # 先排序，因為中位數要從排序後的位置取得
    xs.sort()
    ys.sort()

    n = len(points)

    # 對於絕對值和最小化問題
    # 最佳解會出現在中位數
    # 這裡直接取排序後中間位置的值來計算最小距離和
    mx = xs[n // 2]
    my = ys[n // 2]

    min_sum = 0

    # 曼哈頓距離可以拆成 x 和 y 各自計算
    for x in xs:
        min_sum += abs(x - mx)

    for y in ys:
        min_sum += abs(y - my)

    # 接著算有幾個整數點可以達到相同最小值
    # 若 n 是奇數，中位數唯一，所以 x 與 y 都各只有 1 種
    if n % 2 == 1:
        count_x = 1
        count_y = 1
    else:
        # 若 n 是偶數，排序後中間兩個值之間的所有整數都可以
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
import sys


def main():
    input = sys.stdin.buffer.readline
    t = int(input())
    ans = []

    for _ in range(t):
        n = int(input())
        xs = []
        ys = []

        for _ in range(n):
            x, y = map(int, input().split())
            xs.append(x)
            ys.append(y)

        # 曼哈頓距離可以拆成 x 軸和 y 軸各自處理。
        xs.sort()
        ys.sort()

        # 奇數個點時，中位數只有一個。
        # 偶數個點時，夾在中間兩個值之間的整數都可以。
        mx = xs[(n - 1) // 2]
        my = ys[(n - 1) // 2]

        total = 0
        for x in xs:
            total += abs(x - mx)
        for y in ys:
            total += abs(y - my)

        if n % 2 == 1:
            ways = 1
        else:
            ways = (xs[n // 2] - xs[n // 2 - 1] + 1) * (ys[n // 2] - ys[n // 2 - 1] + 1)

        ans.append(f"{total} {ways}")

    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    main()
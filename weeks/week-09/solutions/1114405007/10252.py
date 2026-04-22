import sys

input = sys.stdin.buffer.readline
t = int(input())
out = []

for _ in range(t):
    n = int(input())
    xs = []
    ys = []

    for _ in range(n):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)

    # 曼哈頓距離分成 x 與 y 各自獨立處理。
    xs.sort()
    ys.sort()

    # 任取中位數都能讓距離和最小。
    x = xs[(n - 1) // 2]
    y = ys[(n - 1) // 2]
    dist = 0

    for v in xs:
        dist += abs(v - x)
    for v in ys:
        dist += abs(v - y)

    if n % 2 == 1:
        cnt = 1
    else:
        # 偶數時，中間區間內的整數點都能達到相同最小值。
        cnt = (xs[n // 2] - xs[n // 2 - 1] + 1) * (ys[n // 2] - ys[n // 2 - 1] + 1)

    out.append(f"{dist} {cnt}")

sys.stdout.write("\n".join(out))
import sys


# 一維最小化 sum(|x-ai|)：
# 最小值在中位數；偶數個時是中間區間所有整數
def one_dim_min_and_count(arr):
    arr.sort()
    n = len(arr)

    if n % 2 == 1:
        med = arr[n // 2]
        min_sum = sum(abs(v - med) for v in arr)
        cnt = 1
    else:
        l = arr[n // 2 - 1]
        r = arr[n // 2]
        med = l
        min_sum = sum(abs(v - med) for v in arr)
        cnt = r - l + 1

    return min_sum, cnt


def solve():
    input = sys.stdin.readline
    t = int(input().strip())
    out = []

    for _ in range(t):
        n = int(input().strip())
        xs = []
        ys = []
        for _ in range(n):
            x, y = map(int, input().split())
            xs.append(x)
            ys.append(y)

        sx, cx = one_dim_min_and_count(xs)
        sy, cy = one_dim_min_and_count(ys)

        # 二維曼哈頓可拆成 x 與 y 獨立最小化
        # 最小總和 = sx + sy
        # 解的數量 = cx * cy
        out.append(f"{sx + sy} {cx * cy}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()

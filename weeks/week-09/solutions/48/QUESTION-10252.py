import sys


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
        out.append(f"{sx + sy} {cx * cy}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()

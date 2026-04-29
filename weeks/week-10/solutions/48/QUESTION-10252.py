import sys


def one_dim_min_and_count(arr):
    # 優化點：二維問題拆成 x / y 兩個一維問題，時間與實作都更簡潔。
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
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        xs = []
        ys = []
        for _ in range(n):
            x = int(next(it)); y = int(next(it))
            xs.append(x); ys.append(y)
        sx, cx = one_dim_min_and_count(xs)
        sy, cy = one_dim_min_and_count(ys)
        out.append(f"{sx + sy} {cx * cy}")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()

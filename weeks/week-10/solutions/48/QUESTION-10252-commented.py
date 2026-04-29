"""
註解版本：曼哈頓中位數問題，將二維分解為 x 與 y 兩個一維。
一維最小化 sum(|x - ai|) 的解為中位數；若偶數個點，解的數量是區間寬度。
"""
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

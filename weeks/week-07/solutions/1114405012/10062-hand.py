"""10062 easy-hand：手打版（重點是好背、好寫）。"""

import sys


def solve(data):
    if not data:
        return []

    n = data[0]

    # a[pos]：第 pos 個位置前面有幾個較小編號。
    a = [0] * (n + 1)
    for pos in range(2, n + 1):
        a[pos] = data[pos - 1]

    # remaining 內維持目前還沒被拿走的編號（遞增）。
    remaining = list(range(1, n + 1))
    ans = [0] * (n + 1)

    # 從右往左放：拿第 a[pos]+1 小（0-based 就是 a[pos]）。
    for pos in range(n, 0, -1):
        ans[pos] = remaining.pop(a[pos])

    return ans[1:]


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    out = solve(data)
    if out:
        sys.stdout.write("\n".join(map(str, out)))


if __name__ == "__main__":
    main()

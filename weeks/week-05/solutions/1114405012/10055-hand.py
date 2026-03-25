import sys


def solve(data: str) -> str:
    nums = list(map(int, data.split()))
    if not nums:
        return ""

    n, q = nums[0], nums[1]
    idx = 2

    # 使用 Fenwick Tree 記錄每個位置翻轉次數的奇偶
    tree = [0] * (n + 1)

    def add(pos: int, value: int) -> None:
        while pos <= n:
            tree[pos] ^= value
            pos += pos & -pos

    def prefix_xor(pos: int) -> int:
        x = 0
        while pos > 0:
            x ^= tree[pos]
            pos -= pos & -pos
        return x

    def range_xor(left: int, right: int) -> int:
        return prefix_xor(right) ^ prefix_xor(left - 1)

    ans = []

    for _ in range(q):
        op = nums[idx]
        idx += 1

        if op == 1:
            i = nums[idx]
            idx += 1
            add(i, 1)
        else:
            l = nums[idx]
            r = nums[idx + 1]
            idx += 2
            ans.append(str(range_xor(l, r)))

    return "\n".join(ans)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))

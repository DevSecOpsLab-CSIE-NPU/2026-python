import sys


class FenwickXor:
    def __init__(self, n: int) -> None:
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, v: int) -> None:
        while i <= self.n:
            self.bit[i] ^= v
            i += i & -i

    def prefix_xor(self, i: int) -> int:
        res = 0
        while i > 0:
            res ^= self.bit[i]
            i -= i & -i
        return res

    def range_xor(self, l: int, r: int) -> int:
        return self.prefix_xor(r) ^ self.prefix_xor(l - 1)


def solve(data: bytes) -> str:
    nums = list(map(int, data.split()))
    if not nums:
        return ""

    n, q = nums[0], nums[1]
    idx = 2
    fw = FenwickXor(n)
    out = []

    for _ in range(q):
        v = nums[idx]
        idx += 1
        if v == 1:
            pos = nums[idx]
            idx += 1
            fw.add(pos, 1)
        else:
            l = nums[idx]
            r = nums[idx + 1]
            idx += 2
            out.append(str(fw.range_xor(l, r)))

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.buffer.read()))

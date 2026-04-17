import sys


class FenwickXor:
    def __init__(self, n: int) -> None:
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.bit[i] ^= delta
            i += i & -i

    def query(self, i: int) -> int:
        s = 0
        while i > 0:
            s ^= self.bit[i]
            i -= i & -i
        return s

    def range_xor(self, l: int, r: int) -> int:
        return self.query(r) ^ self.query(l - 1)


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, q = data[0], data[1]
    idx = 2

    bit = FenwickXor(n)
    state = [0] * (n + 1)
    out = []

    for _ in range(q):
        v = data[idx]
        idx += 1

        if v == 1:
            i = data[idx]
            idx += 1
            state[i] ^= 1
            bit.update(i, 1)
        else:
            l = data[idx]
            r = data[idx + 1]
            idx += 2
            out.append(str(bit.range_xor(l, r)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()

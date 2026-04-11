import sys


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


def solve():
    # 用 BIT 記錄「目前有幾個函數是遞減」。
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, q = data[0], data[1]
    idx = 2

    state = [0] * (n + 1)
    bit = FenwickTree(n)
    out = []

    for _ in range(q):
        typ = data[idx]
        idx += 1

        if typ == 1:
            pos = data[idx]
            idx += 1

            if state[pos] == 0:
                state[pos] = 1
                bit.add(pos, 1)
            else:
                state[pos] = 0
                bit.add(pos, -1)
        else:
            l = data[idx]
            r = data[idx + 1]
            idx += 2

            cnt = bit.sum(r) - bit.sum(l - 1)
            out.append(str(cnt % 2))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
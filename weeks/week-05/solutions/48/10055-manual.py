import sys


class FenwickTree:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def prefix_sum(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, left: int, right: int) -> int:
        return self.prefix_sum(right) - self.prefix_sum(left - 1)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    idx = 0
    n = data[idx]
    idx += 1
    q = data[idx]
    idx += 1

    state = [0] * (n + 1)
    ft = FenwickTree(n)
    out = []

    for _ in range(q):
        v = data[idx]
        idx += 1

        if v == 1:
            i = data[idx]
            idx += 1
            if state[i] == 0:
                state[i] = 1
                ft.add(i, 1)
            else:
                state[i] = 0
                ft.add(i, -1)
        else:
            left = data[idx]
            idx += 1
            right = data[idx]
            idx += 1
            cnt_dec = ft.range_sum(left, right)
            out.append("1" if cnt_dec % 2 == 1 else "0")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

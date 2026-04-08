import sys


class BIT:
    def __init__(self, n: int) -> None:
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx: int, delta: int) -> None:
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def kth(self, k: int) -> int:
        idx = 0
        step = 1 << (self.n.bit_length())
        while step:
            nxt = idx + step
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                idx = nxt
            step >>= 1
        return idx + 1


def solve(data: str) -> str:
    tokens = data.split()
    if not tokens:
        return ""

    n = int(tokens[0])
    smaller_before = [0] * (n + 1)
    for pos in range(2, n + 1):
        smaller_before[pos] = int(tokens[pos - 1])

    bit = BIT(n)
    for i in range(1, n + 1):
        bit.add(i, 1)

    ans = [0] * (n + 1)
    for pos in range(n, 0, -1):
        k = smaller_before[pos] + 1
        value = bit.kth(k)
        ans[pos] = value
        bit.add(value, -1)

    return "\n".join(str(ans[i]) for i in range(1, n + 1))


def main() -> None:
    text = sys.stdin.read()
    out = solve(text)
    if out:
        print(out)


if __name__ == "__main__":
    main()

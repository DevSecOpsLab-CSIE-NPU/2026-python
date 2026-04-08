import sys


class FenwickTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, index: int, value: int) -> None:
        while index <= self.n:
            self.tree[index] += value
            index += index & -index

    def find_kth(self, k: int) -> int:
        index = 0
        bit_mask = 1 << (self.n.bit_length() - 1)
        while bit_mask:
            next_index = index + bit_mask
            if next_index <= self.n and self.tree[next_index] < k:
                k -= self.tree[next_index]
                index = next_index
            bit_mask >>= 1
        return index + 1


def reconstruct_lineup(smaller_counts: list[int]) -> list[int]:
    n = len(smaller_counts) + 1
    counts = [0] * (n + 1)
    for i in range(2, n + 1):
        counts[i] = smaller_counts[i - 2]

    bit = FenwickTree(n)
    for i in range(1, n + 1):
        bit.add(i, 1)

    answer = [0] * (n + 1)
    for i in range(n, 0, -1):
        rank = counts[i] + 1
        answer[i] = bit.find_kth(rank)
        bit.add(answer[i], -1)

    return answer[1:]


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    smaller_counts = [int(data[i]) for i in range(1, n)]
    lineup = reconstruct_lineup(smaller_counts)
    print("\n".join(str(x) for x in lineup))


if __name__ == "__main__":
    main()

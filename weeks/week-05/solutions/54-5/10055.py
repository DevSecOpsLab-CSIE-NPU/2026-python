import sys
from typing import List


class FenwickTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.data = [0] * (n + 1)

    def add(self, i: int, value: int) -> None:
        while i <= self.n:
            self.data[i] += value
            i += i & -i

    def sum(self, i: int) -> int:
        result = 0
        while i > 0:
            result += self.data[i]
            i -= i & -i
        return result


def process_queries(n: int, queries: List[List[int]]) -> List[int]:
    tree = FenwickTree(n)
    flipped = [0] * (n + 1)
    results: List[int] = []

    for query in queries:
        if query[0] == 1:
            idx = query[1]
            flipped[idx] ^= 1
            tree.add(idx, 1 if flipped[idx] == 1 else -1)
        else:
            l, r = query[1], query[2]
            count = tree.sum(r) - tree.sum(l - 1)
            results.append(1 if count % 2 == 1 else 0)

    return results


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    q = int(next(it))
    queries = []
    for _ in range(q):
        v = int(next(it))
        if v == 1:
            queries.append([v, int(next(it))])
        else:
            queries.append([v, int(next(it)), int(next(it))])

    results = process_queries(n, queries)
    sys.stdout.write("\n".join(str(x) for x in results))


if __name__ == "__main__":
    main()

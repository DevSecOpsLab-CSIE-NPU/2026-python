import sys
from typing import List


def process_queries(n: int, queries: List[List[int]]) -> List[int]:
    flipped = [0] * (n + 1)
    results: List[int] = []

    for query in queries:
        if query[0] == 1:
            idx = query[1]
            flipped[idx] ^= 1
        else:
            l, r = query[1], query[2]
            count = sum(flipped[l : r + 1])
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

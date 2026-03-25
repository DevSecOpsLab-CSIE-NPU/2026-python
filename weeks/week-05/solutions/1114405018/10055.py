from typing import Iterable, List, Tuple


class Fenwick:
    def __init__(self, n: int) -> None:
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx: int, delta: int) -> None:
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def sum_prefix(self, idx: int) -> int:
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s

    def range_sum(self, left: int, right: int) -> int:
        return self.sum_prefix(right) - self.sum_prefix(left - 1)


def process_queries(n: int, operations: Iterable[Tuple[int, ...]]) -> List[int]:
    # state[i] = 0 表示增函數，1 表示減函數
    state = [0] * (n + 1)
    fw = Fenwick(n)
    out: List[int] = []

    for op in operations:
        if op[0] == 1:
            i = op[1]
            if state[i] == 0:
                state[i] = 1
                fw.add(i, 1)
            else:
                state[i] = 0
                fw.add(i, -1)
        else:
            l, r = op[1], op[2]
            # 區間內減函數個數奇數 => 複合後為減函數(1)
            out.append(fw.range_sum(l, r) % 2)

    return out


def solve(data: str) -> str:
    tokens = list(map(int, data.split()))
    if not tokens:
        return ""

    n = tokens[0]
    q = tokens[1]
    i = 2
    operations: List[Tuple[int, ...]] = []

    for _ in range(q):
        v = tokens[i]
        i += 1
        if v == 1:
            idx = tokens[i]
            i += 1
            operations.append((1, idx))
        else:
            l = tokens[i]
            r = tokens[i + 1]
            i += 2
            operations.append((2, l, r))

    result = process_queries(n, operations)
    return "\n".join(map(str, result))


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()))

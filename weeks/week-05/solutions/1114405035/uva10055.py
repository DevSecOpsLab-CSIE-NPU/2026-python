def process_input(input_text: str) -> str:
    tokens = input_text.strip().split()
    if not tokens:
        return ''

    n = int(tokens[0])
    q = int(tokens[1])
    idx = 2
    values = [0] * (n + 1)
    results = []

    for _ in range(q):
        op = int(tokens[idx])
        idx += 1
        if op == 1:
            i = int(tokens[idx])
            idx += 1
            values[i] ^= 1
        else:
            l = int(tokens[idx])
            r = int(tokens[idx + 1])
            idx += 2
            parity = sum(values[l:r + 1]) % 2
            results.append('1' if parity else '0')

    return '\n'.join(results)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
from typing import List


class FenwickTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int) -> None:
        while index <= self.size:
            self.tree[index] ^= 1
            index += index & -index

    def query(self, index: int) -> int:
        result = 0
        while index > 0:
            result ^= self.tree[index]
            index -= index & -index
        return result


def process_input(input_text: str) -> str:
    tokens = input_text.strip().split()
    if not tokens:
        return ''

    n = int(tokens[0])
    q = int(tokens[1])
    operations = [int(x) for x in tokens[2:]]

    fenwick = FenwickTree(n)
    state = [0] * (n + 1)
    idx = 0
    results: List[str] = []

    for _ in range(q):
        op_type = operations[idx]
        idx += 1
        if op_type == 1:
            i = operations[idx]
            idx += 1
            state[i] ^= 1
            fenwick.update(i)
        else:
            l = operations[idx]
            r = operations[idx + 1]
            idx += 2
            parity = fenwick.query(r) ^ fenwick.query(l - 1)
            results.append('1' if parity else '0')

    return '\n'.join(results)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')

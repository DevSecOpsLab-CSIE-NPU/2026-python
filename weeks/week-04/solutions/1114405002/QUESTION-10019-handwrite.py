"""UVA 10019 手打版。"""

import sys


def solve():
    result = []
    data = sys.stdin.buffer.read().splitlines()

    for line in data:
        if not line.strip():
            continue
        first, second = map(int, line.split())
        if first > second:
            result.append(str(first - second))
        else:
            result.append(str(second - first))

    sys.stdout.write("\n".join(result))


if __name__ == "__main__":
    solve()

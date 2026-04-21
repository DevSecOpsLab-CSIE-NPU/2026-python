"""UVA 10019 Hashmat the Brave Warrior 標準版。"""

import sys


def solve():
    out = []
    for line in sys.stdin.buffer.read().splitlines():
        if not line.strip():
            continue
        a, b = map(int, line.split())
        out.append(str(abs(a - b)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
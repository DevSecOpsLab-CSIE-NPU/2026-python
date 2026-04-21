"""UVA 10019 Hashmat - easy 版。

題目重點只有一個：每組輸入都輸出兩數差的絕對值。
"""

import sys


def solve():
    ans = []
    for line in sys.stdin.buffer.read().splitlines():
        if line.strip() == b"":
            continue
        x, y = map(int, line.split())
        ans.append(str(x - y if x >= y else y - x))
    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    solve()
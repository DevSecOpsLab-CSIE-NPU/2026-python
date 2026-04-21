"""UVA 10008 手打版。

這份版本保留很明確的流程：
先累計每個英文字母的次數，再排序後輸出。
"""

import sys


def solve():
    lines = sys.stdin.buffer.read().splitlines()
    if not lines:
        return

    n = int(lines[0].decode())
    count = {}

    for i in range(1, 1 + n):
        text = lines[i].decode(errors="ignore")
        for ch in text:
            if "a" <= ch <= "z":
                ch = ch.upper()
            if "A" <= ch <= "Z":
                if ch not in count:
                    count[ch] = 0
                count[ch] += 1

    arr = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    out = []
    for ch, num in arr:
        out.append(f"{ch} {num}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()

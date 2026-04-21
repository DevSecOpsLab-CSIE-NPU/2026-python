"""UVA 10008 Cryptanalysis 標準版。

做法：
1. 讀入全部文字。
2. 只統計英文字母，並統一轉成大寫。
3. 依照「次數由大到小、字母由小到大」排序輸出。
"""

import sys
from collections import Counter


def solve():
    lines = sys.stdin.buffer.read().splitlines()
    if not lines:
        return

    n = int(lines[0].decode())
    counter = Counter()

    for line in lines[1 : 1 + n]:
        for ch in line.decode(errors="ignore"):
            if "a" <= ch <= "z":
                counter[ch.upper()] += 1
            elif "A" <= ch <= "Z":
                counter[ch] += 1

    items = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    out = [f"{ch} {count}" for ch, count in items]
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
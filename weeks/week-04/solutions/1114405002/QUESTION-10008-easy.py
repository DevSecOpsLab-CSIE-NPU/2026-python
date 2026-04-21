"""UVA 10008 Cryptanalysis - easy 版。

這版把核心概念縮成三步：
1. 數字母。
2. 排序。
3. 印出來。

因為題目只看英文字母，所以其他符號全部忽略。
"""

import sys


def solve():
    data = sys.stdin.buffer.read().splitlines()
    if not data:
        return

    n = int(data[0].decode())
    cnt = {}

    for line in data[1 : 1 + n]:
        for ch in line.decode(errors="ignore"):
            if "A" <= ch <= "Z":
                key = ch
            elif "a" <= ch <= "z":
                key = ch.upper()
            else:
                continue
            cnt[key] = cnt.get(key, 0) + 1

    result = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
    ans = []
    for ch, num in result:
        ans.append(f"{ch} {num}")

    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    solve()
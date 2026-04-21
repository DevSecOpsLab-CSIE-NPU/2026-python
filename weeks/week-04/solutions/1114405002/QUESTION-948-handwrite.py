"""UVA 948 手打版。

這份版本刻意維持非常直線的流程：
先讀資料，再一顆一顆試硬幣，最後直接輸出答案。
"""

import sys


def solve():
    data = sys.stdin.buffer.read().splitlines()

    i = 0
    while i < len(data) and not data[i].strip():
        i += 1

    if i >= len(data):
        return

    m = int(data[i].decode())
    i += 1
    ans = []

    for _ in range(m):
        while i < len(data) and not data[i].strip():
            i += 1

        n, k = map(int, data[i].split())
        i += 1

        wa = []
        for _ in range(k):
            line = list(map(int, data[i].split()))
            i += 1
            p = line[0]
            left = set(line[1 : 1 + p])
            right = set(line[1 + p : 1 + 2 * p])
            result = data[i].decode().strip()
            i += 1
            wa.append((left, right, result))

        found = 0
        count = 0

        for coin in range(1, n + 1):
            good = True

            # 先假設偏重
            for left, right, result in wa:
                if coin in left:
                    expect = ">"
                elif coin in right:
                    expect = "<"
                else:
                    expect = "="
                if expect != result:
                    good = False
                    break

            if good:
                found = coin
                count += 1
                continue

            # 再假設偏輕
            good = True
            for left, right, result in wa:
                if coin in left:
                    expect = "<"
                elif coin in right:
                    expect = ">"
                else:
                    expect = "="
                if expect != result:
                    good = False
                    break

            if good:
                found = coin
                count += 1

        ans.append(str(found if count == 1 else 0))

    sys.stdout.write("\n\n".join(ans))


if __name__ == "__main__":
    solve()

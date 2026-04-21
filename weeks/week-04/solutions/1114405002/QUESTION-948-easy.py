"""UVA 948 金條銀行假幣判定 - easy 版。

這一版刻意寫得更直覺：
1. 逐一嘗試每一顆硬幣。
2. 分別假設它是偏重或偏輕。
3. 只要所有秤重都符合，就保留這顆硬幣。

這種寫法好記、好改，也方便手寫。
"""

import sys


def read_nonempty(lines, idx):
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    return idx


def ok(coin, heavy, weighings):
    """假設某顆硬幣是假的，檢查是否和所有秤重結果一致。"""
    for left, right, result in weighings:
        if coin in left:
            expect = ">" if heavy else "<"
        elif coin in right:
            expect = "<" if heavy else ">"
        else:
            expect = "="

        if expect != result:
            return False
    return True


def solve():
    lines = sys.stdin.buffer.read().splitlines()
    idx = 0
    idx = read_nonempty(lines, idx)
    if idx >= len(lines):
        return

    t = int(lines[idx].decode())
    idx += 1
    out = []

    for _ in range(t):
        idx = read_nonempty(lines, idx)
        n, k = map(int, lines[idx].split())
        idx += 1

        weighings = []
        for _ in range(k):
            data = list(map(int, lines[idx].split()))
            idx += 1
            p = data[0]
            left = set(data[1 : 1 + p])
            right = set(data[1 + p : 1 + 2 * p])
            result = lines[idx].decode().strip()
            idx += 1
            weighings.append((left, right, result))

        answer = 0
        candidates = 0
        for coin in range(1, n + 1):
            if ok(coin, True, weighings) or ok(coin, False, weighings):
                answer = coin
                candidates += 1

        out.append(str(answer if candidates == 1 else 0))

    sys.stdout.write("\n\n".join(out))


if __name__ == "__main__":
    solve()
"""UVA 11321 - Sort! Sort!! and Sort!!! (easy version with detailed comments)."""

from __future__ import annotations

import sys


def make_key(x: int, m: int) -> tuple[int, int, int]:
    # 第一順位：餘數小的排前面。
    r = x % m

    # 第二順位：奇數排在偶數前面。
    # 第三順位：奇數由大到小；偶數由小到大。
    if x % 2 != 0:
        return (r, 0, -x)
    return (r, 1, x)


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    pos = 0
    output: list[str] = []

    # 直到讀到 0 0 為止。
    while pos + 1 < len(data):
        n = data[pos]
        m = data[pos + 1]
        pos += 2

        if n == 0 and m == 0:
            break

        arr = data[pos:pos + n]
        pos += n

        arr.sort(key=lambda x: make_key(x, m))

        # 經典輸出格式：先印 n m，再印排序好的陣列。
        output.append(f"{n} {m}")
        output.append(" ".join(map(str, arr)))

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()
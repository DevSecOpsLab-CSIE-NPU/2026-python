"""Task 1: Sequence Clean

讀入一串整數，輸出：
1) 去重（保留第一次出現）
2) 升冪排序
3) 降冪排序
4) 偶數子序列（保留原順序）
"""

from __future__ import annotations

import sys


def main() -> None:
    numbers = [int(x) for x in sys.stdin.read().split()]

    seen = set()
    dedupe = []
    for value in numbers:
        if value not in seen:
            seen.add(value)
            dedupe.append(value)

    asc = sorted(numbers)
    desc = sorted(numbers, reverse=True)
    evens = [x for x in numbers if x % 2 == 0]

    print(f"dedupe: {' '.join(map(str, dedupe))}")
    print(f"asc: {' '.join(map(str, asc))}")
    print(f"desc: {' '.join(map(str, desc))}")
    print(f"evens: {' '.join(map(str, evens))}")


if __name__ == "__main__":
    main()

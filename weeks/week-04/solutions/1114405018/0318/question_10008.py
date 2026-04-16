"""UVA 10008 - What's Cryptanalysis?

統計所有輸入行中的英文字母（大小寫視為相同），
並依照「次數由大到小、字母由小到大」輸出。
"""

from __future__ import annotations

import sys
from collections import Counter


def solve(data: str) -> str:
    lines = data.splitlines()
    if not lines:
        return ""

    n = int(lines[0].strip())
    text_lines = lines[1 : 1 + n]

    counts: Counter[str] = Counter()
    for line in text_lines:
        for ch in line:
            if ch.isalpha():
                c = ch.upper()
                if "A" <= c <= "Z":
                    counts[c] += 1

    items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return "\n".join(f"{ch} {cnt}" for ch, cnt in items)


def main() -> None:
    result = solve(sys.stdin.read())
    if result:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()

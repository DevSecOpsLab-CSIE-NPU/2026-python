"""QUESTION-10008 正式版解答。"""

from __future__ import annotations

from collections import Counter
import sys


def solve(text: str) -> str:
    lines = text.splitlines()
    if not lines:
        return ""

    line_count = int(lines[0].strip())
    counts = Counter()

    for line in lines[1 : 1 + line_count]:
        # 題目要求忽略大小寫，所以統一轉成大寫後再計數。
        for char in line:
            if char.isalpha():
                counts[char.upper()] += 1

    # 先比出現次數，再比字母本身，剛好對應題目排序規則。
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return "\n".join(f"{letter} {count}" for letter, count in ordered)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

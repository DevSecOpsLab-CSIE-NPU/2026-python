"""QUESTION-10008 easy 版。

這題的核心只有兩件事：
1. 把英文字母全部轉成大寫後計數。
2. 依照「次數由大到小、字母由小到大」排序。

這份 easy 版故意不用太多技巧，讓流程保持直線化，
之後手打時比較不容易忘記。
"""

from __future__ import annotations

import sys


def solve(text: str) -> str:
    lines = text.splitlines()
    if not lines:
        return ""

    n = int(lines[0].strip())
    counter: dict[str, int] = {}

    for line in lines[1 : 1 + n]:
        for char in line:
            if char.isalpha():
                upper_char = char.upper()
                counter[upper_char] = counter.get(upper_char, 0) + 1

    items = list(counter.items())
    items.sort(key=lambda item: (-item[1], item[0]))

    answer_lines = []
    for letter, count in items:
        answer_lines.append(f"{letter} {count}")

    return "\n".join(answer_lines)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

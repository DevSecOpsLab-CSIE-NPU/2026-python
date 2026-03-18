"""
UVA 10008 - What's Cryptanalysis?
"""

from __future__ import annotations

from collections import Counter


def count_letters(lines: list[str]) -> list[tuple[str, int]]:
    """統計 A-Z 字母頻率，忽略大小寫與非字母字元。"""
    counter: Counter[str] = Counter()
    for line in lines:
        for char in line.upper():
            if "A" <= char <= "Z":
                counter[char] += 1
    return sorted(counter.items(), key=lambda item: (-item[1], item[0]))


def solve(text: str) -> str:
    """輸出依頻率遞減、字母遞增排序的統計結果。"""
    raw_lines = text.splitlines()
    if not raw_lines:
        return ""

    line_count = int(raw_lines[0].strip() or "0")
    lines = raw_lines[1 : 1 + line_count]
    return "\n".join(f"{letter} {count}" for letter, count in count_letters(lines))


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

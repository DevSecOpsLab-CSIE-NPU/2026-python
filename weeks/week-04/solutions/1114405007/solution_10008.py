from __future__ import annotations

from collections import Counter


def solve(data: str) -> str:
    lines = data.splitlines()
    if not lines:
        return ""

    line_count = int(lines[0].strip())
    counter: Counter[str] = Counter()

    # 只統計英文字母，並先統一轉成大寫處理大小寫合併。
    for line in lines[1 : 1 + line_count]:
        for char in line.upper():
            if "A" <= char <= "Z":
                counter[char] += 1

    # 依照次數由大到小排序；若次數相同則依字母順序排序。
    ordered = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    return "\n".join(f"{letter} {count}" for letter, count in ordered)


def main() -> None:
    import sys

    # 讀入全部文字，統計英文字母出現次數後輸出。
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
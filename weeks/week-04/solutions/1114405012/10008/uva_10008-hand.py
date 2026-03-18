from __future__ import annotations

import sys


def solve(data: str) -> str:
    """
    UVA 10008 手打版

    重點：
    - 大小寫視為同一字母，先轉大寫
    - 只統計 A~Z
    - 依次數降冪、字母升冪輸出
    """
    lines = data.splitlines()
    if not lines:
        return ""

    try:
        n = int(lines[0].strip())
    except ValueError:
        return ""

    counts = [0] * 26

    for line in lines[1 : 1 + n]:
        for ch in line:
            if ch.isalpha():
                pos = ord(ch.upper()) - ord("A")
                if 0 <= pos < 26:
                    counts[pos] += 1

    items = [(chr(i + ord("A")), counts[i]) for i in range(26) if counts[i] > 0]
    items.sort(key=lambda pair: (-pair[1], pair[0]))

    return "\n".join(f"{ch} {count}" for ch, count in items)


def main() -> None:
    text = sys.stdin.read()
    sys.stdout.write(solve(text))


if __name__ == "__main__":
    main()

from __future__ import annotations

import sys


def solve(data: str) -> str:
    """
    UVA 10008 - Cryptanalysis
    統計所有英文字母（不分大小寫）的出現次數，並依題目規則排序輸出。
    """
    lines = data.splitlines()
    if not lines:
        return ""

    try:
        n = int(lines[0].strip())
    except ValueError:
        return ""

    # 以長度 26 的陣列分別記錄 A~Z 次數
    counts = [0] * 26

    for line in lines[1 : 1 + n]:
        for ch in line:
            if ch.isalpha():
                index = ord(ch.upper()) - ord("A")
                if 0 <= index < 26:
                    counts[index] += 1

    pairs = [(chr(i + ord("A")), counts[i]) for i in range(26) if counts[i] > 0]

    # 先按次數由大到小，再按字母由小到大
    pairs.sort(key=lambda item: (-item[1], item[0]))

    return "\n".join(f"{letter} {count}" for letter, count in pairs)


def main() -> None:
    raw_input = sys.stdin.read()
    sys.stdout.write(solve(raw_input))


if __name__ == "__main__":
    main()

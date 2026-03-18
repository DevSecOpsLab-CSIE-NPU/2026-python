"""UVA 10008: 容易記憶版本。

這一版盡量維持直線流程：讀入、累加、排序、輸出。
"""

import sys


def solve(text: str) -> str:
    lines = text.splitlines()
    if not lines:
        return ""

    n = int(lines[0].strip())
    counts: dict[str, int] = {}

    # 逐行處理密文，每看到一個英文字母就累加一次。
    for line in lines[1 : 1 + n]:
        for char in line.upper():
            if "A" <= char <= "Z":
                counts[char] = counts.get(char, 0) + 1

    # easy 版保留最直接的排序規則寫法，方便背誦。
    order = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    answer_lines = []
    for letter, count in order:
        answer_lines.append(f"{letter} {count}")
    return "\n".join(answer_lines)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
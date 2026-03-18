"""UVA 10008: 字母統計。

這一版把輸入解析、統計與輸出格式化拆成函式，
方便單元測試，也比較接近正式提交時可重用的寫法。
"""

from collections import Counter
import sys


def count_letters(lines: list[str]) -> list[tuple[str, int]]:
    """統計所有英文字母出現次數，忽略大小寫與非字母字元。"""
    counter: Counter[str] = Counter()

    for line in lines:
        # 題目要求大小寫視為相同，因此先轉成大寫再統計。
        for char in line.upper():
            if "A" <= char <= "Z":
                counter[char] += 1

    # 先依照次數遞減排序，再依字母遞增排序。
    return sorted(counter.items(), key=lambda item: (-item[1], item[0]))


def solve(text: str) -> str:
    """依照題目輸入格式回傳結果字串。"""
    rows = text.splitlines()
    if not rows:
        return ""

    total = int(rows[0].strip())
    # 只取題目指定的 n 行資料，避免多餘輸入干擾結果。
    lines = rows[1 : 1 + total]
    result = count_letters(lines)
    return "\n".join(f"{letter} {count}" for letter, count in result)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
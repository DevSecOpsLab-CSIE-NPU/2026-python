"""UVA 10008 Cryptanalysis 解答。

題目要做的事很單純：
1. 讀入 n 行文字。
2. 只統計英文字母（A~Z），且大小寫視為相同。
3. 依規則排序後輸出：先比次數（大到小），再比字母（小到大）。
"""

from __future__ import annotations

import sys
from collections import Counter


def solve(data: str) -> str:
    """
    依題目規則統計字母頻率並輸出排序結果。

    規則：
    1. 只統計英文字母 A~Z。
    2. 大小寫視為相同（先轉成大寫）。
    3. 依「次數由大到小」排序；若同次數則依字母由小到大。
    """
    # splitlines() 會保留每一行資料，不受空白行格式影響。
    lines = data.splitlines()
    if not lines:
        return ""

    # 第一行是接下來要分析的文字行數。
    # 第一行是要分析的行數；若第一行是空字串，視為 0 行。
    n = int(lines[0].strip() or "0")

    # 使用 Counter 紀錄每個大寫字母的出現次數。
    counter: Counter[str] = Counter()

    # 累積統計前 n 行內容。
    # 只讀取接下來 n 行，避免多餘資料影響結果。
    for line in lines[1 : 1 + n]:
        for ch in line.upper():
            # 只統計英文字母，其餘字元（數字、符號、空白）全部忽略。
            if "A" <= ch <= "Z":
                counter[ch] += 1

    # 先按次數遞減，再按字母遞增。
    # 排序規則：
    # -item[1] 代表次數由大到小；item[0] 代表同次數時字母由小到大。
    ordered = sorted(counter.items(), key=lambda item: (-item[1], item[0]))

    if not ordered:
        return ""

    # 每行格式為「字母 次數」，最後補一個換行，符合 UVA 慣例。
    return "\n".join(f"{ch} {count}" for ch, count in ordered) + "\n"


def main() -> None:
    """標準輸入輸出入口：從 stdin 讀入，將答案輸出到 stdout。"""
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

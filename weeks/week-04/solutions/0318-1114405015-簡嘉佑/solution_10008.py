"""
UVA 10008 - 字母頻率統計（正式版）

題意摘要：
  讀取 N 列文字，統計每個英文字母（A~Z）出現的次數。
  - 大小寫視為相同（a 和 A 都算 A）。
  - 未出現的字母不輸出。
  - 輸出排序規則：
      1. 次數由大到小。
      2. 次數相同時，字母順序由小到大（A < B < ... < Z）。

解法：
  1. 建立 A~Z 計數字典，初始值皆為 0。
  2. 將每列轉為大寫後逐字元掃描，遇到字母就累加。
  3. 過濾次數為 0 的字母。
  4. 依（-次數, 字母）排序後輸出。

時間複雜度：O(N × L)，N = 列數，L = 每列字元數
空間複雜度：O(1)（字典固定 26 個 key）
"""

from __future__ import annotations

import sys


def count_letters(lines: list[str]) -> list[tuple[str, int]]:
    """
    統計多列文字中各英文字母的出現次數。

    :param lines: 輸入文字行的清單
    :return:      排序後的 [(大寫字母, 次數), ...] 清單
                  排序規則：次數由大到小；次數相同則字母由小到大
    """
    # 建立 A~Z 計數字典，初始全為 0
    counts: dict[str, int] = {chr(c): 0 for c in range(ord("A"), ord("Z") + 1)}

    for line in lines:
        for ch in line.upper():        # 統一轉大寫
            if "A" <= ch <= "Z":       # 只統計英文字母
                counts[ch] += 1

    # 過濾未出現的字母，並依（-次數, 字母）排序
    result = [(letter, cnt) for letter, cnt in counts.items() if cnt > 0]
    result.sort(key=lambda x: (-x[1], x[0]))
    return result


def main() -> None:
    """讀取標準輸入，輸出各字母的出現次數。"""
    data = sys.stdin.read().splitlines()
    # 第一列為行數 N
    n = int(data[0])
    lines = data[1: n + 1]

    for letter, cnt in count_letters(lines):
        print(f"{letter} {cnt}")


if __name__ == "__main__":
    main()

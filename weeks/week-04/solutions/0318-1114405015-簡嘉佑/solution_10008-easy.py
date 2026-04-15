"""
UVA 10008 - 字母頻率統計（easy 版）

簡單記法：
  用 Counter 一行統計所有字母，再排序輸出。

核心步驟：
  1. 把所有文字合併成一個大字串，轉大寫。
  2. 用 Counter 計算每個字元的出現次數。
  3. 只保留 A~Z 的計數，其餘忽略。
  4. 依（-次數, 字母）排序後輸出。

比較正式版：
  - 正式版：逐行掃描，手動維護字典。
  - easy 版：用 Counter + 條件過濾，程式碼更短易記。
"""

from __future__ import annotations

import sys
from collections import Counter


def count_letters(lines: list[str]) -> list[tuple[str, int]]:
    """
    統計多列文字中各英文字母（A~Z）的出現次數。

    :param lines: 輸入文字行的清單
    :return:      排序後的 [(大寫字母, 次數), ...] 清單
                  排序規則：次數由大到小；次數相同則字母由小到大

    簡單記法：
      - "".join(lines).upper()  → 把所有列合成一個大字串並轉大寫
      - Counter(...)            → 自動計算每個字元的出現次數
      - if "A" <= ch <= "Z"     → 只留字母
      - sort key=(-次數, 字母)  → 先多後少，同次數按字母序
    """
    # 步驟 1：把所有行合成一個大字串，統一轉大寫
    all_text = "".join(lines).upper()

    # 步驟 2：用 Counter 計算每個字元的次數
    counter = Counter(all_text)

    # 步驟 3：只保留 A~Z 的統計，過濾掉空白、數字、符號等
    letter_counts = [
        (ch, counter[ch])
        for ch in counter           # 遍歷所有出現過的字元
        if "A" <= ch <= "Z"         # 只取英文字母
    ]

    # 步驟 4：依（-次數, 字母）排序
    #   -次數 → 次數由大到小（負號讓大的數字排前面）
    #   字母  → 次數相同時字母由小到大（A < B < ... < Z）
    letter_counts.sort(key=lambda x: (-x[1], x[0]))

    return letter_counts


def main() -> None:
    """讀取標準輸入，輸出各字母的出現次數。"""
    data = sys.stdin.read().splitlines()
    n = int(data[0])              # 第一列為行數 N
    lines = data[1: n + 1]        # 取接下來的 N 列

    for letter, cnt in count_letters(lines):
        print(f"{letter} {cnt}")  # 輸出格式：大寫字母 + 空格 + 次數


if __name__ == "__main__":
    main()

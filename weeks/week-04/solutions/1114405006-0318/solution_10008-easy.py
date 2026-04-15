"""UVA 10008（簡單好記版）。

題目重點：
1. 第一行給你 n，代表接下來有 n 行文字要分析。
2. 只統計英文字母 A~Z，且大小寫視為相同字母。
3. 輸出時要先看出現次數（由大到小），
    若次數一樣，再看字母順序（由小到大）。
"""

from __future__ import annotations

import sys


# 好記口訣：
# 1) 讀 n 行
# 2) 全轉大寫
# 3) 只數 A~Z
# 4) 先照次數大到小，再照字母小到大


def solve(data: str) -> str:
    """
    將整份輸入文字轉成題目要求的輸出字串。

    參數：
    data: 完整輸入內容（通常來自 stdin）。

    回傳：
    排序後的統計結果字串；若沒有任何字母，回傳空字串。
    """
    # splitlines() 可以直接把輸入切成一行一行，方便處理。
    lines = data.splitlines()
    if not lines:
        return ""

    # 第一行是 n（接下來要分析幾行文字）。
    # 若第一行剛好空白，這裡保底當作 0。
    n = int(lines[0].strip() or "0")

    # 用長度 26 的陣列做計數：
    # freq[0] 對應 A，freq[25] 對應 Z。
    freq = [0] * 26

    # 只處理第 2 行到第 n+1 行，避免額外行數干擾。
    for line in lines[1 : 1 + n]:
        # 先轉大寫，這樣大小寫就能統一統計。
        for ch in line.upper():
            # 只接受 A~Z，其他符號、數字、空白都忽略。
            if "A" <= ch <= "Z":
                # 例：'A' -> 0, 'B' -> 1, ..., 'Z' -> 25
                freq[ord(ch) - ord("A")] += 1

    # 把計數陣列轉回 (字母, 次數) 的列表，便於排序輸出。
    pairs: list[tuple[str, int]] = []
    for i, count in enumerate(freq):
        if count > 0:
            pairs.append((chr(ord("A") + i), count))

    # 排序規則：
    # 1) -次數：次數大排前面
    # 2) 字母：同次數時字母小排前面
    pairs.sort(key=lambda x: (-x[1], x[0]))

    # 若完全沒有英文字母，題目不需要輸出任何行。
    if not pairs:
        return ""

    # 每行輸出格式為：<字母><空白><次數>
    # 最後補一個換行，符合 UVA 常見輸出習慣。
    return "\n".join(f"{ch} {count}" for ch, count in pairs) + "\n"


def main() -> None:
    # 標準輸入輸出入口：讀 stdin，印出 solve 的結果。
    print(solve(sys.stdin.read()), end="")


if __name__ == "__main__":
    main()

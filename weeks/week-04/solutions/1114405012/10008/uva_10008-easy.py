from __future__ import annotations

import sys


def solve(data: str) -> str:
    """
    UVA 10008 easy 版（好記版）

    解題口訣：
    - 先把所有字母轉成大寫來統一。
    - 只統計 A~Z。
    - 排序規則：次數多的在前；次數一樣時字母小的在前。
    """
    lines = data.splitlines()
    if not lines:
        return ""

    # 第一行代表要分析的文字行數
    try:
        n = int(lines[0].strip())
    except ValueError:
        return ""

    # 用 dict 存每個大寫字母出現次數，初始都設成 0
    # 這樣最後輸出前可以簡單過濾 count > 0 的項目
    freq: dict[str, int] = {chr(code): 0 for code in range(ord("A"), ord("Z") + 1)}

    # 只處理接下來 n 行（若輸入不足 n 行，也不會越界）
    for line in lines[1 : 1 + n]:
        for ch in line:
            if ch.isalpha():
                upper_ch = ch.upper()
                # 題目範圍是英文字母，因此只加總 A~Z
                if "A" <= upper_ch <= "Z":
                    freq[upper_ch] += 1

    # 過濾：沒有出現過的字母不輸出
    items = [(ch, count) for ch, count in freq.items() if count > 0]

    # 排序：
    # 1) 次數由大到小 -> -count
    # 2) 若次數相同，字母由小到大 -> ch
    items.sort(key=lambda x: (-x[1], x[0]))

    # 每行格式：大寫字母 空白 次數
    return "\n".join(f"{ch} {count}" for ch, count in items)


def main() -> None:
    text = sys.stdin.read()
    sys.stdout.write(solve(text))


if __name__ == "__main__":
    main()

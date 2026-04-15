"""
UVA 10222 - Decode the Mad man
AI 教學簡單版本（含中文註解）
"""

import sys


def build_map() -> dict[str, str]:
    # 題目使用的鍵盤排列
    rows = [
        "`1234567890-=",
        "qwertyuiop[]\\",
        "asdfghjkl;'",
        "zxcvbnm,./",
    ]

    mp: dict[str, str] = {}

    for row in rows:
        # 瘋子打字時手往右偏，解碼時要換成左邊那顆鍵
        for i in range(1, len(row)):
            left = row[i - 1]
            right = row[i]
            mp[right] = left
            mp[right.upper()] = left.upper()

    return mp


def solve(data: str) -> str:
    mp = build_map()
    out = []

    for ch in data:
        # 空白、換行與不在映射表的符號原樣輸出
        out.append(mp.get(ch, ch))

    return "".join(out)


def main() -> None:
    data = sys.stdin.read()
    print(solve(data), end="")


if __name__ == "__main__":
    main()

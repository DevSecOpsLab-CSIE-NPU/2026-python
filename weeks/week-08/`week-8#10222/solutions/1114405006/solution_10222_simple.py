"""
UVA 10222 - Decode the Mad man
簡單版（CPE 現場可手打）
"""


def build_map():
    rows = [
        "`1234567890-=",
        "qwertyuiop[]\\",
        "asdfghjkl;'",
        "zxcvbnm,./",
    ]

    mp = {}
    for row in rows:
        # 瘋子手往右偏，解碼時把字元換成左邊那顆鍵
        for i in range(1, len(row)):
            mp[row[i]] = row[i - 1]
            mp[row[i].upper()] = row[i - 1].upper()
    return mp


def solve() -> None:
    import sys

    mp = build_map()
    out_lines = []

    for line in sys.stdin:
        decoded = []
        for ch in line:
            # 空白與不在鍵盤表內的字元原樣保留
            decoded.append(mp.get(ch, ch))
        out_lines.append("".join(decoded))

    sys.stdout.write("".join(out_lines))


if __name__ == "__main__":
    solve()

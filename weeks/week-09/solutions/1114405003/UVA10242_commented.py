# UVA 10242 - Fourth Point!!
# 詳細註解版（繁體中文）

import sys


def same(p, q) -> bool:
    # 輸入是十進位小數，直接比較即可；若擔心誤差可改用 epsilon
    return p[0] == q[0] and p[1] == q[1]


def solve() -> None:
    out = []

    # 每行有 8 個數字：x1 y1 x2 y2 x3 y3 x4 y4
    # 其中四點裡有一點重複出現兩次，需找出平行四邊形缺失的第四點
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        vals = list(map(float, line.split()))
        if len(vals) != 8:
            continue

        p1 = (vals[0], vals[1])
        p2 = (vals[2], vals[3])
        p3 = (vals[4], vals[5])
        p4 = (vals[6], vals[7])

        # 設重複點為 D，另外兩點為 A、B，則缺點 C = A + B - D
        if same(p1, p3):
            d, a, b = p1, p2, p4
        elif same(p1, p4):
            d, a, b = p1, p2, p3
        elif same(p2, p3):
            d, a, b = p2, p1, p4
        else:
            d, a, b = p2, p1, p3

        x = a[0] + b[0] - d[0]
        y = a[1] + b[1] - d[1]
        out.append(f"{x:.3f} {y:.3f}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()

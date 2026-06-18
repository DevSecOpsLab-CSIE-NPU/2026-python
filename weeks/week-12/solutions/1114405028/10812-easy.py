# 10812 UVA Beat the Spread! 簡易版
# 這個版本直接依照題意計算兩隊得分，並判斷是否存在非負整數解。

def solve() -> None:
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    t = int(next(it))
    out_lines = []

    for _ in range(t):
        s = int(next(it))
        d = int(next(it))
        if d > s or (s + d) % 2 == 1:
            out_lines.append("impossible")
            continue

        high = (s + d) // 2
        low = (s - d) // 2
        if low < 0:
            out_lines.append("impossible")
        else:
            out_lines.append(f"{high} {low}")

    sys.stdout.write("\n".join(out_lines) + ("\n" if out_lines else ""))


if __name__ == "__main__":
    solve()

# 10908 UVA Largest Square 簡易版
# 這個版本針對每個查詢從中心往外擴張，找到最大邊長。

def solve() -> None:
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    t = int(next(it))
    out_lines = []

    for _ in range(t):
        m = int(next(it))
        n = int(next(it))
        q = int(next(it))
        grid = [list(next(it).strip()) for _ in range(m)]
        out_lines.append(f"{m} {n} {q}")

        for _ in range(q):
            r = int(next(it))
            c = int(next(it))
            ch = grid[r][c]
            size = 1

            while True:
                half = size // 2
                top = r - half
                left = c - half
                bottom = r + half
                right = c + half
                if top < 0 or left < 0 or bottom >= m or right >= n:
                    break

                ok = True
                for i in range(top, bottom + 1):
                    if not ok:
                        break
                    for j in range(left, right + 1):
                        if grid[i][j] != ch:
                            ok = False
                            break
                if not ok:
                    break

                size += 2

            out_lines.append(str(size - 2))

    sys.stdout.write("\n".join(out_lines) + ("\n" if out_lines else ""))


if __name__ == "__main__":
    solve()

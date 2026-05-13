# UVA 10908 - Largest Square
# 簡單版本（含中文註解）

import sys


def main() -> None:
    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        return

    t = int(lines[0].strip())
    i = 1
    out = []

    for _ in range(t):
        # 有些測資會有空行，先跳過
        while i < len(lines) and lines[i].strip() == "":
            i += 1

        m, n, q = map(int, lines[i].split())
        i += 1

        grid = []
        for _r in range(m):
            grid.append(lines[i].rstrip("\n"))
            i += 1

        out.append(f"{m} {n} {q}")

        for _query in range(q):
            r, c = map(int, lines[i].split())
            i += 1

            ch = grid[r][c]
            radius = 0

            # 每次把半徑加 1（邊長加 2），檢查新增外框是否都同字元
            while True:
                nr = radius + 1
                top = r - nr
                bottom = r + nr
                left = c - nr
                right = c + nr

                # 出界就不能再擴
                if top < 0 or left < 0 or bottom >= m or right >= n:
                    break

                ok = True

                # 檢查上邊與下邊
                for col in range(left, right + 1):
                    if grid[top][col] != ch or grid[bottom][col] != ch:
                        ok = False
                        break

                # 檢查左邊與右邊
                if ok:
                    for row in range(top, bottom + 1):
                        if grid[row][left] != ch or grid[row][right] != ch:
                            ok = False
                            break

                if not ok:
                    break

                radius = nr

            out.append(str(2 * radius + 1))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

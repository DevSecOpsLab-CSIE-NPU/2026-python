import sys


def main() -> None:
    # 讀取整份輸入，方便一次處理多組測資。
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    p = 0
    t = int(data[p])
    p += 1
    out = []

    for _ in range(t):
        m = int(data[p])
        n = int(data[p + 1])
        q = int(data[p + 2])
        p += 3

        grid = [data[p + i].decode() for i in range(m)]
        p += m

        out.append(f"{m} {n} {q}")

        for _ in range(q):
            r = int(data[p])
            c = int(data[p + 1])
            p += 2

            ch = grid[r][c]
            k = 0

            # 只要新擴大的正方形還在範圍內，而且每個字元都相同，就繼續擴張。
            while True:
                nk = k + 1
                if r - nk < 0 or c - nk < 0 or r + nk >= m or c + nk >= n:
                    break

                ok = True
                for i in range(r - nk, r + nk + 1):
                    for j in range(c - nk, c + nk + 1):
                        if grid[i][j] != ch:
                            ok = False
                            break
                    if not ok:
                        break

                if not ok:
                    break

                k = nk

            out.append(str(2 * k + 1))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
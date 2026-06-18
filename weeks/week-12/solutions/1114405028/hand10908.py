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
            char = grid[r][c]
            length = 1

            while True:
                half = length // 2
                top = r - half
                left = c - half
                bottom = r + half
                right = c + half
                if top < 0 or left < 0 or bottom >= m or right >= n:
                    break

                valid = True
                for i in range(top, bottom + 1):
                    for j in range(left, right + 1):
                        if grid[i][j] != char:
                            valid = False
                            break
                    if not valid:
                        break

                if not valid:
                    break
                length += 2

            out_lines.append(str(length - 2))

    sys.stdout.write("\n".join(out_lines) + ("\n" if out_lines else ""))


if __name__ == "__main__":
    solve()

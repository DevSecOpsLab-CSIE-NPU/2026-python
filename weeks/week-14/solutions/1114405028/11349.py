def solve() -> None:
    import sys

    data = sys.stdin.read().strip().splitlines()
    if not data:
        return

    t = int(data[0].strip())
    out = []
    line_idx = 1

    for case in range(1, t + 1):
        n = int(data[line_idx].split('=')[1].strip())
        line_idx += 1
        matrix = []

        for _ in range(n):
            matrix.append(list(map(int, data[line_idx].split())))
            line_idx += 1

        symmetric = True
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0 or matrix[i][j] != matrix[n - 1 - i][n - 1 - j]:
                    symmetric = False
                    break
            if not symmetric:
                break

        if symmetric:
            out.append(f"Test #{case}: Symmetric.")
        else:
            out.append(f"Test #{case}: Non-symmetric.")

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


if __name__ == "__main__":
    solve()

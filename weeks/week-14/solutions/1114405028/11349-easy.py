# 11349 Symmetric Matrix 簡易版
# 判斷方陣是否為中心對稱矩陣，並且所有元素皆為非負數。

def solve() -> None:
    import sys

    data = sys.stdin.read().strip().splitlines()
    if not data:
        return

    t = int(data[0].strip())
    out = []
    line_idx = 1

    for case in range(1, t + 1):
        header = data[line_idx].strip()
        line_idx += 1
        n = int(header.split('=')[1])

        matrix = []
        for _ in range(n):
            row = list(map(int, data[line_idx].split()))
            matrix.append(row)
            line_idx += 1

        symmetric = True
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0 or matrix[i][j] != matrix[n - 1 - i][n - 1 - j]:
                    symmetric = False
                    break
            if not symmetric:
                break

        label = "Symmetric" if symmetric else "Non-symmetric"
        out.append(f"Test #{case}: {label}.")

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


if __name__ == "__main__":
    solve()

import re
import sys


def solve(data):
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    t = int(lines[0])
    idx = 1
    out = []

    for case_id in range(1, t + 1):
        n = int(re.search(r"\d+", lines[idx]).group())
        idx += 1

        mat = []
        for _ in range(n):
            mat.append(list(map(int, lines[idx].split())))
            idx += 1

        ok = True
        for i in range(n):
            for j in range(n):
                if mat[i][j] < 0 or mat[i][j] != mat[n - 1 - i][n - 1 - j]:
                    ok = False
                    break
            if not ok:
                break

        out.append(f"Test #{case_id}: {'Symmetric.' if ok else 'Non-symmetric.'}")

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
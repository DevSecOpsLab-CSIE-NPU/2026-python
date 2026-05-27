from __future__ import annotations

import sys


def is_symmetric(matrix: list[list[int]]) -> bool:
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            value = matrix[i][j]
            if value < 0:
                return False
            if value != matrix[n - 1 - i][n - 1 - j]:
                return False
    return True


def solve(data: str) -> str:
    lines = data.strip().splitlines()
    if not lines:
        return ""

    t = int(lines[0].strip())
    idx = 1
    out: list[str] = []

    for case_id in range(1, t + 1):
        n_line = lines[idx].strip()
        idx += 1
        n = int(n_line.split("=")[1].strip())

        matrix: list[list[int]] = []
        for _ in range(n):
            row = list(map(int, lines[idx].split()))
            idx += 1
            matrix.append(row)

        if is_symmetric(matrix):
            out.append(f"Test #{case_id}: Symmetric.")
        else:
            out.append(f"Test #{case_id}: Non-symmetric.")

    return "\n".join(out)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

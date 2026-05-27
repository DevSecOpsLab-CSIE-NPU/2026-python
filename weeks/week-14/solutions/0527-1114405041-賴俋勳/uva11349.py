"""UVA 11349 - Symmetric Matrix"""

from __future__ import annotations

import sys


def is_symmetric_matrix(matrix: list[list[int]]) -> bool:
    """檢查是否同時滿足非負與中心對稱。"""
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
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    t = int(lines[0])
    idx = 1
    out: list[str] = []

    for case_no in range(1, t + 1):
        n_line = lines[idx]
        idx += 1
        n = int(n_line.split("=")[1].strip())

        matrix: list[list[int]] = []
        for _ in range(n):
            row = list(map(int, lines[idx].split()))
            idx += 1
            matrix.append(row)

        ans = "Symmetric." if is_symmetric_matrix(matrix) else "Non-symmetric."
        out.append(f"Test #{case_no}: {ans}")

    return "\n".join(out)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

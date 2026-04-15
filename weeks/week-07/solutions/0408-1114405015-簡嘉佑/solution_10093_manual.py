"""
UVA 10093 manual solution.

Problem:
Deploy artillery on N x M grid to maximize count while avoiding mutual attacks.
Attack range: 2 cells in all four directions (up, down, left, right).

Algorithm:
Backtracking - try placing or not placing artillery at each position.
Check if position conflicts with already placed units (Chebyshev distance > 2).

Time: O(2^(N*M)) worst case, but fast with pruning.
Space: O(N*M)
"""

from __future__ import annotations

from typing import List


def count_artillery(n: int, m: int, grid: List[str]) -> int:
    """Count maximum artillery that can be placed without conflicts."""
    max_count = [0]

    def can_place(r: int, c: int, placed: List[tuple]) -> bool:
        """Check if position (r, c) can place artillery."""
        if grid[r][c] == "H":
            return False
        for pr, pc in placed:
            # Chebyshev distance must be > 2
            if abs(pr - r) <= 2 and abs(pc - c) <= 2 and (pr != r or pc != c):
                return False
        return True

    def backtrack(row: int, col: int, placed: List[tuple]) -> None:
        """Scan all positions and try placing or not placing."""
        # Finished scanning all positions
        if row >= n:
            max_count[0] = max(max_count[0], len(placed))
            return

        # Calculate next position
        next_row = row
        next_col = col + 1
        if next_col >= m:
            next_row += 1
            next_col = 0

        # Option 1: do not place at (row, col)
        backtrack(next_row, next_col, placed)

        # Option 2: try to place at (row, col)
        if can_place(row, col, placed):
            backtrack(next_row, next_col, placed + [(row, col)])

    backtrack(0, 0, [])
    return max_count[0]


def main() -> None:
    """Read input and output result."""
    import sys

    lines = sys.stdin.read().strip().split("\n")
    n, m = map(int, lines[0].split())
    grid = [lines[i + 1] for i in range(n)]

    result = count_artillery(n, m, grid)
    sys.stdout.write(str(result))


if __name__ == "__main__":
    main()

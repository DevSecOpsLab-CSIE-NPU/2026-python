"""
UVA 10101 - Sticks Puzzle (manual English version)

Model used in this file:
- Only digits can change.
- One move means: one digit loses one stick, another digit gains one stick.
- Operators (+, -, =) are unchanged.
"""

from __future__ import annotations

from typing import Optional


STICKS = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def _delta(src: int, dst: int) -> int:
    """Return sticks difference dst-src if abs(diff)==1; otherwise 0."""
    diff = STICKS[dst] - STICKS[src]
    return diff if abs(diff) == 1 else 0


def _is_true_equation(expr: str) -> bool:
    """Evaluate whether the equation is mathematically true."""
    try:
        left, right = expr.split("=", 1)
        return eval(left) == eval(right)
    except Exception:
        return False


def solve_equation(equation: str) -> Optional[str]:
    """Return one valid equation after moving one stick, or None."""
    if equation.count("=") != 1:
        return None

    positions = [i for i, ch in enumerate(equation) if ch.isdigit()]
    base = list(equation)

    for i in positions:
        old_i = ord(base[i]) - ord("0")
        for new_i in range(10):
            if new_i == old_i or _delta(old_i, new_i) != -1:
                continue

            step1 = base[:]
            step1[i] = str(new_i)

            for j in positions:
                if j == i:
                    continue
                old_j = ord(base[j]) - ord("0")
                for new_j in range(10):
                    if new_j == old_j or _delta(old_j, new_j) != 1:
                        continue

                    step2 = step1[:]
                    step2[j] = str(new_j)
                    candidate = "".join(step2)
                    if _is_true_equation(candidate):
                        return candidate

    return None


def main() -> None:
    import sys

    raw = sys.stdin.read().strip()
    equation = raw.split("#", 1)[0]
    ans = solve_equation(equation)

    if ans is None:
        sys.stdout.write("No\n")
    else:
        sys.stdout.write(ans + "#\n")


if __name__ == "__main__":
    main()

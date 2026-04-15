"""
UVA 948 - Fake Coin Detection (manual version)

Problem summary:
  N coins, one is fake (lighter or heavier than the rest).
  K weighings, each records left coins, right coins, and result (< > =).
  Find the fake coin number; output 0 if it cannot be uniquely determined.

Algorithm:
  For each coin, try assuming it is the fake and is either heavy or light.
  A hypothesis is valid if it is consistent with every weighing result.
  If exactly one coin passes (regardless of heavy/light), output it; else 0.
"""

from __future__ import annotations

import sys


def is_consistent(coin: int, heavy: bool,
                  weighings: list[tuple[list[int], list[int], str]]) -> bool:
    for left, right, result in weighings:
        on_left  = coin in left
        on_right = coin in right

        if result == "=":
            if on_left or on_right:
                return False
        elif result == "<":
            if not on_left and not on_right:
                return False
            if on_left and heavy:
                return False
            if on_right and not heavy:
                return False
        else:  # ">"
            if not on_left and not on_right:
                return False
            if on_left and not heavy:
                return False
            if on_right and heavy:
                return False

    return True


def find_fake(n: int,
              weighings: list[tuple[list[int], list[int], str]]) -> int:
    candidates = []
    for coin in range(1, n + 1):
        if is_consistent(coin, True, weighings) or \
           is_consistent(coin, False, weighings):
            candidates.append(coin)
    return candidates[0] if len(candidates) == 1 else 0


def main() -> None:
    lines = [l.strip() for l in sys.stdin.read().splitlines() if l.strip()]
    idx = 0
    m = int(lines[idx]); idx += 1
    out = []
    for _ in range(m):
        n, k = map(int, lines[idx].split()); idx += 1
        weighings = []
        for _ in range(k):
            parts = lines[idx].split(); idx += 1
            p = int(parts[0])
            left  = list(map(int, parts[1: p + 1]))
            right = list(map(int, parts[p + 1: 2 * p + 1]))
            res   = lines[idx]; idx += 1
            weighings.append((left, right, res))
        out.append(str(find_fake(n, weighings)))
    sys.stdout.write("\n\n".join(out) + "\n")


if __name__ == "__main__":
    main()

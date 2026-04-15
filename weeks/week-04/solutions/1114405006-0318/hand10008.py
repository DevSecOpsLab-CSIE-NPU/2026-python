from __future__ import annotations

import sys


def solve(data: str) -> str:
    lines = data.splitlines()
    if not lines:
        return ""

    n = int(lines[0].strip() or "0")
    counts = [0] * 26

    for line in lines[1 : 1 + n]:
        for ch in line.upper():
            if "A" <= ch <= "Z":
                counts[ord(ch) - ord("A")] += 1

    items = []
    for i, count in enumerate(counts):
        if count > 0:
            items.append((chr(ord("A") + i), count))

    items.sort(key=lambda item: (-item[1], item[0]))

    if not items:
        return ""

    return "\n".join(f"{ch} {count}" for ch, count in items) + "\n"


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
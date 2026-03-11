"""UVA 118 - Mutant Flatworld Explorers（簡單版）"""

import sys


DIRECTIONS = "NESW"
MOVE = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


def solve(data: str) -> str:
    lines = [line.rstrip("\n") for line in data.splitlines() if line.strip() != ""]
    if not lines:
        return ""

    max_x, max_y = map(int, lines[0].split())
    scents = set()
    out = []

    idx = 1
    while idx + 1 < len(lines):
        x, y, d = lines[idx].split()
        x, y = int(x), int(y)
        commands = lines[idx + 1].strip()
        idx += 2

        lost = False
        for cmd in commands:
            if cmd == "L":
                d = DIRECTIONS[(DIRECTIONS.index(d) - 1) % 4]
            elif cmd == "R":
                d = DIRECTIONS[(DIRECTIONS.index(d) + 1) % 4]
            else:
                dx, dy = MOVE[d]
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx > max_x or ny > max_y:
                    if (x, y) in scents:
                        continue
                    scents.add((x, y))
                    lost = True
                    break
                x, y = nx, ny

        if lost:
            out.append(f"{x} {y} {d} LOST")
        else:
            out.append(f"{x} {y} {d}")

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))

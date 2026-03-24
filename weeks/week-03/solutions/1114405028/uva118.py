import sys


DIRS = "NESW"
MOVE = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


def turn(direction, cmd):
    idx = DIRS.index(direction)
    if cmd == "L":
        return DIRS[(idx - 1) % 4]
    return DIRS[(idx + 1) % 4]


def main():
    lines = [line.rstrip("\n") for line in sys.stdin if line.strip() != ""]
    if not lines:
        return

    max_x, max_y = map(int, lines[0].split())
    scent = set()

    out = []
    i = 1
    while i + 1 < len(lines):
        x, y, direction = lines[i].split()
        x, y = int(x), int(y)
        instructions = lines[i + 1].strip()
        i += 2

        lost = False
        for cmd in instructions:
            if cmd in ("L", "R"):
                direction = turn(direction, cmd)
                continue

            dx, dy = MOVE[direction]
            nx, ny = x + dx, y + dy

            if 0 <= nx <= max_x and 0 <= ny <= max_y:
                x, y = nx, ny
                continue

            if (x, y) in scent:
                continue

            scent.add((x, y))
            lost = True
            break

        if lost:
            out.append(f"{x} {y} {direction} LOST")
        else:
            out.append(f"{x} {y} {direction}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

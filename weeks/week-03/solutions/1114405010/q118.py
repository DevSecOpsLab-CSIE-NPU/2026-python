"""UVA 118 - Mutant Flatworld Explorers"""

import sys


ORDER = "NESW"
STEP = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


def rotate_left(direction: str) -> str:
    return ORDER[(ORDER.index(direction) - 1) % 4]


def rotate_right(direction: str) -> str:
    return ORDER[(ORDER.index(direction) + 1) % 4]


def solve(text: str) -> str:
    rows = [line.rstrip("\n") for line in text.splitlines() if line.strip() != ""]
    if not rows:
        return ""

    world_x, world_y = map(int, rows[0].split())
    scented_positions = set()
    answer = []

    i = 1
    while i + 1 < len(rows):
        sx, sy, direction = rows[i].split()
        x, y = int(sx), int(sy)
        instructions = rows[i + 1].strip()
        i += 2

        is_lost = False
        for ins in instructions:
            if ins == "L":
                direction = rotate_left(direction)
                continue
            if ins == "R":
                direction = rotate_right(direction)
                continue

            dx, dy = STEP[direction]
            next_x, next_y = x + dx, y + dy

            out_of_world = (
                next_x < 0 or next_y < 0 or next_x > world_x or next_y > world_y
            )
            if not out_of_world:
                x, y = next_x, next_y
                continue

            if (x, y) in scented_positions:
                continue

            scented_positions.add((x, y))
            is_lost = True
            break

        if is_lost:
            answer.append(f"{x} {y} {direction} LOST")
        else:
            answer.append(f"{x} {y} {direction}")

    return "\n".join(answer)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))

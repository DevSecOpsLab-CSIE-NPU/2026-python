import sys

dirs = ["N", "E", "S", "W"]
move = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0)
}

max_x, max_y = map(int, sys.stdin.readline().split())

scent = set()

for line in sys.stdin:

    if not line.strip():
        continue

    x, y, d = line.split()
    x = int(x)
    y = int(y)

    commands = sys.stdin.readline().strip()

    lost = False

    for c in commands:

        if c == "L":
            d = dirs[(dirs.index(d) - 1) % 4]

        elif c == "R":
            d = dirs[(dirs.index(d) + 1) % 4]

        else:
            dx, dy = move[d]
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx > max_x or ny > max_y:

                if (x, y, d) in scent:
                    continue

                scent.add((x, y, d))
                lost = True
                break

            x, y = nx, ny

    if lost:
        print(x, y, d, "LOST")
    else:
        print(x, y, d)
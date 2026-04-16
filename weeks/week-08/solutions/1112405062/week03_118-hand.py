DIRS = ["N", "E", "S", "W"]
DX = [0, 1, 0, -1]  
DY = [1, 0, -1, 0]  


def turn_left(d):
    return (d + 3) % 4


def turn_right(d):
    return (d + 1) % 4


def solve():

    import sys

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            lines = [line.strip() for line in f if line.strip()]
    else:
        lines = [line.strip() for line in sys.stdin if line.strip()]
    max_x, max_y = map(int, lines[0].split())

    scents = set()

    for i in range(1, len(lines), 2):
        x, y, d_char = lines[i].split()
        x, y = int(x), int(y)
        d = DIRS.index(d_char)

        cmds = lines[i + 1]

        lost = False

        for cmd in cmds:
            if cmd == "L":
                d = turn_left(d)
            elif cmd == "R":
                d = turn_right(d)
            else:
                nx, ny = x + DX[d], y + DY[d]
                if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                    if (x, y) not in scents:
                        lost = True
                        scents.add((x, y))
                        break
                else:
                    x, y = nx, ny
        result = f"{x} {y} {DIRS[d]}"
        if lost:
            result += " LOST"
        print(result)

if __name__ == "__main__":
    solve()
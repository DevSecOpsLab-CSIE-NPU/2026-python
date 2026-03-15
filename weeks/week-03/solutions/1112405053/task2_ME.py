import sys


def solve() -> None:
    lines = [line.strip() for line in sys.stdin if line.strip()]
    if not lines:
        return

    max_x, max_y = map(int, lines[0].split())

    scent = set()

    dirs = ["N", "E", "S", "W"]
    delta = {
        "N": (0, 1),
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0),
    }
 
    out = []
    i = 1
    while i + 1 < len(lines):
        x, y, d = lines[i].split()
        x = int(x)
        y = int(y)
        cmd = lines[i + 1]
        i += 2

        lost = False

        for c in cmd:
            if c == "L":
                d = dirs[(dirs.index(d) - 1) % 4]
            elif c == "R":
                d = dirs[(dirs.index(d) + 1) % 4]
            else:  # c == "F"
                dx, dy = delta[d]
                nx, ny = x + dx, y + dy

                if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                    if (x, y) in scent:
                        continue
                    scent.add((x, y))
                    lost = True
                    break

                x, y = nx, ny

        if lost:
            out.append(f"{x} {y} {d} LOST")
        else:
            out.append(f"{x} {y} {d}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()


DIRECTIONS = "NESW"
STEP = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}
def main() -> None:
    import sys
    lines = [line.strip() for line in sys.stdin if line.strip()]
    if not lines:
        return
    max_x, max_y = map(int, lines[0].split())
    scent = set()
    i = 1
    while i + 1 < len(lines):
        x, y, d = lines[i].split()
        x = int(x)
        y = int(y)
        commands = lines[i + 1]
        lost = False
        for cmd in commands:
            if cmd == "L":
                d = DIRECTIONS[(DIRECTIONS.index(d) - 1) % 4]
            elif cmd == "R":
                d = DIRECTIONS[(DIRECTIONS.index(d) + 1) % 4]
            else:
                dx, dy = STEP[d]
                nx, ny = x + dx, y + dy
                if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                    key = (x, y, d)
                    if key in scent:
                        continue
                    scent.add(key)
                    lost = True
                    break
                x, y = nx, ny
        if lost:
            print(f"{x} {y} {d} LOST")
        else:
            print(f"{x} {y} {d}")
        i += 2
if __name__ == "__main__":
    main()
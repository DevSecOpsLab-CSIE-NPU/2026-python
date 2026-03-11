import sys

RIGHT = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
LEFT  = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
DX = {'N':  0, 'E':  1, 'S':  0, 'W': -1}
DY = {'N':  1, 'E':  0, 'S': -1, 'W':  0}

def solve(input_text):
    lines = [l.strip() for l in input_text.strip().splitlines() if l.strip()]
    max_x, max_y = map(int, lines[0].split())
    scents = set()
    out = []
    i = 1

    while i + 1 < len(lines):
        parts = lines[i].split()
        x, y, d = int(parts[0]), int(parts[1]), parts[2]
        cmds = lines[i + 1]
        i += 2
        lost = False

        for cmd in cmds:
            if cmd == 'L':
                d = LEFT[d]
            elif cmd == 'R':
                d = RIGHT[d]
            elif cmd == 'F':
                nx = x + DX[d]
                ny = y + DY[d]
                if 0 <= nx <= max_x and 0 <= ny <= max_y:
                    x, y = nx, ny
                elif (x, y) in scents:
                    pass
                else:
                    scents.add((x, y))
                    lost = True
                    break

        if lost:
            out.append(f"{x} {y} {d} LOST")
        else:
            out.append(f"{x} {y} {d}")

    return "\n".join(out)

if __name__ == "__main__":
    print(solve(sys.stdin.read()))
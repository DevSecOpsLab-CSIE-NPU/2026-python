import sys

def main():
    lines = sys.stdin.readlines()
    idx = 0
    w, h = map(int, lines[idx].split())
    idx += 1
    scents = set()

    while idx < len(lines):
        x, y, d = lines[idx].split()
        x, y = int(x), int(y)
        instr = lines[idx + 1].strip()
        idx += 2

        lost = False
        for c in instr:
            if c == 'L':
                if d == 'N': d = 'W'
                elif d == 'W': d = 'S'
                elif d == 'S': d = 'E'
                elif d == 'E': d = 'N'
            elif c == 'R':
                if d == 'N': d = 'E'
                elif d == 'E': d = 'S'
                elif d == 'S': d = 'W'
                elif d == 'W': d = 'N'
            elif c == 'F':
                nx, ny = x, y
                if d == 'N': ny += 1
                elif d == 'S': ny -= 1
                elif d == 'E': nx += 1
                elif d == 'W': nx -= 1
                if 0 <= nx <= w and 0 <= ny <= h:
                    x, y = nx, ny
                else:
                    if (x, y) not in scents:
                        scents.add((x, y))
                        lost = True
                        break
        print(f"{x} {y} {d}", end="")
        if lost:
            print(" LOST")
        else:
            print()

if __name__ == "__main__":
    main()
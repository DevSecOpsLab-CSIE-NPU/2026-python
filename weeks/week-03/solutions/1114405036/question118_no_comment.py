def solve_118(input_text):
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    max_x, max_y = map(int, lines[0].split())
    scents = set()
    out = []
    dirs = 'NESW'
    for i in range(1, len(lines), 2):
        x, y, d = lines[i].split()
        x, y = int(x), int(y)
        lost = False
        for c in lines[i+1].strip():
            if c == 'L':
                d = dirs[(dirs.index(d) - 1) % 4]
            elif c == 'R':
                d = dirs[(dirs.index(d) + 1) % 4]
            else:
                nx, ny = x, y
                if d == 'N':
                    ny += 1
                elif d == 'S':
                    ny -= 1
                elif d == 'E':
                    nx += 1
                else:
                    nx -= 1
                if 0 <= nx <= max_x and 0 <= ny <= max_y:
                    x, y = nx, ny
                elif (x, y, d) not in scents:
                    scents.add((x, y, d))
                    lost = True
                    break
        out.append(f"{x} {y} {d}" + (" LOST" if lost else ""))
    return "\n".join(out)

if __name__ == '__main__':
    import sys
    print(solve_118(sys.stdin.read()).strip())

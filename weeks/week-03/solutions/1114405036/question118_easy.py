def solve_118(input_text):
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    max_x, max_y = map(int, lines[0].split())
    scents = set()
    results = []
    directions = 'NESW'

    for i in range(1, len(lines), 2):
        x, y, d = lines[i].split()
        x, y = int(x), int(y)
        for cmd in lines[i + 1].strip():
            if cmd == 'L':
                d = directions[(directions.index(d) - 1) % 4]
            elif cmd == 'R':
                d = directions[(directions.index(d) + 1) % 4]
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
                    results.append(f"{x} {y} {d} LOST")
                    break
        else:
            results.append(f"{x} {y} {d}")
    return "\n".join(results)

if __name__ == '__main__':
    import sys
    print(solve_118(sys.stdin.read()).strip())

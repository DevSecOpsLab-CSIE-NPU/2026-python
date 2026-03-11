import sys

dirs = ['N', 'E', 'S', 'W']
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

lines = sys.stdin.read().split('\n')
idx = 0
mx, my = map(int, lines[idx].split())
idx += 1

scents = set()

while idx < len(lines):
    line = lines[idx].strip()
    idx += 1
    if not line:
        continue
    parts = line.split()
    x, y, d = int(parts[0]), int(parts[1]), parts[2]
    di = dirs.index(d)

    if idx >= len(lines):
        break
    cmds = lines[idx].strip()
    idx += 1

    lost = False
    for c in cmds:
        if c == 'L':
            di = (di + 3) % 4
        elif c == 'R':
            di = (di + 1) % 4
        elif c == 'F':
            nx = x + dx[di]
            ny = y + dy[di]
            if nx < 0 or nx > mx or ny < 0 or ny > my:
                if (x, y, di) in scents:
                    continue
                scents.add((x, y, di))
                lost = True
                break
            x, y = nx, ny

    if lost:
        print(x, y, dirs[di], "LOST")
    else:
        print(x, y, dirs[di])

import sys


left = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
right = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
step = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}


def main():
    data = [line.strip() for line in sys.stdin if line.strip()]
    if not data:
        return

    x_max, y_max = map(int, data[0].split())
    scent = set()
    out = []
    i = 1

    while i < len(data):
        x, y, d = data[i].split()
        x = int(x)
        y = int(y)
        commands = data[i + 1]
        i += 2

        lost = False

        for cmd in commands:
            if cmd == 'L':
                d = left[d]
            elif cmd == 'R':
                d = right[d]
            else:
                dx, dy = step[d]
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx > x_max or ny < 0 or ny > y_max:
                    if (x, y, d) in scent:
                        continue
                    scent.add((x, y, d))
                    lost = True
                    break

                x = nx
                y = ny

        line = f'{x} {y} {d}'
        if lost:
            line += ' LOST'
        out.append(line)

    sys.stdout.write('\n'.join(out) + ('\n' if out else ''))


if __name__ == '__main__':
    main()
import sys


def solve(data: str) -> str:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    max_x, max_y = map(int, lines[0].split())
    dirs = "NESW"
    move = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
    scent = set()

    out = []
    i = 1
    while i + 1 < len(lines):
        x_str, y_str, d = lines[i].split()
        cmds = lines[i + 1]
        i += 2

        x, y = int(x_str), int(y_str)
        lost = False

        for c in cmds:
            if c == "L":
                d = dirs[(dirs.index(d) - 1) % 4]
            elif c == "R":
                d = dirs[(dirs.index(d) + 1) % 4]
            else:
                dx, dy = move[d]
                nx, ny = x + dx, y + dy
                if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                    if (x, y, d) in scent:
                        continue
                    scent.add((x, y, d))
                    lost = True
                    break
                x, y = nx, ny

        if lost:
            out.append(f"{x} {y} {d} LOST")
        else:
            out.append(f"{x} {y} {d}")

    return "\n".join(out)


def main() -> None:
    data = sys.stdin.read()
    ans = solve(data)
    if ans:
        print(ans)


if __name__ == "__main__":
    main()

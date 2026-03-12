"""
UVA 118 手打版（簡單好記）

重點：
- 方向表 N,E,S,W
- L/R 只改方向
- F 嘗試前進，若出界則看 scent 是否忽略
"""

dirs = ["N", "E", "S", "W"]
step = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


def turn(d: str, cmd: str) -> str:
    i = dirs.index(d)
    if cmd == "L":
        return dirs[(i - 1) % 4]
    return dirs[(i + 1) % 4]


def out_of_map(x: int, y: int, mx: int, my: int) -> bool:
    return x < 0 or x > mx or y < 0 or y > my


def run_robot(x: int, y: int, d: str, cmds: str, mx: int, my: int, scent: set):
    for c in cmds:
        if c in ("L", "R"):
            d = turn(d, c)
            continue

        dx, dy = step[d]
        nx, ny = x + dx, y + dy

        if out_of_map(nx, ny, mx, my):
            if (x, y) in scent:
                continue
            scent.add((x, y))
            return x, y, d, True

        x, y = nx, ny

    return x, y, d, False


def solve_all(text: str) -> str:
    lines = [s.strip() for s in text.splitlines() if s.strip()]
    if not lines:
        return ""

    mx, my = map(int, lines[0].split())
    scent = set()
    ans = []

    i = 1
    while i + 1 < len(lines):
        x, y, d = lines[i].split()
        cmds = lines[i + 1]

        fx, fy, fd, lost = run_robot(int(x), int(y), d, cmds, mx, my, scent)
        if lost:
            ans.append(f"{fx} {fy} {fd} LOST")
        else:
            ans.append(f"{fx} {fy} {fd}")

        i += 2

    return "\n".join(ans)


if __name__ == "__main__":
    import sys

    data = sys.stdin.read()
    if data.strip():
        print(solve_all(data))

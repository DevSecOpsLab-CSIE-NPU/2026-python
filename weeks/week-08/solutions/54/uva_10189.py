import sys


NEIGHBORS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def annotate_field(grid: list[str]) -> list[str]:
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    out = [["0" for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "*":
                out[r][c] = "*"
                continue

            mines = 0
            for dr, dc in NEIGHBORS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "*":
                    mines += 1
            out[r][c] = str(mines)

    return ["".join(row) for row in out]


def solve(data: str) -> str:
    lines = data.splitlines()
    i = 0
    case_no = 1
    blocks: list[str] = []

    while i < len(lines):
        line = lines[i].strip()
        i += 1
        if not line:
            continue

        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break

        grid = []
        for _ in range(n):
            grid.append(lines[i].rstrip("\n"))
            i += 1

        annotated = annotate_field(grid)
        block = [f"Field #{case_no}:"] + annotated
        blocks.append("\n".join(block))
        case_no += 1

    return "\n\n".join(blocks)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

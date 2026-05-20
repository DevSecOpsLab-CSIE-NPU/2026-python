"""週 13 題目 11321：動態判斷新陷阱會不會把柏油路封死。"""

import sys


def find(parent: list[int], x: int) -> int:
    """路徑壓縮版 find。"""
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(parent: list[int], size: list[int], top_touch: list[bool], bottom_touch: list[bool], a: int, b: int) -> int:
    """合併兩個已被封住的區塊。"""
    ra = find(parent, a)
    rb = find(parent, b)
    if ra == rb:
        return ra

    if size[ra] < size[rb]:
        ra, rb = rb, ra

    parent[rb] = ra
    size[ra] += size[rb]
    top_touch[ra] = top_touch[ra] or top_touch[rb]
    bottom_touch[ra] = bottom_touch[ra] or bottom_touch[rb]
    return ra


def solve_case(rows: int, cols: int, traps: list[tuple[int, int]]) -> list[str]:
    """依序判斷每個陷阱能不能放。"""
    total = rows * cols
    blocked = bytearray(total)
    parent = [-1] * total
    size = [0] * total
    top_touch = [False] * total
    bottom_touch = [False] * total

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]

    output: list[str] = []

    for x, y in traps:
        cell = x * cols + y

        # 先找出所有相鄰的封住區塊，判斷這個新陷阱會不會把上邊界和下邊界接起來。
        roots: list[int] = []
        seen: set[int] = set()
        touches_top = x == 0
        touches_bottom = x == rows - 1

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < rows and 0 <= ny < cols):
                continue
            neighbor = nx * cols + ny
            if not blocked[neighbor]:
                continue
            root = find(parent, neighbor)
            if root in seen:
                continue
            seen.add(root)
            roots.append(root)
            touches_top = touches_top or top_touch[root]
            touches_bottom = touches_bottom or bottom_touch[root]

        if touches_top and touches_bottom:
            output.append(">_<")
            continue

        # 可以放，正式把這格佔起來，並且跟相鄰區塊合併。
        output.append("<(_ _)>")
        blocked[cell] = 1
        parent[cell] = cell
        size[cell] = 1
        top_touch[cell] = x == 0
        bottom_touch[cell] = x == rows - 1

        for root in roots:
            cell = union(parent, size, top_touch, bottom_touch, cell, root)

    return output


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    index = 0
    output: list[str] = []
    while index < len(data):
        rows, cols, trap_count = data[index:index + 3]
        index += 3
        traps = []
        for _ in range(trap_count):
            x, y = data[index:index + 2]
            index += 2
            traps.append((x, y))
        output.extend(solve_case(rows, cols, traps))

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()
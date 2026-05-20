"""
週 13 題目 11321 - easy 版

這題可以把「陷阱」看成是逐步封住的格子。
我們只要知道：
1. 目前已封住的格子群，哪些碰到上邊界。
2. 哪些碰到下邊界。

如果一個新陷阱放上去之後，會把某個碰上邊界的區塊和某個碰上下邊界的區塊接在一起，
那麼上下邊界就被連通，柏油路也就被封死了，這個陷阱就不能放。

因為只會「新增」陷阱，不會移除，所以可以用並查集維護已封住的區塊。
"""

import sys


def find(parent: list[int], x: int) -> int:
    """並查集查找根節點。"""
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(parent: list[int], size: list[int], top_touch: list[bool], bottom_touch: list[bool], a: int, b: int) -> int:
    """合併兩個封住區塊，並把邊界資訊一起帶過去。"""
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
    total = rows * cols
    blocked = bytearray(total)
    parent = [-1] * total
    size = [0] * total
    top_touch = [False] * total
    bottom_touch = [False] * total

    # 8 個方向都要看，因為斜對角也可能把路徑擠死。
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]

    output: list[str] = []

    for x, y in traps:
        cell = x * cols + y

        # 先看看新陷阱附近有哪些已經封住的區塊。
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

        # 只要上、下邊界會被接起來，這個陷阱就不能放。
        if touches_top and touches_bottom:
            output.append(">_<")
            continue

        output.append("<(_ _)>")

        # 正式把這格封起來。
        blocked[cell] = 1
        parent[cell] = cell
        size[cell] = 1
        top_touch[cell] = x == 0
        bottom_touch[cell] = x == rows - 1

        # 再把它跟周圍同樣封住的區塊合併。
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
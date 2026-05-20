from typing import Dict, List, Tuple


class UnionFind:
    def __init__(self) -> None:
        self.parent: List[int] = []
        self.rank: List[int] = []
        self.history: List[Tuple[int, int, int, int]] = []

    def new_node(self) -> int:
        idx = len(self.parent)
        self.parent.append(idx)
        self.rank.append(0)
        return idx

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            x_root, y_root = y_root, x_root
        self.history.append((y_root, self.parent[y_root], x_root, self.rank[x_root]))
        self.parent[y_root] = x_root
        if self.rank[x_root] == self.rank[y_root]:
            self.rank[x_root] += 1

    def snapshot(self) -> int:
        return len(self.history)

    def rollback(self, snapshot: int) -> None:
        while len(self.history) > snapshot:
            y_root, parent_y, x_root, rank_x = self.history.pop()
            self.parent[y_root] = parent_y
            self.rank[x_root] = rank_x


class TrapGrid:
    def __init__(self, n: int, m: int) -> None:
        self.n = n
        self.m = m
        self.blocked: Dict[Tuple[int, int], int] = {}
        self.uf = UnionFind()
        self.top = self.uf.new_node()
        self.bottom = self.uf.new_node()

    def try_place(self, x: int, y: int) -> bool:
        if (x, y) in self.blocked:
            return True

        snapshot = self.uf.snapshot()
        node = self.uf.new_node()
        self.blocked[(x, y)] = node

        if x == 0:
            self.uf.union(node, self.top)
        if x == self.n - 1:
            self.uf.union(node, self.bottom)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbor = (x + dx, y + dy)
            if neighbor in self.blocked:
                self.uf.union(node, self.blocked[neighbor])

        if self.uf.find(self.top) == self.uf.find(self.bottom):
            self.uf.rollback(snapshot)
            del self.blocked[(x, y)]
            return False

        return True


def solve(lines: List[str]) -> List[str]:
    parts: List[int] = []
    for line in lines:
        for token in line.split():
            parts.append(int(token))
    if len(parts) < 3:
        return []

    n = parts[0]
    m = parts[1]
    t = parts[2]
    output: List[str] = []
    trap_grid = TrapGrid(n, m)
    idx = 3

    for _ in range(t):
        x = parts[idx]
        y = parts[idx + 1]
        idx += 2
        if trap_grid.try_place(x, y):
            output.append("<(_ _)>")
        else:
            output.append(">_<")
    return output


def main() -> None:
    import sys
    lines = [line.rstrip("\n") for line in sys.stdin]
    print("\n".join(solve(lines)))


if __name__ == "__main__":
    main()

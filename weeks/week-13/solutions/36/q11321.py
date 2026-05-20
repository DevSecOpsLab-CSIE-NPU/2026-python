from typing import Dict, List, Tuple


class UnionFind:
    def __init__(self) -> None:
        self.parent: List[int] = []
        self.rank: List[int] = []
        self.history: List[Tuple[int, int, int, int]] = []

    def new_node(self) -> int:
        index = len(self.parent)
        self.parent.append(index)
        self.rank.append(0)
        return index

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

    def rollback(self, snap: int) -> None:
        while len(self.history) > snap:
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
        """嘗試放陷阱，若導致道路封死則回傳 False。"""
        if (x, y) in self.blocked:
            return True

        snap = self.uf.snapshot()
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
            self.uf.rollback(snap)
            del self.blocked[(x, y)]
            return False

        return True


def solve(lines: List[str]) -> List[str]:
    """逐筆讀取陷阱位置並判斷是否可放。"""
    tokens = [int(token) for line in lines for token in line.split()]
    if len(tokens) < 3:
        return []

    n, m, t = tokens[0], tokens[1], tokens[2]
    output: List[str] = []
    trap_grid = TrapGrid(n, m)
    index = 3

    for _ in range(t):
        x = tokens[index]
        y = tokens[index + 1]
        index += 2
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

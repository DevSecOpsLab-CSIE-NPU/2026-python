import sys


class DSU:
    # 這題只需要管理「已經成功放上去的陷阱」之間的連通性。
    def __init__(self) -> None:
        self.parent: list[int] = []
        self.size: list[int] = []
        self.touch_top: list[bool] = []
        self.touch_bottom: list[bool] = []

    def add(self, top: bool, bottom: bool) -> int:
        idx = len(self.parent)
        self.parent.append(idx)
        self.size.append(1)
        self.touch_top.append(top)
        self.touch_bottom.append(bottom)
        return idx

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> int:
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return a
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        self.touch_top[a] = self.touch_top[a] or self.touch_top[b]
        self.touch_bottom[a] = self.touch_bottom[a] or self.touch_bottom[b]
        return a


def main() -> None:
    # 讀入所有整數輸入，格式：n m t, 接著 t 行的放置座標
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, t = data[:3]
    index = 3
    dsu = DSU()
    occupied: dict[tuple[int, int], int] = {}
    output = []

    for _ in range(t):
        x, y = data[index:index + 2]
        index += 2

        neighbors = set()
        touch_top = x == 0
        touch_bottom = x == n - 1

        # 檢查 8 個相鄰方向是否有已放置的陷阱，並合併資訊
        for dx, dy in (
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1),
        ):
            pos = (x + dx, y + dy)
            if pos in occupied:
                root = dsu.find(occupied[pos])
                neighbors.add(root)
                touch_top = touch_top or dsu.touch_top[root]
                touch_bottom = touch_bottom or dsu.touch_bottom[root]

        # 如果這次放下會讓某個連通塊同時接觸最上排與最下排，則拒絕
        if touch_top and touch_bottom:
            output.append(">_<")
            continue

        # 可以放下時，新增節點並與相鄰節點 union
        node = dsu.add(x == 0, x == n - 1)
        occupied[(x, y)] = node
        for root in neighbors:
            node = dsu.union(node, root)

        output.append("<(_ _)>")

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()
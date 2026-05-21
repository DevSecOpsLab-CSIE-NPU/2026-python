import sys

"""
11321 Trap placement

此程式管理使用者逐一放置陷阱的動作，核心概念為：只對實際放下去的陷阱建立 DSU 節點，
每次放置前檢查周邊連通塊是否會造成從上到下的封鎖（touch_top 與 touch_bottom 同時為 True），
若會造成牆則拒絕放置。
"""


class DSU:
    # 只對「真的被放下去的陷阱」建立節點，所以空間只跟 T 有關。
    def __init__(self) -> None:
        self.parent: list[int] = []
        self.size: list[int] = []
        self.touch_top: list[bool] = []
        self.touch_bottom: list[bool] = []

    def add(self, top: bool, bottom: bool) -> int:
        node = len(self.parent)
        self.parent.append(node)
        self.size.append(1)
        self.touch_top.append(top)
        self.touch_bottom.append(bottom)
        return node

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

        neighbor_roots: set[int] = set()
        touch_top = x == 0
        touch_bottom = x == n - 1

        # 障礙物的連通要把斜對角也算進來，這樣才會正確判定是否封死道路。
        for dx, dy in (
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1),
        ):
            neighbor = (x + dx, y + dy)
            if neighbor in occupied:
                root = dsu.find(occupied[neighbor])
                neighbor_roots.add(root)
                touch_top = touch_top or dsu.touch_top[root]
                touch_bottom = touch_bottom or dsu.touch_bottom[root]

        # 如果加上這個陷阱後，障礙物連成了從上到下的牆，就不能放。
        if touch_top and touch_bottom:
            output.append(">_<")
            continue

        node = dsu.add(x == 0, x == n - 1)
        occupied[(x, y)] = node
        for root in neighbor_roots:
            node = dsu.union(node, root)

        output.append("<(_ _)>")

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()
import sys


class DSU:
    def __init__(self, total_size):
        self.parent = list(range(total_size))
        self.size = [1] * total_size
        self.touch_top = [False] * total_size
        self.touch_bottom = [False] * total_size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return root_a

        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        self.touch_top[root_a] = self.touch_top[root_a] or self.touch_top[root_b]
        self.touch_bottom[root_a] = self.touch_bottom[root_a] or self.touch_bottom[root_b]

        return root_a


def solve(data):
    tokens = data.split()

    if not tokens:
        return ""

    index = 0
    n = int(tokens[index])
    m = int(tokens[index + 1])
    t = int(tokens[index + 2])
    index += 3

    total_cells = n * m
    dsu = DSU(total_cells)
    active = [False] * total_cells

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    output = []

    for _ in range(t):
        x = int(tokens[index])
        y = int(tokens[index + 1])
        index += 2

        cell_id = x * m + y
        will_touch_top = (x == n - 1)
        will_touch_bottom = (x == 0)
        neighbor_roots = set()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m:
                neighbor_id = nx * m + ny

                if active[neighbor_id]:
                    root = dsu.find(neighbor_id)
                    neighbor_roots.add(root)

        for root in neighbor_roots:
            will_touch_top = will_touch_top or dsu.touch_top[root]
            will_touch_bottom = will_touch_bottom or dsu.touch_bottom[root]

        if will_touch_top and will_touch_bottom:
            output.append(">_<")
            continue

        output.append("<(_ _)>")
        active[cell_id] = True
        dsu.touch_top[cell_id] = (x == n - 1)
        dsu.touch_bottom[cell_id] = (x == 0)

        for root in neighbor_roots:
            dsu.union(cell_id, root)

    return "\n".join(output)


def main():
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()

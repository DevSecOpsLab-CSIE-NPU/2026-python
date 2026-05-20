import sys


def solve(data):
    values = data.split()

    if not values:
        return ""

    pos = 0

    N = int(values[pos])
    M = int(values[pos + 1])
    T = int(values[pos + 2])
    pos += 3

    total = N * M

    parent = list(range(total))
    size = [1] * total
    touch_top = [False] * total
    touch_bottom = [False] * total
    active = [False] * total

    def find(a):
        if parent[a] != a:
            parent[a] = find(parent[a])
        return parent[a]

    def union(a, b):
        root_a = find(a)
        root_b = find(b)

        if root_a == root_b:
            return root_a

        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a

        parent[root_b] = root_a
        size[root_a] += size[root_b]
        touch_top[root_a] = touch_top[root_a] or touch_top[root_b]
        touch_bottom[root_a] = touch_bottom[root_a] or touch_bottom[root_b]

        return root_a

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    answer = []

    for _ in range(T):
        x = int(values[pos])
        y = int(values[pos + 1])
        pos += 2

        current_id = x * M + y

        new_touch_top = (x == N - 1)
        new_touch_bottom = (x == 0)

        neighbor_roots = set()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < M:
                neighbor_id = nx * M + ny

                if active[neighbor_id]:
                    neighbor_roots.add(find(neighbor_id))

        for root in neighbor_roots:
            new_touch_top = new_touch_top or touch_top[root]
            new_touch_bottom = new_touch_bottom or touch_bottom[root]

        if new_touch_top and new_touch_bottom:
            answer.append(">_<")
            continue

        answer.append("<(_ _)>")

        active[current_id] = True
        touch_top[current_id] = (x == N - 1)
        touch_bottom[current_id] = (x == 0)

        for root in neighbor_roots:
            union(current_id, root)

    return "\n".join(answer)


def main():
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()
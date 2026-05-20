import sys


def solve(data):
    """
    直觀版本解法。

    本題想知道每次放陷阱後，
    是否還存在一條從左邊到右邊的道路。

    重要觀念：
    如果陷阱形成一條從上邊界連到下邊界的牆，
    就會把左邊到右邊的路完全切斷。

    因此我們不用每次重新 BFS 找路，
    而是維護陷阱的連通狀態。

    因為人只能上下左右走，
    所以陷阱只要斜角相連，也可能造成阻隔。
    所以陷阱連通要看 8 方向。
    """

    values = data.split()

    if not values:
        return ""

    pos = 0

    # 讀取 N、M、T。
    # N 是高度，也就是 x 方向格子數。
    # M 是寬度，也就是 y 方向格子數。
    # T 是接下來要嘗試放的陷阱數量。
    N = int(values[pos])
    M = int(values[pos + 1])
    T = int(values[pos + 2])
    pos += 3

    total = N * M

    # parent[i] 表示 i 這個格子在 DSU 中的父節點。
    parent = list(range(total))

    # size[i] 表示以 i 為 root 的集合大小。
    # 用來讓小集合接到大集合上，提升效率。
    size = [1] * total

    # touch_top[i] 表示以 i 為 root 的陷阱區塊是否碰到上邊界。
    touch_top = [False] * total

    # touch_bottom[i] 表示以 i 為 root 的陷阱區塊是否碰到下邊界。
    touch_bottom = [False] * total

    # active[i] 表示 i 這個格子是否已經成功放上陷阱。
    active = [False] * total

    def find(a):
        """
        找出 a 所在集合的 root。

        使用路徑壓縮，讓之後查詢更快。
        """

        if parent[a] != a:
            parent[a] = find(parent[a])

        return parent[a]

    def union(a, b):
        """
        合併 a 與 b 所在的陷阱連通區塊。

        合併時也要合併：
        - 是否碰到上邊界
        - 是否碰到下邊界
        """

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

    # 陷阱連通要看 8 方向。
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

        # 將二維座標轉成一維 id。
        current_id = x * M + y

        # 先判斷新陷阱本身是否碰到上下邊界。
        # x = N - 1 是上邊界。
        # x = 0 是下邊界。
        new_touch_top = (x == N - 1)
        new_touch_bottom = (x == 0)

        # neighbor_roots 用來存放周圍已存在陷阱的連通區塊 root。
        # 用 set 是為了避免同一個區塊被重複計算。
        neighbor_roots = set()

        # 檢查 8 個方向。
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            # 先確認鄰居座標沒有超出地圖。
            if 0 <= nx < N and 0 <= ny < M:
                neighbor_id = nx * M + ny

                # 如果鄰居已經是陷阱，就取得它的 root。
                if active[neighbor_id]:
                    root = find(neighbor_id)
                    neighbor_roots.add(root)

        # 模擬把新陷阱和周圍陷阱合併後，
        # 這個新區塊是否會碰到上下邊界。
        for root in neighbor_roots:
            if touch_top[root]:
                new_touch_top = True

            if touch_bottom[root]:
                new_touch_bottom = True

        # 如果合併後同時碰到上邊界和下邊界，
        # 代表陷阱牆已經把道路封死。
        # 所以這個陷阱不能放。
        if new_touch_top and new_touch_bottom:
            answer.append(">_<")
            continue

        # 否則可以放陷阱。
        answer.append("<(_ _)>")

        # 標記目前格子已放陷阱。
        active[current_id] = True

        # 設定目前新陷阱自己的邊界資訊。
        touch_top[current_id] = (x == N - 1)
        touch_bottom[current_id] = (x == 0)

        # 真的把它和周圍陷阱合併。
        for root in neighbor_roots:
            union(current_id, root)

    return "\n".join(answer)


def main():
    """
    從標準輸入讀取資料並輸出答案。
    """

    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()
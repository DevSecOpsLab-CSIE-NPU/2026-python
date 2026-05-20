import sys


class DSU:
    """
    Disjoint Set Union，中文常稱為「並查集」。

    本題用 DSU 來維護目前已放置的陷阱連通區塊。

    每一個陷阱格子都是一個節點。
    如果兩個陷阱在 8 方向上相鄰，就把它們合併成同一個連通區塊。

    除了 parent 與 size 之外，本題還需要額外記錄：
    1. touch_top：該陷阱連通區塊是否碰到上邊界
    2. touch_bottom：該陷阱連通區塊是否碰到下邊界

    如果某個陷阱連通區塊同時碰到上邊界與下邊界，
    就代表陷阱形成上下阻隔牆，左到右道路會被封死。
    """

    def __init__(self, total_size):
        """
        初始化 DSU。

        total_size 是整張地圖的格子數，也就是 N * M。
        """

        self.parent = list(range(total_size))
        self.size = [1] * total_size
        self.touch_top = [False] * total_size
        self.touch_bottom = [False] * total_size

    def find(self, x):
        """
        找出 x 所在集合的代表節點 root。

        使用路徑壓縮：
        在查找 root 的同時，將路徑上的節點直接接到 root，
        讓之後查詢更快。
        """

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, a, b):
        """
        將 a 與 b 所在的兩個集合合併。

        合併時也要合併 touch_top 與 touch_bottom 狀態。
        """

        root_a = self.find(a)
        root_b = self.find(b)

        # 如果已經在同一個集合，就不需要再合併。
        if root_a == root_b:
            return root_a

        # 使用 union by size：
        # 讓小集合接到大集合下面，降低樹高度。
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]

        # 合併兩個陷阱區塊是否碰到上下邊界的資訊。
        self.touch_top[root_a] = self.touch_top[root_a] or self.touch_top[root_b]
        self.touch_bottom[root_a] = self.touch_bottom[root_a] or self.touch_bottom[root_b]

        return root_a


def solve(data):
    """
    處理完整輸入資料，並回傳完整輸出字串。

    核心想法：
    每次嘗試放陷阱時，先判斷它是否會讓陷阱形成
    從上邊界到下邊界的連通牆。

    如果會形成上下牆，表示左到右道路被封死，不能放。
    如果不會形成上下牆，才真的把陷阱放進 DSU。
    """

    tokens = data.split()

    if not tokens:
        return ""

    index = 0

    # 讀取柏油路大小與嘗試放陷阱的數量。
    n = int(tokens[index])
    m = int(tokens[index + 1])
    t = int(tokens[index + 2])
    index += 3

    total_cells = n * m

    # 初始化 DSU。
    dsu = DSU(total_cells)

    # active[id] 表示該格子是否已經成功放上陷阱。
    active = [False] * total_cells

    # 8 方向，用來判斷陷阱之間是否連通。
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

        # 先假設這個新陷阱本身是否碰到上下邊界。
        # x = n - 1 是上邊界。
        # x = 0 是下邊界。
        will_touch_top = (x == n - 1)
        will_touch_bottom = (x == 0)

        # 收集周圍已存在陷阱的 root。
        # 使用 set 避免同一個連通區塊重複計算。
        neighbor_roots = set()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            # 確認鄰居座標在地圖範圍內。
            if 0 <= nx < n and 0 <= ny < m:
                neighbor_id = nx * m + ny

                # 只有已經成功放置的陷阱才需要考慮。
                if active[neighbor_id]:
                    root = dsu.find(neighbor_id)
                    neighbor_roots.add(root)

        # 先把周圍陷阱連通區塊的上下邊界資訊合併起來，
        # 用來判斷如果放下新陷阱後是否會封死道路。
        for root in neighbor_roots:
            will_touch_top = will_touch_top or dsu.touch_top[root]
            will_touch_bottom = will_touch_bottom or dsu.touch_bottom[root]

        # 如果新陷阱與周圍陷阱合併後，
        # 會同時碰到上邊界與下邊界，
        # 表示陷阱形成上下阻隔牆，會封死左到右道路。
        if will_touch_top and will_touch_bottom:
            output.append(">_<")
            continue

        # 如果不會封死道路，就可以放陷阱。
        output.append("<(_ _)>")

        # 啟用該格子。
        active[cell_id] = True

        # 初始化該陷阱本身的上下邊界狀態。
        dsu.touch_top[cell_id] = (x == n - 1)
        dsu.touch_bottom[cell_id] = (x == 0)

        # 將新陷阱與周圍已存在的陷阱合併。
        for root in neighbor_roots:
            dsu.union(cell_id, root)

    return "\n".join(output)


def main():
    """
    主程式進入點。
    """

    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()
import sys


class FenwickTree:
    def __init__(self, size):
        # 用樹狀陣列記錄目前「遞減函數」的數量。
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, index, delta):
        # 單點加值：把某一個函數的狀態改變後，順便更新相關區間。
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def prefix_sum(self, index):
        # 算前綴和：前面有幾個函數是遞減。
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total


def solve():
    # 這題最容易記的方法：
    # 把每個函數看成 0 或 1。
    # 0 = 遞增，1 = 遞減。
    # 區間內遞減函數的個數如果是奇數，整體就是遞減；偶數則是遞增。
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    q = data[1]
    index = 2

    # state[i] = 0 表示第 i 個函數目前是遞增，1 表示遞減。
    state = [0] * (n + 1)
    bit = FenwickTree(n)
    output = []

    for _ in range(q):
        kind = data[index]
        index += 1

        if kind == 1:
            # 翻轉某一個函數的性質。
            pos = data[index]
            index += 1

            if state[pos] == 0:
                state[pos] = 1
                bit.add(pos, 1)
            else:
                state[pos] = 0
                bit.add(pos, -1)
        else:
            # 查詢區間 [l, r] 的單調性。
            l = data[index]
            r = data[index + 1]
            index += 2

            # 先算出區間內有幾個遞減函數，再看奇偶性。
            minus_count = bit.prefix_sum(r) - bit.prefix_sum(l - 1)
            output.append(str(minus_count % 2))

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()
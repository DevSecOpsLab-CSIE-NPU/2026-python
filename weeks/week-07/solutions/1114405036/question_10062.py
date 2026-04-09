# 題目 10062: 乳牛排序問題
# 給定每頭乳牛前面比它編號小的乳牛數量，重建正確的排列順序。
# 使用 Fenwick Tree 來高效處理查詢和更新。

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

    def find_kth(self, k):
        # 找到第 k 小的位置（1-based）
        low, high = 1, self.size
        while low < high:
            mid = (low + high) // 2
            if self.query(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low

def reconstruct_cow_order(N, counts):
    # counts 是 list of int, len(counts) = N-1, counts[0] 是位置2的count, counts[N-2] 是位置N的count
    ft = FenwickTree(N)
    for i in range(1, N+1):
        ft.update(i, 1)  # 初始所有編號可用

    order = [0] * N

    # 從最後位置開始
    for i in range(N-1, 0, -1):  # i from N-1 down to 1
        count = counts[i-1]
        k = count + 1
        num = ft.find_kth(k)
        order[i] = num  # position i+1 (1-based) is order[i]
        ft.update(num, -1)

    # 位置1 是剩下的
    for i in range(1, N+1):
        if ft.query(i) - ft.query(i-1) == 1:
            order[0] = i
            break

    return order

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    counts = list(map(int, data[1:]))
    order = reconstruct_cow_order(N, counts)
    for num in order:
        print(num)
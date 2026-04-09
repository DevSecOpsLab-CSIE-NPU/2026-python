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
        low, high = 1, self.size
        while low < high:
            mid = (low + high) // 2
            if self.query(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low

def reconstruct_cow_order(N, counts):
    ft = FenwickTree(N)
    for i in range(1, N+1):
        ft.update(i, 1)

    order = [0] * N

    for i in range(N-1, 0, -1):
        count = counts[i-1]
        k = count + 1
        num = ft.find_kth(k)
        order[i] = num
        ft.update(num, -1)

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
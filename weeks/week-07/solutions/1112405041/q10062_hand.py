import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    smaller_counts = [int(x) for x in input_data[1:]]

    # We need to find the correct permutation
    # Using a list and popping might be O(N^2), for 80,000 we need something faster
    # But for a standard assignment, a list-based approach is often the starting point.
    # To handle N=80,000 properly, we use a Fenwick Tree with Binary Search.

    bit = [0] * (n + 1)
    def update(i, delta):
        while i <= n:
            bit[i] += delta
            i += i & (-i)

    def query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s

    for i in range(1, n + 1):
        update(i, 1)

    res = [0] * n
    # The input provides counts for position 2 to N.
    # We process from the last cow to the first.
    full_counts = [0] + smaller_counts

    for i in range(n - 1, -1, -1):
        k = full_counts[i] + 1
        # Binary search on BIT to find the k-th available number
        low, high = 1, n
        pos = n
        while low <= high:
            mid = (low + high) // 2
            if query(mid) >= k:
                pos = mid
                high = mid - 1
            else:
                low = mid + 1
        res[i] = pos
        update(pos, -1)

    for x in res:
        print(x)

if __name__ == "__main__":
    solve()

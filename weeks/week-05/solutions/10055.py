class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self.build(arr, 2*node, start, mid)
        self.build(arr, 2*node+1, mid+1, end)
        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]

    def update_range(self, node, start, end, l, r):
        if self.lazy[node] != 0:
            self.tree[node] = (end - start + 1) - self.tree[node]
            if start != end:
                self.lazy[2*node] ^= 1
                self.lazy[2*node+1] ^= 1
            self.lazy[node] = 0
        if start > end or start > r or end < l:
            return
        if l <= start and end <= r:
            self.tree[node] = (end - start + 1) - self.tree[node]
            if start != end:
                self.lazy[2*node] ^= 1
                self.lazy[2*node+1] ^= 1
            return
        mid = (start + end) // 2
        self.update_range(2*node, start, mid, l, r)
        self.update_range(2*node+1, mid+1, end, l, r)
        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]

    def query_range(self, node, start, end, l, r):
        if self.lazy[node] != 0:
            self.tree[node] = (end - start + 1) - self.tree[node]
            if start != end:
                self.lazy[2*node] ^= 1
                self.lazy[2*node+1] ^= 1
            self.lazy[node] = 0
        if start > end or start > r or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query_range(2*node, start, mid, l, r)
        p2 = self.query_range(2*node+1, mid+1, end, l, r)
        return p1 + p2

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0
    N = int(data[index])
    index += 1
    Q = int(data[index])
    index += 1
    funcs = [0] * (N + 1)
    st = SegmentTree(N + 1)
    st.build(funcs, 1, 1, N)
    results = []
    for _ in range(Q):
        v = int(data[index])
        index += 1
        if v == 1:
            i = int(data[index])
            index += 1
            st.update_range(1, 1, N, i, i)
        else:
            L = int(data[index])
            index += 1
            R = int(data[index])
            index += 1
            dec_count = st.query_range(1, 1, N, L, R)
            is_dec = dec_count % 2
            results.append(str(is_dec))
    print('\n'.join(results))

if __name__ == "__main__":
    main()
def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    q = int(next(it))
    arr = [0] * (n + 1)
    seg = [0] * (4 * n)
    def build(node, l, r):
        if l == r:
            seg[node] = arr[l]
        else:
            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            seg[node] = seg[node * 2] ^ seg[node * 2 + 1]
    def update(node, l, r, idx, val):
        if l == r:
            seg[node] = val
        else:
            mid = (l + r) // 2
            if idx <= mid:
                update(node * 2, l, mid, idx, val)
            else:
                update(node * 2 + 1, mid + 1, r, idx, val)
            seg[node] = seg[node * 2] ^ seg[node * 2 + 1]
    def query(node, l, r, ql, qr):
        if ql > r or qr < l:
            return 0
        if ql <= l and r <= qr:
            return seg[node]
        mid = (l + r) // 2
        return query(node * 2, l, mid, ql, qr) ^ query(node * 2 + 1, mid + 1, r, ql, qr)
    build(1, 1, n)
    results = []
    for _ in range(q):
        v = int(next(it))
        if v == 1:
            i = int(next(it))
            arr[i] ^= 1
            update(1, 1, n, i, arr[i])
        else:
            l = int(next(it))
            r = int(next(it))
            res = query(1, 1, n, l, r)
            results.append(str(res))
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()
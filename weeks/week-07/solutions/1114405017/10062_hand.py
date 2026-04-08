import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    n = int(input_data[0])
    pre_smaller = [0] + [int(x) for x in input_data[1:]]
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
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        target_rank = pre_smaller[i] + 1
        low, high = 1, n
        pos = n
        while low <= high:
            mid = (low + high) // 2
            if query(mid) >= target_rank:
                pos = mid
                high = mid - 1
            else:
                low = mid + 1
        ans[i] = pos
        update(pos, -1)
    sys.stdout.write('\n'.join(map(str, ans)) + '\n')
if __name__ == '__main__':
    solve()
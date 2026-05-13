import sys
def solve():
    data = sys.stdin.read().split()
    if not data: return
    it = iter(data)
    try:
        for _ in range(int(next(it))):
            s, d = int(next(it)), int(next(it))
            if s >= d and (s + d) % 2 == 0:
                print((s + d) // 2, (s - d) // 2)
            else:
                print("impossible")
    except StopIteration: pass
if __name__ == "__main__":
    solve()

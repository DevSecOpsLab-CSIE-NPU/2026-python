import sys
from collections import Counter
def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data: return
    n, s = data[0], data[1:]
    lhs_counts = Counter(a + b + c for a in s for b in s for c in s)
    ans = sum(lhs_counts[f - d - e] for f in s for d in s for e in s)
    print(ans)
if __name__ == "__main__":
    solve()
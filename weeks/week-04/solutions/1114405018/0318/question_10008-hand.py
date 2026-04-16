import sys
from collections import Counter

n = int(sys.stdin.readline())
cnt = Counter()

for _ in range(n):
    for ch in sys.stdin.readline():
        if ch.isalpha():
            cnt[ch.upper()] += 1

for ch, c in sorted(cnt.items(), key=lambda x: (-x[1], x[0])):
    print(ch, c)
    
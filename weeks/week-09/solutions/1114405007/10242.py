import sys
from collections import deque

input = sys.stdin.buffer.readline

n, m = map(int, input().split())

# g 是原圖，rg 是反向圖，做 SCC 會用到。
g = [[] for _ in range(n + 1)]
rg = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    rg[b].append(a)

money = [0] * (n + 1)
for i in range(1, n + 1):
    money[i] = int(input())

s, p = map(int, input().split())
bars = []
while len(bars) < p:
    bars += list(map(int, input().split()))

is_bar = [0] * (n + 1)
for x in bars:
    is_bar[x] = 1

vis = [0] * (n + 1)
order = []

# 第一次 DFS：拿到拓樸後序。
for st in range(1, n + 1):
    if vis[st]:
        continue
    stack = [(st, 0)]
    vis[st] = 1
    while stack:
        x, i = stack[-1]
        if i < len(g[x]):
            y = g[x][i]
            stack[-1] = (x, i + 1)
            if not vis[y]:
                vis[y] = 1
                stack.append((y, 0))
        else:
            order.append(x)
            stack.pop()

cid = [-1] * (n + 1)
cmoney = []
cbar = []
cnt = 0

# 第二次 DFS：在反向圖上找 SCC，順便把同一個 SCC 的金額加總。
for st in reversed(order):
    if cid[st] != -1:
        continue
    stack = [st]
    cid[st] = cnt
    total = 0
    has_bar = 0
    while stack:
        x = stack.pop()
        total += money[x]
        has_bar |= is_bar[x]
        for y in rg[x]:
            if cid[y] == -1:
                cid[y] = cnt
                stack.append(y)
    cmoney.append(total)
    cbar.append(has_bar)
    cnt += 1

# 縮點後形成 DAG。
dag = [set() for _ in range(cnt)]
for x in range(1, n + 1):
    a = cid[x]
    for y in g[x]:
        b = cid[y]
        if a != b:
            dag[a].add(b)

start = cid[s]
can = [0] * cnt
stack = [start]
can[start] = 1

# 只保留從起點真的走得到的 SCC。
while stack:
    x = stack.pop()
    for y in dag[x]:
        if not can[y]:
            can[y] = 1
            stack.append(y)

deg = [0] * cnt
for x in range(cnt):
    if not can[x]:
        continue
    for y in dag[x]:
        if can[y]:
            deg[y] += 1

q = deque()
for i in range(cnt):
    if can[i] and deg[i] == 0:
        q.append(i)

dp = [-1] * cnt
dp[start] = cmoney[start]
ans = 0

# 在 DAG 上做最長路 DP。
while q:
    x = q.popleft()
    if cbar[x] and dp[x] > ans:
        ans = dp[x]
    for y in dag[x]:
        if can[y] and dp[x] != -1:
            dp[y] = max(dp[y], dp[x] + cmoney[y])
        if can[y]:
            deg[y] -= 1
            if deg[y] == 0:
                q.append(y)

print(ans)
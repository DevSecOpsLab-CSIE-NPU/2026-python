# 手打程式：手動實現拓撲排序 DP，加上繁體中文註解

from collections import defaultdict, deque

# 讀取輸入

with open('test_input_10242.txt', 'r') as f:

    data = f.read().split()

index = 0

N = int(data[index])

M = int(data[index+1])

index +=2

# 建圖

graph = defaultdict(list)

for _ in range(M):

    u = int(data[index]) -1

    v = int(data[index+1]) -1

    index +=2

    graph[u].append(v)

# 讀取 ATM 金額

money = []

for _ in range(N):

    money.append(int(data[index]))

    index +=1

# 起始點和酒吧

S = int(data[index]) -1

P = int(data[index+1])

index +=2

pubs = []

for _ in range(P):

    pubs.append(int(data[index]) -1)

    index +=1

# 計算入度

indegree = [0] * N

for u in graph:

    for v in graph[u]:

        indegree[v] +=1

# 拓撲排序隊列

queue = deque([i for i in range(N) if indegree[i] == 0])

# DP 陣列

dp = [-float('inf')] * N

dp[S] = money[S]

# 處理隊列

while queue:

    u = queue.popleft()

    for v in graph[u]:

        dp[v] = max(dp[v], dp[u] + money[v])

        indegree[v] -=1

        if indegree[v] == 0:

            queue.append(v)

# 找出最大金額

max_money = max(dp[p] for p in pubs if dp[p] != -float('inf'))

# 輸出到記錄

with open('10242-manual_test.log', 'w') as log:

    log.write(str(max_money) + '\n')
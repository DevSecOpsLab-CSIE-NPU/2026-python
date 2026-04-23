# 簡單版本：使用相同的 DP 方法

from collections import defaultdict, deque

with open('test_input_10242.txt', 'r') as f:

    data = f.read().split()

index = 0

N = int(data[index])

M = int(data[index+1])

index +=2

graph = defaultdict(list)

for _ in range(M):

    u = int(data[index]) -1

    v = int(data[index+1]) -1

    index +=2

    graph[u].append(v)

money = []

for _ in range(N):

    money.append(int(data[index]))

    index +=1

S = int(data[index]) -1

P = int(data[index+1])

index +=2

pubs = []

for _ in range(P):

    pubs.append(int(data[index]) -1)

    index +=1

indegree = [0] * N

for u in graph:

    for v in graph[u]:

        indegree[v] +=1

queue = deque([i for i in range(N) if indegree[i] == 0])

dp = [-float('inf')] * N

dp[S] = money[S]

while queue:

    u = queue.popleft()

    for v in graph[u]:

        dp[v] = max(dp[v], dp[u] + money[v])

        indegree[v] -=1

        if indegree[v] == 0:

            queue.append(v)

max_money = max(dp[p] for p in pubs if dp[p] != -float('inf'))

with open('10242-easy_test.log', 'w') as log:

    log.write(str(max_money) + '\n')
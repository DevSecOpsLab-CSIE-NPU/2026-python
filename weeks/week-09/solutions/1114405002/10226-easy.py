# 簡單版本：使用簡單的遞歸來嘗試生成排列

import itertools

# 讀取輸入檔案

with open('test_input_10226.txt', 'r') as f:

    data = f.read().split()

index = 0

N = int(data[index])

index +=1

forbidden = []

for i in range(N):

    f = set()

    while True:

        pos = int(data[index])

        index +=1

        if pos == 0:

            break

        f.add(pos)

    forbidden.append(f)

# 使用 itertools 生成所有排列，然後過濾

perms = []

for perm in itertools.permutations(range(N)):

    valid = True

    for p in range(N):

        if p+1 in forbidden[perm[p]]:

            valid = False

            break

    if valid:

        perms.append(perm)

# 輸出到 log

with open('10226-easy_test.log', 'w') as log:

    prev = None

    for perm in perms:

        s = ''.join(chr(ord('A') + p) for p in perm)

        if prev is None:

            log.write(s + '\n')

            prev = s

            continue

        i = 0

        while i < len(s) and i < len(prev) and s[i] == prev[i]:

            i += 1

        if i < len(s):

            log.write(s[i:] + '\n')

            prev = s
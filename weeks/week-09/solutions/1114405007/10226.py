import sys


out = []

while True:
    # 讀到 EOF 就結束，題目有多筆測資。
    line = sys.stdin.readline()
    if not line:
        break
    line = line.strip()
    if not line:
        continue

    n = int(line)
    # bad[i] 記錄第 i 個人不能站哪些位置。
    bad = [set() for _ in range(n)]
    for i in range(n):
        a = list(map(int, sys.stdin.readline().split()))
        bad[i] = set(a[:-1])

    # used 表示某個人是否已經放進排列。
    used = [0] * n
    path = [""] * n
    # prev 記住上一個完整排列，輸出時只印和上一筆不同的尾端。
    prev = [""]
    ans = []

    def dfs(pos):
        if pos == n:
            s = "".join(path)
            i = 0
            while i < len(prev[0]) and prev[0][i] == s[i]:
                i += 1
            ans.append(s[i:])
            prev[0] = s
            return

        for i in range(n):
            if used[i]:
                continue
            if pos + 1 in bad[i]:
                continue
            used[i] = 1
            path[pos] = chr(65 + i)
            dfs(pos + 1)
            used[i] = 0

    dfs(0)
    out.append("\n".join(ans))

sys.stdout.write("\n\n".join(out))
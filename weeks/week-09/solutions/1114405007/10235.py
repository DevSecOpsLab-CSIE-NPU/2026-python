import sys

MOD = 1000000007

t = int(sys.stdin.readline())
out = []

for tc in range(1, t + 1):
    n, m = map(int, sys.stdin.readline().split())
    g = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # 把欄數壓到比較小，狀態數會少很多。
    if m > n:
        g = [list(x) for x in zip(*g)]
        n, m = m, n

    # mask 記錄上一列往下延伸到目前這列的連線狀態。
    dp = {0: 1}

    for r in range(n):
        ndp = {}

        for mask, ways in dp.items():
            def dfs(c, left, nmask):
                if c == m:
                    if left == 0:
                        ndp[nmask] = (ndp.get(nmask, 0) + ways) % MOD
                    return

                # up 是上方是否有一條邊連到這格。
                up = (mask >> c) & 1

                # 0 代表插座，不能被蛇佔據。
                if g[r][c] == 0:
                    if up == 0 and left == 0:
                        dfs(c + 1, 0, nmask)
                    return

                # 每個可用格都必須剛好有 2 條邊，形成環。
                need = 2 - up - left

                if need == 0:
                    dfs(c + 1, 0, nmask)
                elif need == 1:
                    if c + 1 < m:
                        dfs(c + 1, 1, nmask)
                    if r + 1 < n:
                        dfs(c + 1, 0, nmask | (1 << c))
                else:
                    if c + 1 < m and r + 1 < n:
                        dfs(c + 1, 1, nmask | (1 << c))

            dfs(0, 0, 0)

        dp = ndp

    out.append(f"Case {tc}: {dp.get(0, 0)}")

sys.stdout.write("\n".join(out))
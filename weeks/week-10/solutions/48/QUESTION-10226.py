import sys

sys.setrecursionlimit(10000)

# 產生符合限制的排列（字典序），並即時輸出壓縮形式

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    out_lines = []

    while True:
        try:
            n = int(next(it))
        except StopIteration:
            break
        if n == 0:
            break
        forbidden = [set() for _ in range(n)]
        for i in range(n):
            while True:
                v = int(next(it))
                if v == 0:
                    break
                forbidden[i].add(v - 1)

        # 優化點：用 used / cur 原地回溯，避免建立大量中間排列物件。
        used = [False] * n
        cur = [0] * n
        prev = None

        def dfs(pos):
            nonlocal prev
            if pos == n:
                s = "".join(chr(ord("A") + x) for x in cur)
                # compressed print compared to prev
                if prev is None:
                    out_lines.append(s)
                else:
                    i = 0
                    L = min(len(s), len(prev))
                    while i < L and s[i] == prev[i]:
                        i += 1
                    out_lines.append(s[i:])
                prev = s
                return
            for person in range(n):
                if used[person]:
                    continue
                if pos in forbidden[person]:
                    continue
                used[person] = True
                cur[pos] = person
                dfs(pos + 1)
                used[person] = False

        dfs(0)
        out_lines.append("")  # 分隔不同測資

    # 移除尾端多餘空行
    if out_lines and out_lines[-1] == "":
        out_lines.pop()
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()

"""
帶註解的版本（示範用）：此檔展示解題思路並可直接執行。
演算法：回溯生成排列，遇到不可站的位置就跳過；輸出使用與前一列比較的壓縮表示。
"""
import sys

sys.setrecursionlimit(10000)

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
        # forbidden[i] = set of 0-based positions person i cannot occupy
        forbidden = [set() for _ in range(n)]
        for i in range(n):
            while True:
                v = int(next(it))
                if v == 0:
                    break
                forbidden[i].add(v - 1)

        used = [False] * n
        cur = [0] * n
        prev = None

        def dfs(pos):
            nonlocal prev
            if pos == n:
                s = "".join(chr(ord("A") + x) for x in cur)
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
        out_lines.append("")

    if out_lines and out_lines[-1] == "":
        out_lines.pop()
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()

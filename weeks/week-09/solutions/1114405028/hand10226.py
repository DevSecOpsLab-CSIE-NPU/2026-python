# 手打版本
# 這是純手動寫的 10226 解法，使用回溯並處理輸出差異。

def solve() -> None:
    import sys

    data = sys.stdin.read().split()
    if not data:
        return

    it = iter(data)
    out = []

    while True:
        try:
            n = int(next(it))
        except StopIteration:
            break

        forbidden = []
        for _ in range(n):
            row = []
            while True:
                x = int(next(it))
                if x == 0:
                    break
                row.append(x - 1)
            forbidden.append(set(row))

        prev = ""

        def dfs(idx, used, current):
            nonlocal prev
            if idx == n:
                s = "".join(chr(ord('A') + x) for x in current)
                if prev == "":
                    out.append(s)
                else:
                    i = 0
                    while i < len(s) and i < len(prev) and s[i] == prev[i]:
                        i += 1
                    out.append(s[i:])
                prev = s
                return

            for person in range(n):
                if (used >> person) & 1:
                    continue
                if idx in forbidden[person]:
                    continue
                current.append(person)
                dfs(idx + 1, used | (1 << person), current)
                current.pop()

        if n > 0:
            dfs(0, 0, [])
        out.append("")

    if out and out[-1] == "":
        out.pop()

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


if __name__ == '__main__':
    solve()

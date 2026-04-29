def solve_10226_easy():
    import sys
    lines = sys.stdin.read().split()
    if not lines: return
    idx = 0
    out = []
    while idx < len(lines):
        n = int(lines[idx]); idx += 1
        dislikes = [set() for _ in range(n)]
        for i in range(n):
            while idx < len(lines):
                val = int(lines[idx]); idx += 1
                if val == 0: break
                dislikes[i].add(val - 1)
        prev_arr = []
        used = [False] * n
        curr_arr = []
        def dfs(depth):
            nonlocal prev_arr
            if depth == n:
                diff_idx = 0
                while diff_idx < n and prev_arr and prev_arr[diff_idx] == curr_arr[diff_idx]:
                    diff_idx += 1
                out.append("".join(chr(c + 65) for c in curr_arr[diff_idx:]))
                prev_arr = list(curr_arr)
                return
            for i in range(n):
                if not used[i] and depth not in dislikes[i]:
                    used[i] = True
                    curr_arr.append(i)
                    dfs(depth + 1)
                    curr_arr.pop()
                    used[i] = False
        dfs(0)
        out.append("")
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    solve_10226_easy()
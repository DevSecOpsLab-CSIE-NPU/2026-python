import sys
def run():
    lines = sys.stdin.read().split()
    if not lines: return
    idx = 0
    m = int(lines[idx]); idx += 1
    for t in range(m):
        n = int(lines[idx]); k = int(lines[idx+1]); idx += 2
        possible = [True] * (n + 1)
        for _ in range(k):
            p = int(lines[idx]); idx += 1
            scale = [int(lines[idx + i]) for i in range(2 * p)]
            idx += 2 * p
            res = lines[idx]; idx += 1
            if res == '=':
                for c in scale: possible[c] = False
            else:
                s_set = set(scale)
                for i in range(1, n + 1):
                    if i not in s_set: possible[i] = False
        ans = [i for i in range(1, n+1) if possible[i]]
        print(ans[0] if len(ans) == 1 else 0)
        if t < m - 1: print()
if __name__ == "__main__":
    run()
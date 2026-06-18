import sys
def solve():
    lines = sys.stdin.readlines()
    if not lines: return
    tc = int(lines[0].strip())
    cur = 1
    for t in range(1, tc + 1):
        while cur < len(lines) and not lines[cur].strip(): cur += 1
        n = int(lines[cur].split('=')[-1].strip())
        cur += 1
        mat = []
        for _ in range(n):
            mat.append(list(map(int, lines[cur].split())))
            cur += 1
        sym = True
        for r in range(n):
            for c in range(n):
                if mat[r][c] < 0 or mat[r][c] != mat[n-1-r][n-1-c]:
                    sym = False; break
            if not sym: break
        print(f"Test #{t}: {'Symmetric' if sym else 'Non-symmetric'}.")
if __name__ == '__main__': solve()

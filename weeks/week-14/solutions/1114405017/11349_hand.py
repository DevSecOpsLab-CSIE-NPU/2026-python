import sys
def solve():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    t = int(data[0].strip())
    idx = 1
    out_lines = []
    for case in range(1, t + 1):
        while idx < len(data) and data[idx].strip() == "":
            idx += 1
        head = data[idx].strip()
        idx += 1
        if '=' in head:
            n = int(head.split('=')[1].strip())
        else:
            n = int(head)
        mat = []
        for _ in range(n):
            row = list(map(int, data[idx].split()))
            idx += 1
            mat.append(row)
        sym = True
        for i in range(n):
            for j in range(n):
                if mat[i][j] < 0 or mat[i][j] != mat[n - 1 - i][n - 1 - j]:
                    sym = False
                    break
            if not sym:
                break
        if sym:
            out_lines.append(f"Test #{case}: Symmetric.")
        else:
            out_lines.append(f"Test #{case}: Non-symmetric.")
    sys.stdout.write('\n'.join(out_lines))
if __name__ == '__main__':
    solve()
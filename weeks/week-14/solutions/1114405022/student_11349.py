"""
手打版本（示範）：UVA 11349 — Symmetric Matrix

此檔為學生手寫版本的示範（保留較少註解，模擬手打習作）。
"""

def is_center_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 0:
                return False
            if matrix[i][j] != matrix[n-1-i][n-1-j]:
                return False
    return True


def solve():
    import sys
    lines = [l.strip() for l in sys.stdin if l.strip()]
    if not lines:
        return
    t = int(lines[0])
    idx = 1
    k = 1
    res = []
    while k <= t and idx < len(lines):
        header = lines[idx]; idx += 1
        if '=' in header:
            n = int(header.split('=')[1].strip())
        else:
            n = int(header)
        mat = []
        for _ in range(n):
            mat.append(list(map(int, lines[idx].split()))); idx += 1
        if is_center_symmetric(mat):
            res.append(f"Test #{k}: Symmetric.")
        else:
            res.append(f"Test #{k}: Non-symmetric.")
        k += 1
    print('\n'.join(res))


if __name__ == '__main__':
    solve()

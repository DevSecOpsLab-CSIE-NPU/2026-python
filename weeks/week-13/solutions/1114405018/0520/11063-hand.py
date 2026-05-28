import sys

def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    vals = data[1:]
    expect = 3 * n * n
    vals = vals[:expect]

    out_lines = []
    ys = []
    for i in range(0, len(vals), 3):
        r, g, b = vals[i], vals[i+1], vals[i+2]
        x = 0.5149 * r + 0.3244 * g + 0.1607 * b
        y = 0.2654 * r + 0.6704 * g + 0.0642 * b
        z = 0.0248 * r + 0.1248 * g + 0.8504 * b
        ys.append(y)
        out_lines.append(f"{x:.4f} {y:.4f} {z:.4f}")

    avg_y = sum(ys) / len(ys) if ys else 0.0
    out_lines.append(f"The average of Y is {avg_y:.4f}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == '__main__':
    solve()
    
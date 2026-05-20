import sys

def rgb_to_xyz(r, g, b):
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    return x, y, z


def solve(text):
    arr = text.split()
    p = 0

    n = int(arr[p])
    p += 1

    lines = []
    y_sum = 0.0

    for _ in range(n * n):
        r = int(arr[p])
        g = int(arr[p + 1])
        b = int(arr[p + 2])
        p += 3

        x, y, z = rgb_to_xyz(r, g, b)
        y_sum += y

        lines.append(f"{x:.4f} {y:.4f} {z:.4f}")

    y_avg = y_sum / (n * n)
    lines.append(f"The average of Y is {y_avg:.4f}")

    return "\n".join(lines)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

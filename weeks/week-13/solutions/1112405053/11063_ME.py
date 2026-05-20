import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n = data[0]
    vals = data[1:]

    total_pixels = len(vals) // 3

    a = (0.5149, 0.3244, 0.1607)
    b = (0.2654, 0.6704, 0.0642)
    c = (0.0248, 0.1248, 0.8504)

    out_lines = []
    sum_Y = 0.0

    for i in range(total_pixels):
        R = vals[3 * i]
        G = vals[3 * i + 1]
        B = vals[3 * i + 2]

        X = a[0] * R + a[1] * G + a[2] * B
        Y = b[0] * R + b[1] * G + b[2] * B
        Z = c[0] * R + c[1] * G + c[2] * B

        sum_Y += Y

        out_lines.append("{:.4f} {:.4f} {:.4f}".format(X, Y, Z))

    sys.stdout.write("\n".join(out_lines))

    if total_pixels > 0:
        avg_Y = sum_Y / total_pixels
        sys.stdout.write("\nThe average of Y is {:.4f}\n".format(avg_Y))


if __name__ == '__main__':
    main()

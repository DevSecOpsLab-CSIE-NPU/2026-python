import sys


def solve(data):
    values = data.split()

    if not values:
        return ""

    pos = 0
    n = int(values[pos])
    pos += 1

    total_pixels = n * n
    result_lines = []
    y_sum = 0.0

    for _ in range(total_pixels):
        r = int(values[pos])
        g = int(values[pos + 1])
        b = int(values[pos + 2])
        pos += 3

        x = 0.5149 * r + 0.3244 * g + 0.1607 * b
        y = 0.2654 * r + 0.6704 * g + 0.0642 * b
        z = 0.0248 * r + 0.1248 * g + 0.8504 * b

        y_sum += y
        result_lines.append(f"{x:.4f} {y:.4f} {z:.4f}")

    average_y = y_sum / total_pixels
    result_lines.append(f"The average of Y is {average_y:.4f}")

    return "\n".join(result_lines)


def main():
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()
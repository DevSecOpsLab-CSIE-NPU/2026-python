import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    values = data[1:]
    total_pixels = n * n

    output = []
    sum_y = 0.0
    index = 0

    for _ in range(total_pixels):
        red = values[index]
        green = values[index + 1]
        blue = values[index + 2]
        index += 3

        x = 0.5149 * red + 0.3244 * green + 0.1607 * blue
        y = 0.2654 * red + 0.6704 * green + 0.0642 * blue
        z = 0.0248 * red + 0.1248 * green + 0.8504 * blue
        sum_y += y
        output.append(f"{x:.4f} {y:.4f} {z:.4f}")

    average_y = sum_y / total_pixels
    output.append(f"The average of Y is {average_y:.4f}")
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()
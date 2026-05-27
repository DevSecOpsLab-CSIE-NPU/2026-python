import sys


def count_squares(a, b):
    count = 0
    number = 1

    while number * number <= b:
        square = number * number

        if square >= a:
            count += 1

        number += 1

    return count


def solve(data):
    parts = data.split()
    output = []

    for i in range(0, len(parts), 2):
        a = int(parts[i])
        b = int(parts[i + 1])

        if a == 0 and b == 0:
            break

        output.append(str(count_squares(a, b)))

    return "\n".join(output)


def main():
    data = sys.stdin.read()
    answer = solve(data)
    print(answer)


if __name__ == "__main__":
    main()
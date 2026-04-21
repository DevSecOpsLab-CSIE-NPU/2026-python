import sys


cache = {1: 1}


def cycle_length(number: int) -> int:
    original = number
    trail = []

    while number not in cache:
        trail.append(number)
        if number % 2 == 1:
            number = 3 * number + 1
        else:
            number //= 2

    length = cache[number]
    for value in reversed(trail):
        length += 1
        cache[value] = length

    return cache[original]


def main() -> None:
    data = sys.stdin.buffer.read().split()
    output = []

    for index in range(0, len(data), 2):
        first = int(data[index])
        second = int(data[index + 1])
        left = min(first, second)
        right = max(first, second)
        best = 0

        for number in range(left, right + 1):
            current = cycle_length(number)
            if current > best:
                best = current

        output.append(f"{first} {second} {best}")

    sys.stdout.write("\n".join(output) + ("\n" if output else ""))


if __name__ == "__main__":
    main()
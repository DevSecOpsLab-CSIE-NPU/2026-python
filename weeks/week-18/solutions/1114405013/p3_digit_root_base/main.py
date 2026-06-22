import sys


BASE = 3


def digit_sum_in_base(number):
    total = 0

    if number == 0:
        return 0

    while number > 0:
        total += number % BASE
        number //= BASE

    return total


def digit_root(number):
    while number >= BASE:
        number = digit_sum_in_base(number)
    return number


def main():
    outputs = []

    for line in sys.stdin.read().splitlines():
        number = int(line)
        outputs.append(str(digit_root(number)))

    if outputs:
        sys.stdout.write("\n".join(outputs) + "\n")


if __name__ == "__main__":
    main()

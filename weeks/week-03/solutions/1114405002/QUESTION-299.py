import sys


def inversion_count(numbers):
    swaps = 0
    size = len(numbers)

    for i in range(size):
        for j in range(i + 1, size):
            if numbers[i] > numbers[j]:
                swaps += 1

    return swaps


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    case_count = data[0]
    position = 1
    output = []

    for _ in range(case_count):
        train_length = data[position]
        position += 1
        train = data[position:position + train_length]
        position += train_length
        swaps = inversion_count(train)
        output.append(f"Optimal train swapping takes {swaps} swaps.")

    sys.stdout.write("\n".join(output) + ("\n" if output else ""))


if __name__ == "__main__":
    main()
D = 2


def clean_sequence(numbers: list[int], d: int) -> list[int]:
    """
    Remove duplicate numbers while preserving first occurrence,
    keep numbers divisible by d, then sort in ascending order.
    """
    seen = set()
    unique_numbers = []

    for number in numbers:
        if number not in seen:
            seen.add(number)
            unique_numbers.append(number)

    filtered_numbers = [
        number for number in unique_numbers
        if number % d == 0
    ]

    return sorted(filtered_numbers)


def solve(input_text: str, d: int = D) -> str:
    """
    Parse multiple test cases from token stream.

    Input format:
        n a1 a2 ... an n a1 a2 ... an 0

    n decides how many numbers belong to the current array.
    Newlines are not used to decide where an array ends.
    """
    tokens = input_text.split()

    if not tokens:
        return ""

    outputs = []
    index = 0

    while index < len(tokens):
        n = int(tokens[index])
        index += 1

        if n == 0:
            break

        numbers = []

        for _ in range(n):
            if index >= len(tokens):
                break

            numbers.append(int(tokens[index]))
            index += 1

        result = clean_sequence(numbers, d)

        if result:
            outputs.append(" ".join(map(str, result)))
        else:
            outputs.append("NONE")

    return "\n".join(outputs)


def main() -> None:
    outputs = []

    while True:
        n = int(input().strip())

        if n == 0:
            break

        numbers = []

        while len(numbers) < n:
            numbers.extend(map(int, input().split()))

        numbers = numbers[:n]
        result = clean_sequence(numbers, D)

        if result:
            outputs.append(" ".join(map(str, result)))
        else:
            outputs.append("NONE")

    if outputs:
        print("\n".join(outputs))


if __name__ == "__main__":
    main()
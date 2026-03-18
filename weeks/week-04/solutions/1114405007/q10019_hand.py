def count_ones(number):
    binary_text = bin(number)
    return binary_text.count("1")


def solve(data):
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    total_cases = int(lines[0])
    answers = []

    for number_text in lines[1 : 1 + total_cases]:
        decimal_value = int(number_text)
        first_count = count_ones(decimal_value)

        hex_value = int(number_text, 16)
        second_count = count_ones(hex_value)
        answers.append(f"{first_count} {second_count}")

    return "\n".join(answers)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()), end="")
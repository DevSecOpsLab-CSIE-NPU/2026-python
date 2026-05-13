import sys


def digit_sum(text):
    return sum(ord(ch) - 48 for ch in text)


def degree_of_nine(text):
    total = digit_sum(text)
    degree = 1

    while total >= 10:
        total = digit_sum(str(total))
        degree += 1

    return degree


def solve():
    output = []

    for line in sys.stdin:
        number = line.strip()
        if number == "0":
            break

        if digit_sum(number) % 9 != 0:
            output.append(f"{number} is not a multiple of 9.")
        else:
            output.append(f"9-degree of {number} is {degree_of_nine(number)}.")

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()
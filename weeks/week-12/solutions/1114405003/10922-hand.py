import sys


def sum_digits(value):
    total = 0
    for ch in value:
        total += ord(ch) - 48
    return total


def main():
    out = []

    for line in sys.stdin:
        s = line.strip()
        if s == "0":
            break

        n = sum_digits(s)
        if n % 9 != 0:
            out.append(f"{s} is not a multiple of 9.")
            continue

        degree = 1
        while n >= 10:
            n = sum_digits(str(n))
            degree += 1

        out.append(f"9-degree of {s} is {degree}.")

    sys.stdout.write("\n".join(out))


main()
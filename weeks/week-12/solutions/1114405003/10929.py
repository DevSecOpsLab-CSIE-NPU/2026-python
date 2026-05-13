import sys


def solve():
    output = []

    for line in sys.stdin:
        number = line.strip()
        if number == "0":
            break

        balance = 0
        sign = 1

        for ch in reversed(number):
            balance += sign * (ord(ch) - 48)
            sign *= -1

        if balance % 11 == 0:
            output.append(f"{number} is a multiple of 11.")
        else:
            output.append(f"{number} is not a multiple of 11.")

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()
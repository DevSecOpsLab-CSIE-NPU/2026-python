import sys


def solve():
    output = []

    for token in sys.stdin.read().split():
        number = int(token)
        if number == 0:
            break

        binary = bin(number)[2:]
        ones = binary.count("1")
        output.append(f"The parity of {binary} is {ones} (mod 2).")

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()
import sys


def main():
    ans = []

    for token in sys.stdin.read().split():
        n = int(token)
        if n == 0:
            break

        bits = []
        ones = 0

        while n > 0:
            bit = n % 2
            bits.append(str(bit))
            if bit == 1:
                ones += 1
            n //= 2

        bits.reverse()
        b = "".join(bits)
        ans.append(f"The parity of {b} is {ones} (mod 2).")

    sys.stdout.write("\n".join(ans))


main()
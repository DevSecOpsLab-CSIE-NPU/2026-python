import sys


def main():
    res = []

    for line in sys.stdin:
        s = line.strip()
        if s == "0":
            break

        diff = 0
        plus = True
        for ch in s[::-1]:
            val = ord(ch) - 48
            if plus:
                diff += val
            else:
                diff -= val
            plus = not plus

        if diff % 11 == 0:
            res.append(f"{s} is a multiple of 11.")
        else:
            res.append(f"{s} is not a multiple of 11.")

    sys.stdout.write("\n".join(res))


main()
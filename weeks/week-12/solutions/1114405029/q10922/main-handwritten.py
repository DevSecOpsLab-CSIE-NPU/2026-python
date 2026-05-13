import sys

def main():
    for line in sys.stdin:
        s = line.strip()

        if s == "0":
            break

        current = s
        degree = 0

        while True:
            total = 0

            for ch in current:
                total += int(ch)

            degree += 1

            if total == 9:
                print(
                    f"{s} is a multiple of 9 and has 9-degree {degree}."
                )
                break

            if total < 9:
                print(
                    f"{s} is not a multiple of 9."
                )
                break

            current = str(total)

if __name__ == "__main__":
    main()
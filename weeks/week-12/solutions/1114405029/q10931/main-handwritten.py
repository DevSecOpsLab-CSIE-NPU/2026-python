import sys

def main():
    for line in sys.stdin:
        n = int(line.strip())

        if n == 0:
            break

        binary = []
        count = 0
        current = n

        while current > 0:
            bit = current % 2

            binary.append(str(bit))

            if bit == 1:
                count += 1

            current //= 2

        binary.reverse()

        binary_string = "".join(binary)

        print(
            f"The parity of {binary_string} is {count} (mod 2)."
        )

if __name__ == "__main__":
    main()
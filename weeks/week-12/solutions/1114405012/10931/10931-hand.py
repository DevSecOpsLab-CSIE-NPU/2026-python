import sys

def main() -> None:
    for raw in sys.stdin:
        value = raw.strip()
        if value == "0":
            break
        if not value:
            continue

        bits = bin(int(value))[2:]
        count = bits.count("1")
        print(f"The parity of {bits} is {count} (mod 2).")

if __name__ == "__main__":
    main()
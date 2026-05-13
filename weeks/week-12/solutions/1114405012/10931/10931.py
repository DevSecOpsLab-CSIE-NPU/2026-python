import sys


def solve() -> None:
    for line in sys.stdin:
        text = line.strip()
        if text == "0":
            break
        if not text:
            continue

        number = int(text)
        binary = format(number, "b")
        ones = binary.count("1")
        print(f"The parity of {binary} is {ones} (mod 2).")


if __name__ == "__main__":
    solve()
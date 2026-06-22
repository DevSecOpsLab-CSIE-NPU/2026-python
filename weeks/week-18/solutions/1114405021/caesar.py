import sys

SHIFT = 2


def shift_char(c: str) -> str:
    if "A" <= c <= "Z":
        return chr((ord(c) - ord("A") + SHIFT) % 26 + ord("A"))
    if "a" <= c <= "z":
        return chr((ord(c) - ord("a") + SHIFT) % 26 + ord("a"))
    return c


def encrypt_line(line: str) -> str:
    return "".join(shift_char(c) for c in line)


def main():
    data = sys.stdin.read().splitlines()
    out = [encrypt_line(line) for line in data]
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

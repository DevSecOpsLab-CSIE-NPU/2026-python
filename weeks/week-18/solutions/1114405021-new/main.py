import sys

SHIFT = 2


def shift_char(ch: str, shift: int) -> str:
    if "A" <= ch <= "Z":
        base = ord("A")
        return chr((ord(ch) - base + shift) % 26 + base)
    if "a" <= ch <= "z":
        base = ord("a")
        return chr((ord(ch) - base + shift) % 26 + base)
    return ch


def encrypt_line(text: str, shift: int = SHIFT) -> str:
    return "".join(shift_char(ch, shift) for ch in text)


def main():
    for line in sys.stdin:
        sys.stdout.write(encrypt_line(line.rstrip("\n")) + "\n")


if __name__ == "__main__":
    main()
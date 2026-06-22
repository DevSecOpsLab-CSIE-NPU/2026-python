import sys


SHIFT = 4


def shift_char(char):
    if "a" <= char <= "z":
        return chr((ord(char) - ord("a") + SHIFT) % 26 + ord("a"))
    if "A" <= char <= "Z":
        return chr((ord(char) - ord("A") + SHIFT) % 26 + ord("A"))
    return char


def main():
    text = sys.stdin.read()
    sys.stdout.write("".join(shift_char(char) for char in text))


if __name__ == "__main__":
    main()

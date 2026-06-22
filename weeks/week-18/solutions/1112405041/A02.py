def caesar_encrypt(text, shift):
    raise NotImplementedError


def main():
    import sys
    for line in sys.stdin:
        line = line.rstrip("\n")
        print(caesar_encrypt(line, shift=2))


if __name__ == "__main__":
    main()

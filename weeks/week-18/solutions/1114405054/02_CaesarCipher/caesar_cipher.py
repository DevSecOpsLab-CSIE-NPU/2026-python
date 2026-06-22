def caesar_cipher(text: str, shift: int) -> str:
    result = []
    for ch in text:
        if "A" <= ch <= "Z":
            result.append(chr((ord(ch) - ord("A") + shift) % 26 + ord("A")))
        elif "a" <= ch <= "z":
            result.append(chr((ord(ch) - ord("a") + shift) % 26 + ord("a")))
        else:
            result.append(ch)
    return "".join(result)


def main():
    import sys
    for line in sys.stdin:
        line = line.rstrip("\n")
        print(caesar_cipher(line, 5))


if __name__ == "__main__":
    main()

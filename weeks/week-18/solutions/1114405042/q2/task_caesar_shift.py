SHIFT = 3

def caesar_encrypt(text):
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + SHIFT) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + SHIFT) % 26 + ord('A')))
        else:
            result.append(ch)
    return "".join(result)

def main():
    import sys
    line = sys.stdin.readline()
    if not line:
        return
    line = line.rstrip('\n')
    sys.stdout.write(caesar_encrypt(line) + "\n")

if __name__ == "__main__":
    main()

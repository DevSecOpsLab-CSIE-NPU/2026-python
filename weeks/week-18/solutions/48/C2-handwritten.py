import sys

SHIFT = 9

def main():
    lines = sys.stdin.read().splitlines()
    for line in lines:
        out = []
        for ch in line:
            if 'A' <= ch <= 'Z':
                out.append(chr((ord(ch) - 65 + SHIFT) % 26 + 65))
            elif 'a' <= ch <= 'z':
                out.append(chr((ord(ch) - 97 + SHIFT) % 26 + 97))
            else:
                out.append(ch)
        print("".join(out))

if __name__ == "__main__":
    main()

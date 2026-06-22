import sys

SHIFT = 9

def main():
    lines = sys.stdin.read().splitlines()
    for line in lines:
        result = []
        for ch in line:
            if 'A' <= ch <= 'Z':
                result.append(chr((ord(ch) - ord('A') + SHIFT) % 26 + ord('A')))
            elif 'a' <= ch <= 'z':
                result.append(chr((ord(ch) - ord('a') + SHIFT) % 26 + ord('a')))
            else:
                result.append(ch)
        print("".join(result))

if __name__ == "__main__":
    main()

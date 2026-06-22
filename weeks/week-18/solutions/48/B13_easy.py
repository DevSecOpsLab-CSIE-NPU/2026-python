import sys

BASE = 13

def main():
    data = sys.stdin.read().splitlines()
    for line in data:
        line = line.strip()
        if not line:
            continue
        x = int(line)

        if x == 0:
            print(0)
            continue

        while x >= BASE:
            s = 0
            while x > 0:
                s += x % BASE
                x //= BASE
            x = s

        print(x)

if __name__ == "__main__":
    main()

import sys

BASE = 13

def main():
    lines = sys.stdin.read().splitlines()
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        x = int(line)

        if x == 0:
            print(0)
            continue

        while x >= BASE:
            total = 0
            while x > 0:
                total = total + (x % BASE)
                x = x // BASE
            x = total

        print(x)

if __name__ == "__main__":
    main()

import sys

def main():
    n = int(sys.stdin.readline())

    for _ in range(n):
        s, d = map(int, sys.stdin.readline().split())

        if d > s:
            print("impossible")
            continue

        if (s + d) % 2 != 0:
            print("impossible")
            continue

        high = (s + d) // 2
        low = (s - d) // 2

        print(high, low)

if __name__ == "__main__":
    main()
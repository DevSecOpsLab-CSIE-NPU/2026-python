def cycle_len(n):

    count = 1

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1

    return count


def main():

    import sys

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            lines = f.readlines()
    else:
        lines = sys.stdin

    for line in lines:
        line = line.strip()
        if not line:
            continue
        i, j = map(int, line.split())
        start, end = min(i, j), max(i, j)
        max_len = max(cycle_len(n) for n in range(start, end + 1))

        print(i, j, max_len)

if __name__ == "__main__":
    main()
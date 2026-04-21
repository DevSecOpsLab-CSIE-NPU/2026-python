import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    cases = data[0]
    p = 1
    result = []

    for _ in range(cases):
        count = data[p]
        p += 1
        arr = data[p:p + count]
        p += count

        arr.sort()
        base = arr[count // 2]

        dist = 0
        for x in arr:
            dist += abs(x - base)
        result.append(str(dist))

    sys.stdout.write("\n".join(result))


if __name__ == "__main__":
    main()

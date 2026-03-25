import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        r = data[idx]
        idx += 1
        arr = data[idx:idx + r]
        idx += r

        arr.sort()
        m = arr[r // 2]
        out.append(str(sum(abs(x - m) for x in arr)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

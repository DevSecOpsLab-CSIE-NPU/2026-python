import sys


def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return

    t = int(raw[0])
    pos = 1
    result = []

    for _ in range(t):
        s = int(raw[pos])
        d = int(raw[pos + 1])
        pos += 2

        if s < d or (s + d) % 2 == 1:
            result.append("impossible")
        else:
            a = (s + d) // 2
            b = s - a
            result.append(f"{a} {b}")

    sys.stdout.write("\n".join(result))


main()
import sys


memo = {1: 1}


def length_of_chain(n):
    trail = []
    value = n

    while value not in memo:
        trail.append(value)
        if value % 2:
            value = 3 * value + 1
        else:
            value //= 2

    steps = memo[value]
    while trail:
        steps += 1
        memo[trail.pop()] = steps

    return memo[n]


def main():
    tokens = sys.stdin.buffer.read().split()
    out = []

    for i in range(0, len(tokens), 2):
        a = int(tokens[i])
        b = int(tokens[i + 1])
        start = a if a < b else b
        stop = b if a < b else a
        best = 0

        for number in range(start, stop + 1):
            current = length_of_chain(number)
            if current > best:
                best = current

        out.append(f"{a} {b} {best}")

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


if __name__ == '__main__':
    main()
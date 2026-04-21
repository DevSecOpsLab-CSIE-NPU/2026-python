import sys


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    w = max(len(x) for x in lines)
    h = len(lines)
    out = []

    for c in range(w):
        row = []
        for r in range(h - 1, -1, -1):
            s = lines[r]
            row.append(s[c] if c < len(s) else ' ')
        out.append(''.join(row))

    sys.stdout.write('\n'.join(out) + ('\n' if out else ''))


if __name__ == '__main__':
    main()
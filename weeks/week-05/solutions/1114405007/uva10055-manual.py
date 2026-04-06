from sys import stdin


def main():
    out = []
    for line in stdin:
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        out.append(str(abs(a - b)))

    print("\n".join(out))


if __name__ == "__main__":
    main()